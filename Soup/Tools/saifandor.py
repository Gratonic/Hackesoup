# [=== Imports ===] #
from extraction import Extractor
from colorama import Fore
from halo import Halo
import tldextract
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

class DNS():
    def __init__(self):
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = [
            "9.9.9.9",        "149.112.112.112", # Quad9
            "1.1.1.1",        "1.0.0.1",         # Cloudflare DNS
            "8.8.8.8",        "8.8.4.4",         # Google DNS
            "208.67.222.222", "208.67.220.220"   # OpenDNS
        ]

    def resolve(self, domain: str):
        try:
            self.resolver.resolve(domain, 'CNAME')
            return 200
        except dns.resolver.AccessDenied:
            return 403
        except:
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
        working_indicator = Halo(text="fetching subdomain information", spinner="bouncingBar")
        target_url = self.clean_url()

        working_indicator.start()

        api_url = f"https://crt.sh/?q=%25.{target_url}&output=json"
        headers = {"User-Agent": random.choice(user_agents)}

        response = requests.get(url=api_url, headers=headers, timeout=30)

        if response.status_code == 200:
            self.records = response.json()
        else:
            print(f"{Fore.RED}[!] Error: fetch failed with status code: {Fore.YELLOW}{response.status_code}{Fore.RESET}")
            exit_program()
        
        self.process_records()

        self.check_status_codes()

        working_indicator.stop()




    """
    {
        {
            'issuer_ca_id': 4, 
            'issuer_name': 'C=US, O=Google Inc, CN=Google Internet Authority',
            'common_name': 'freezone.google.com', 
            'name_value': 'accounts.freezone.google.com\nfreezone.google.com\ngaiastaging.freezone.google.com\nmail.freezone.google.com\nnews.freezone.google.com\nplus.freezone.google.com\nsearch.freezone.google.com\nwww.freezone.google.com', 
            'id': 1708824, 'entry_timestamp': '2013-04-27T12:11:35.274', 
            'not_before': '2013-04-24T15:07:26', 
            'not_after': '2013-12-30T15:07:26', 
            'serial_number': '1403460a000100008520', 
            'result_count': 9
        }
    }
    """

    def process_records(self) -> list:
        record_data = {"subdomains": None, "emails": None, "CA_names": None, "cert_issue_dates": None}
        email_and_subdomain_data = []
        CA_name_data = []
        cert_issue_date_data = []

        records = self.records
        for record in records:
            common_name = record["common_name"]
            name_value = record["name_value"]
            issuer_name = record["issuer_name"]
            cert_issue_date = record["not_before"]

            email_and_subdomain_data.append(common_name)
            email_and_subdomain_data.append(name_value)
            CA_name_data.append(issuer_name)
            cert_issue_date_data.append(cert_issue_date)
        
        subdomains = []
        emails = []
        for entry in email_and_subdomain_data:
            data = entry.split("\n")
            for chunk in data:
                if "@" in chunk:
                    emails.append(chunk.strip())
                else:
                    subdomains.append(chunk.strip())
        
        CA_names = []
        for entry in CA_name_data:
            data = entry.split(",")
            for chunk in data:
                if chunk.startswith("CN="):
                    chunk = chunk.strip("CN=")
                    chunk = chunk.strip()
                    CA_names.append(chunk)
                else:
                    continue
        
        cert_issue_dates = []
        for entry in cert_issue_date_data:
            cert_issue_dates.append(entry.split("T")[0])
        
        record_data["subdomains"] = subdomains
        record_data["emails"] = emails
        record_data["CA_names"] = CA_names
        record_data["cert_issue_dates"] = cert_issue_dates

        self.records = record_data

    def check_status_codes(self):
        dns = DNS()
        records = self.records
        status_codes = []

        for index, subdomain in enumerate(records["subdomains"], start=0):
            status_code = dns.resolve(domain=subdomain)
            if status_code != None:
                status_codes.append(status_code)
            else:
                print(f"\nBye Bye {subdomain}")
                records["subdomains"].pop(index)
                records["CA_names"].pop(index)
                records["cert_issue_dates"].pop(index)




def display_header():
    ascii_banner = """
     _____       _  __                _            
    /  ___|     (_)/ _|              | |           
    \\ `--.  __ _ _| |_ __ _ _ __   __| | ___  _ __ 
     `--. \\/ _` | |  _/ _` | '_ \\ / _` |/ _ \\| '__|
    /\\__/ / (_| | | || (_| | | | | (_| | (_) | |   
    \\____/ \\__,_|_|_| \\__,_|_| |_|\\__,_|\\___/|_|   """
    title_colors = [Fore.RED, Fore.YELLOW, Fore.WHITE, Fore.GREEN]
    colorful_banner = ''.join(title_colors[char % len(title_colors)] + ascii_banner[char] for char in range(len(ascii_banner)))
    
    title_bar = f"{Fore.YELLOW}_________________________________________________________________________/{Fore.RESET}"

    header = f"{colorful_banner}\n{title_bar}\n{Fore.BLUE}Saifandor v1.0{Fore.RESET}"
    print(header)

def test():
    working_indicator = Halo(text="fetching subdomain information", spinner="bouncingBar")
    saifandor = Saifandor()
    display_header()
    working_indicator.start()
    saifandor.fetch_records()

# TODO:

"""
1) Find the domains, emails, CA Name, and the certificate issue date in data
2) Check the status code of each domain (200, 403, 401, and 408 are good)
3) Finish the output display
"""