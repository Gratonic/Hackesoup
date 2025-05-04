import requests, json, re, os, sys, dns.resolver, logging, random, time
from collections import defaultdict
from datetime import datetime

with open("../Soup/Lib/Data/Input_Data/input.json") as file:
    print(file)
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("scanner.log"),
        logging.StreamHandler()
    ]
)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15"
]

VULNERABLE_SERVICES = {
    'aws_s3': {
        'cname_patterns': ['.s3.amazonaws.com', '.s3-website'],
        'response_patterns': ['NoSuchBucket', 'BucketNotFound'],
        'status_codes': [404, 403]
    },
    'github_pages': {
        'cname_patterns': ['.github.io'],
        'response_patterns': ['There isn\'t a GitHub Pages site here'],
        'status_codes': [404]
    }
}

class DNSCacheResolver:
    def __init__(self):
        self.cache = {}
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = ['8.8.8.8', '1.1.1.1']
    
    def resolve(self, domain):
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
    def __init__(self):
        self.resolver = DNSCacheResolver()
        self.valid_domain_pattern = re.compile(r'^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$')

    def sanitize_domain(self, domain):
        domain = re.sub(r'(https?://)|(www\.)|/.*|\s+', '', domain.strip().lower())
        if not self.valid_domain_pattern.match(domain):
            raise ValueError(f"Invalid domain format: {domain}")
        return domain.split(':')[0]

    def fetch_subdomains(self, domain):
        cleaned_domain = self.sanitize_domain(domain)
        api_url = f"https://crt.sh/?q=%25.{cleaned_domain}&output=json"
        headers = {'User-Agent': random.choice(USER_AGENTS)}

        try:
            time.sleep(random.uniform(1.5, 3.5))
            response = requests.get(api_url, headers=headers, timeout=30)
            response.raise_for_status()
            records = response.json()
            subdomains = set()

            for record in records:
                names = record.get('name_value', '').split('\n')
                for name in names:
                    name = self.clean_subdomain(name)
                    if name and name != cleaned_domain:
                        subdomains.add(name)

            return sorted(subdomains, key=lambda x: x.count('.'), reverse=True)
        except Exception as e:
            logging.error(f"Subdomain fetch failed: {str(e)}")
            return []

    def clean_subdomain(self, name):
        name = re.sub(r'^\*\.|[^\w\.-]', '', name.strip().lower())
        return name if self.valid_domain_pattern.match(name) else None

    def check_vulnerabilities(self, subdomains):
        vulnerable = defaultdict(list)

        for subdomain in subdomains:
            try:
                answers = self.resolver.resolve(subdomain)
                if not answers:
                    continue
                cname = str(answers[0].target).lower()

                for service, patterns in VULNERABLE_SERVICES.items():
                    if any(p in cname for p in patterns['cname_patterns']):
                        if self.confirm_vulnerability(subdomain, service):
                            vulnerable[service].append({
                                'subdomain': subdomain,
                                'cname': cname,
                                'verified': datetime.now().isoformat()
                            })
                time.sleep(random.uniform(1, 2))
            except Exception as e:
                logging.warning(f"Check failed for {subdomain}: {str(e)}")

        return vulnerable

    def confirm_vulnerability(self, subdomain, service):
        try:
            headers = {'User-Agent': random.choice(USER_AGENTS)}
            response = requests.get(f"http://{subdomain}", headers=headers, timeout=15, allow_redirects=False)
            patterns = VULNERABLE_SERVICES[service]
            if response.status_code in patterns['status_codes']:
                return any(p in response.text for p in patterns['response_patterns'])
        except requests.exceptions.RequestException:
            return False
        return False

    def save_results(self, results, filename="scan_results.json"):
        output = {
            'metadata': {
                'scan_date': datetime.now().isoformat(),
                'total_subdomains': len(results['subdomains']),
                'vulnerabilities_found': len(results['vulnerabilities'])
            },
            'results': results
        }
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
            logging.info(f"Results saved to {filename}")
        except Exception as e:
            logging.error(f"Failed to save results: {str(e)}")

    def run_scan(self, domain):
        logging.info(f"Starting scan for: {domain}")
        subdomains = self.fetch_subdomains(domain)
        vulnerabilities = self.check_vulnerabilities(subdomains)
        results = {
            'target': domain,
            'subdomains': subdomains,
            'vulnerabilities': vulnerabilities
        }
        self.save_results(results)
        return results

if __name__ == "__main__":
    scanner = SubdomainScanner()
    try:
        target_domain = input("Enter the domain to scan: ").strip()
        results = scanner.run_scan(target_domain)

        print("\nScan Results:")
        print(f"Total Subdomains Found: {len(results['subdomains'])}")
        print(f"Potential Vulnerabilities: {len(results['vulnerabilities'])}")

        for service, entries in results['vulnerabilities'].items():
            print(f"\n{service.upper()} Vulnerabilities:")
            for entry in entries:
                print(f" - {entry['subdomain']} => {entry['cname']}")

    except KeyboardInterrupt:
        logging.info("Scan interrupted by user")
        sys.exit(0)
    except Exception as e:
        logging.error(f"Critical failure: {str(e)}")
        sys.exit(1)