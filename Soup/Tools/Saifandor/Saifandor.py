"""
# -- Author Information and Program Details -- #

File Name: subdomain.py
Author: ibrahim abu al roos (https://github.com/ibrahim-sisar)
Written In: Python 3.12.6
modul(s): sys, os, colorama, requests, re, json, datetime, dns.resolver , random, time, concurrent.futures
Last Modified: May 5th, 2025

# :: Description :: #

A Python-based subdomain enumeration and subdomain takeover scanner.

This tool performs the following tasks:
1. Fetches subdomains of a target domain using crt.sh or a custom wordlist.
2. Resolves CNAME records for the discovered subdomains.
3. Detects possible subdomain takeover vulnerabilities by identifying:
   - Known vulnerable hosting providers (e.g., AWS S3, GitHub Pages).
   - Suspicious CNAMEs pointing to unresponsive services.
4. Flags subdomains that require manual review due to weak HTTP responses or unknown hosting.
5. Logs results and optionally saves them in a structured JSON file.

"""

# -- Imports -- #

import requests, json, re, os, sys, dns.resolver, random, time
from colorama import Style,Fore
from collections import defaultdict
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load input configuration from JSON
with open("../Soup/Lib/Data/Input_Data/input.json") as file:
    data = json.load(file)


# User-Agent pool for HTTP requests
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15"
]

vulnerable_status_code = [400, 403, 404, 502, 503]

def status_messages(message):
    """Prints status messages to the console."""
    print(f"\r{Fore.YELLOW}[PROGRESS] Please wait.{message} {Style.RESET_ALL}", end='')
    sys.stdout.flush()

class DNSCacheResolver:
    """
    Handles DNS CNAME resolution with caching to improve performance.

    - Uses Google (8.8.8.8) and Cloudflare (1.1.1.1) as resolvers.
    - Caches resolved records to avoid redundant DNS queries.
    - Gracefully handles failures by returning None on exceptions.
    """
    def __init__(self):
        self.cache = {}
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = ['8.8.8.8', '1.1.1.1']

    def resolve(self, domain):
        """Resolves CNAME records with caching."""
        if domain in self.cache:
            return self.cache[domain]
        try:
            result = self.resolver.resolve(domain, 'CNAME')
            self.cache[domain] = result
            return result
        except Exception:
            self.cache[domain] = None
            return None

class SubdomainScanner:
    """
    Main engine that handles the full subdomain discovery and vulnerability checking pipeline.

    Features:
    - Sanitizes input domain names.
    - Loads subdomains from crt.sh or a custom wordlist.
    - Resolves subdomain CNAMEs and checks them against known vulnerable patterns.
    - Confirms potential vulnerabilities via HTTP response analysis.
    - Supports RPM throttling and concurrent processing.
    - Logs all major steps and can optionally save results in JSON format.
    """

    def __init__(self, config):
        self.config = config
        self.rpm = config.get("rpm", 180)
        self.timeout = config.get("timeout", 5)
        self.payload_file = config.get("payload_file", None)
        self.resolver = DNSCacheResolver()
        self.valid_domain_pattern = re.compile(r'^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$') # N/A

    def sanitize_domain(self, domain):
        """Sanitizes and validates the input domain name."""
        domain = re.sub(r'(https?://)|(www\.)|/.*|\s+', '', domain.strip().lower())
        if not self.valid_domain_pattern.match(domain):
            raise ValueError(f"Invalid domain format: {domain}")
        return domain.split(':')[0]

    def load_custom_payload(self):
        """Loads subdomains from a custom wordlist file if defined."""
        try:
            status_messages("Loading custom payload...")
            with open(self.payload_file, "r") as f:
                return [line.strip() for line in f if line.strip()]
        except Exception as e:
            status_messages("Failed to load custom payload.")
            print(f"{Fore.RED}[!] Failed to load payload file: {e}{Style.RESET_ALL}")
            return []

    def fetch_subdomains(self, domain):
        """
        Retrieves subdomains from crt.sh or from custom payload if provided.
        Returns a sorted list of sanitized subdomains.
        Implements a retry mechanism for network timeouts.
        """
        cleaned_domain = self.sanitize_domain(domain)

        if self.payload_file:
            subdomains = [f"{sub}.{cleaned_domain}" for sub in self.load_custom_payload()]
            print(f"{Fore.YELLOW}Loaded {len(subdomains)} subdomains from custom payload.{Style.RESET_ALL}")
            return subdomains

        api_url = f"https://crt.sh/?q=%25.{cleaned_domain}&output=json"
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        retries = 3  # Number of retry attempts

        for attempt in range(retries):
            try:
                time.sleep(random.uniform(1, 2))
                status_messages(f"Fetching subdomains from crt.sh (Attempt {attempt + 1}/{retries})...")
                response = requests.get(api_url, headers=headers, timeout=self.timeout)
                response.raise_for_status()
                records = response.json()
                status_messages("Subdomains fetched successfully.")
                subdomains = set()

                for index, record in enumerate(records):
                    names = record.get('name_value', '').split('\n')
                    status_messages(f"Processing [{len(records)}\\{index + 1}] records..." + " " * 20)
                    for name in names:
                        name = self.clean_subdomain(name)
                        if name and name != cleaned_domain:
                            subdomains.add(name)

                return sorted(subdomains, key=lambda x: x.count('.'), reverse=True)
            except requests.exceptions.RequestException as e:
                print(f"{Fore.RED}\n[!] Attempt {attempt + 1} failed: {str(e)}{Style.RESET_ALL}")
                if attempt == retries - 1:
                    print(f"{Fore.RED}[!] All retry attempts failed. Aborting subdomain fetch.{Style.RESET_ALL}")
                    return []

    def clean_subdomain(self, name):
        """Cleans and validates individual subdomain strings."""
        name = re.sub(r'^\*\.|[^\w\.-]', '', name.strip().lower())
        return name if self.valid_domain_pattern.match(name) else None

    def check_vulnerabilities(self, subdomains):
        """
        Concurrently checks each subdomain's HTTP response status code
        and ensures it has a CNAME. Returns those with vulnerable status codes.
        """
        vulnerable = []
        delay = 60 / self.rpm
        max_workers = min(30, len(subdomains))

        def process_subdomain(subdomain, index):
            status_messages(f"Checking [{index+1}\\{len(subdomains)}] subdomains..." + " " * 20)
            try:
                answers = self.resolver.resolve(subdomain)
                if not answers:
                    return None
                cname = str(answers[0].target).lower()

                headers = {'User-Agent': random.choice(USER_AGENTS)}
                response = requests.get(
                    f"http://{subdomain}",
                    headers=headers,
                    timeout=self.timeout,
                    allow_redirects=False
                )
                if response.status_code in vulnerable_status_code and cname:
                    return {'subdomain': subdomain, 'cname': cname, 'status_code': response.status_code}
            except Exception as e:
                pass
            finally:
                # Respect user-defined RPM
                time.sleep(random.uniform(delay * 0.8, delay * 1.2))
            return None

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(process_subdomain, sub, i)
                for i, sub in enumerate(subdomains)
            ]
            for future in as_completed(futures):
                result = future.result()
                if result:
                    vulnerable.append(result)

        return vulnerable

    def save_results(self, results, filename="Saifandor_results.json"):
        r"""Saves scanning results to a specified JSON file in the Hackesoup\Saves directory."""
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        output_dir = os.path.join(project_root, "Saves")
        os.makedirs(output_dir, exist_ok=True)

        output = {
            'metadata': {
                'scan_date': datetime.now().isoformat(),
                'total_subdomains': len(results['subdomains']),
                'vulnerabilities_found': len(results['vulnerabilities'])
            },
            'results': results
        }
        try:
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
            print(f"\r{Fore.YELLOW}[*] Results saved to {Fore.BLUE}{output_path}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to save results: {str(e)}{Style.RESET_ALL}")


    def run_scan(self, domain):
        """Main method to run the full scanning workflow."""
        subdomains = self.fetch_subdomains(domain)
    
        if not subdomains:
            print(f"{Fore.RED}[!] No subdomains found. Scan aborted.{Style.RESET_ALL}")
            return {
                'target': domain,
                'subdomains': [],
                'vulnerabilities': []
            }
    
        vulnerabilities = self.check_vulnerabilities(subdomains)
        results = {
            'target': domain,
            'subdomains': subdomains,
            'vulnerabilities': vulnerabilities
        }
        if data.get("save_file", False):
            self.save_results(results)
        print(f"\n{Fore.GREEN}[SUCCESS] {Fore.MAGENTA}Scan completed successfully.{" "*20}{Style.RESET_ALL}")
        return results

# CLI entry point
def cli_entry_point():
    """Command-line interface for the subdomain scanner."""
    scanner = SubdomainScanner(data)
    try:
        print("\033[?25l", end="\n", flush=True)
        results = scanner.run_scan(data["target"])
        print("\033[?25h", end="", flush=True)
        # print(f"\r{Fore.GREEN}[SUCCESS] {Fore.MAGENTA}Scan completed successfully.{" "*20}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Target Domain: {results['target']}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Total Subdomains Found: {len(results['subdomains'])}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Vulnerabilities Found: {len(results['vulnerabilities'])}{Style.RESET_ALL}")

        for entry in results['vulnerabilities']:
            print(f"{Fore.BLUE} - [{entry["status_code"]}] {entry['subdomain']} => {entry['cname']}{Style.RESET_ALL}")

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        output_dir = os.path.join(project_root, "Saves")

        if data.get("save_file", False):
            print(f"\n{Fore.GREEN}[+] Scan Results Saved to: {os.path.join(output_dir, 'Saifandor_results.json')}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[!] Critical failure: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)