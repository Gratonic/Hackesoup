# [=== Imports ===] #
from colorama import Fore
from halo import Halo
import requests
import dns.resolver
import colorama
import random
import time
import json
import re
import os
import sys

# Tool Plan
"""
Uses crt.sh to retrieve the following info:

* all domains/subdomains of a specified domain
* CA information for each discovered domain/subdomain
* email(s) found for each domain/subdomain dicovered in the crt.sh search
"""

# What the settings dict for the tool looks like:
"""
{
'target': 'https://www.google.com', 
'tool': 'subdomain_finder', 
'tool_class': 'WEB', 
'API_token': None, 
'port': None, 'port_range': None, 
'scan_type': None, 
'save_file': None
}
"""

# Example of what the ouput will look like
"""
<ascii title>
___________________/

[=== Discovered Domains ===]

    Domain Name         Domain IPv4     Status Code         CA     Cert Issued
------------------------------------------------------------------------------
[+] example0.com        <domain-ip>     status_code     <CA Name>    9/15/1995
------------------------------------------------------------------------------
[+] example1.com        <domain-ip>     status_code     <CA Name>    9/15/1995
------------------------------------------------------------------------------
[+] example2.com        <domain-ip>     status_code     <CA Name>    9/15/1995
------------------------------------------------------------------------------

[=== Discovered Emails ===]

    Domain              Domain IPv4        Email
-----------------------------------------------------------------------------
[+] example0.com        <domain-ip>     admin@example.com
-----------------------------------------------------------------------------
[+] example1.com        <domain-ip>     devteam@example.com
-----------------------------------------------------------------------------
[+] example2.com        <domain-ip>     support@example.com
-----------------------------------------------------------------------------

"""

# [=== Global Variables ===] #

settings = None

# user-agent pool for HTTP(S) requests
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15"
]

# [=== Special Functions ===] #
def exit_program():
    print("\n")
    print(f"{Fore.MAGENTA}\n\nغزة تنهي هذا اللقاء، لكنها لا تنتهي!{Fore.RESET}")
    exit()

# [=== Functionality ===] #

# fetches the settings
with open("../Soup/Lib/Data/Input_Data/input.json", "r") as settings_file:
    settings = json.load(settings_file)

class dns():
    def __init__(self):
        self.cache = {}
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = [
            "9.9.9.9",        "149.112.112.112", # Quad9
            "1.1.1.1",        "1.0.0.1",         # Cloudflare DNS
            "8.8.8.8",        "8.8.4.4",         # Google DNS
            "208.67.222.222", "208.67.220.220"   # OpenDNS
        ]

    def resolve(self, domain):
        # resolves certificate records with caching
        if domain in self.cache:
            return self.cache[domain]
        try:
            result = self.resolver.resolve(domain, 'CNAME')
            self.cache[domain] = result
            return result
        except Exception:
            self.cache[domain] = None
            return None

class Saifandor():
    def __init__(self):
        # NOTE: save_file will be None or a string of a file path
        self.target = settings["target"]
        self.save_file = settings["save_file"]
        # placeholder for records
        self.records = {}
    
    def clean_url(self) -> str | None:
        # Regex pattern to match the domain
        pattern = r'https?://(?:www\.)?([^/]+)'
        match = re.search(pattern, self.target)

        if match:
            # extracts the domain
            full_domain = match.group(1)
            # split the domain to get the main part (last two segments)
            domain_parts = full_domain.split('.')
            if len(domain_parts) > 2:
                # returns the last two segments for subdomains
                return '.'.join(domain_parts[-2:])
            else:
                # returns the domain if it's already in the correct format
                return full_domain
        else:
            print(f"{Fore.RED}[!] Error: Scan failed, the domain could not be scanned.{Fore.RESET}")
            exit_program()

    def fetch_records(self) -> None:
        working_indicator = Halo(text="fetching subdomain information", spinner="bar")
        target_url = self.clean_url()

        api_url = f"https://crt.sh/?q=%25.{target_url}&output=json"
        headers = {"User-Agent": random.choice(user_agents)}

        working_indicator.start()
        response = requests.get(url=api_url, headers=headers, timeout=30)
        records = response.json()
        self.records = records
        working_indicator.stop()

        processed_records = self.process_records()
        print(processed_records)



    def extract_subdomains(self, data: str) -> set:
        domain_pattern = r'\b(?:\*?\.[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'
        domains = re.findall(domain_pattern, data)
        return set(domains)

    def extract_emails(self, data: str) -> set:
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        emails = re.findall(email_pattern, data)
        return set(emails)
    
    def extract_certificate_data(self, record_data: dict) -> dict:
        cert_info = {}

        # Extract the issuer name and issue (not_before) date directly from the record_data
        issuer_name = record_data["issuer_name"]
        not_before = record_data["not_before"]

        # searches for the CA name
        ca_name_match = re.search(r'CN=([^,]+)', issuer_name)
        if ca_name_match != None:
            cert_info['ca_name'] = ca_name_match.group(1).strip()
        else:
            pass

        # extracts the date from the not_before date (issue_date)
        not_before = not_before.strip()
        issue_date_pattern = r'(\d{4}-\d{2}-\d{2})T\d{2}:\d{2}:\d{2}'
        issue_date = re.search(issue_date_pattern, not_before)
        cert_info["issue_date"] = issue_date.group(1).strip()

        return cert_info

    def process_records(self) -> list:
        cleaned_records = []

        records = self.records
        for index, record in enumerate(records):
            # domain fields
            common_name = record["common_name"]
            name_value = record["name_value"]
            # relevant certificate information fields
            rel_record_date = {"issuer_name": record["issuer_name"], "not_before": record["not_before"]}

            # extracts the subdomain(s) from the current record
            subdomains = []
            common_name_subdomains = [sub for sub in self.extract_subdomains(data=common_name)]
            for sub in common_name_subdomains:
                subdomains.append(sub)

            name_value_subdomains = [sub for sub in self.extract_subdomains(data=name_value)]
            for sub in name_value_subdomains:
                subdomains.append(sub)

            # extracts the email(s) from the current record
            emails = []
            common_name_emails = [email for email in self.extract_emails(data=common_name)]
            for email in common_name_emails:
                emails.append(email)
            
            name_value_emails = [email for email in self.extract_emails(data=name_value)]
            for email in name_value_emails:
                emails.append(email)
            
            # NOTE: The CA_name and issue data will be the same for all subdomains/emails found for the current record
            certificate_info = self.extract_certificate_data(record_data=rel_record_date)
            ca_name = certificate_info["ca_name"]
            issue_date = certificate_info["issue_date"]

            cleaned_records.append({"discovered_subdomains": subdomains, "CA": ca_name, "issue_date": issue_date})

def test():
    saifandor = Saifandor()
    saifandor.fetch_records()