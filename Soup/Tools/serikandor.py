# [=== Boilerplate ===] #

"""
# :: Author Information and Program Details :: #

File Name: serikandor.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.13.5
Dependencie(s): colorama, halo, asyncio, random, httpx, json, re, os
Last Modified: 8/4/2025

# :: Description :: #

This is the subdomain finder. It has the ability to find subdomains and emails in a websites certificate using
the crt.sh public internet library.

NOTE: The collected emails are owned by the subdomain owner, not the Certificate Authority (CA).

NOTE: The tool is still being worked on and if you would like to test some functionality, it will need to be
run under the test() function. Asyncronus features are used in some functions, so async must be used in the
test() function definition.
"""

# [=== Imports ===] #

import os
import random
import re

from colorama import Fore  # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
from halo import Halo
import dns.resolver
import requests

# [=== Tool Plan ===] #

"""
Uses crt.sh to retrieve the following info:

* all domains/subdomains of a specified domain
* CA information for each discovered domain/subdomain
* email(s) found for each domain/subdomain dicovered in the crt.sh search
"""

# [=== Settings Example ===] #

"""
NOTE: Only the target and save_file information is needed, the other settings are not used by the tool

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

# [=== Final Output Example ===]

"""
<ascii title>
___________________/
Serikandor v1.0

[*] WARNING: These results may not be entirely accurate, it is up to you verify them. This is simply a tool.

[=== Discovered Domains ===]

    Domain Name         Domain IPv4     Status Code         CA     Cert Issued
------------------------------------------------------------------------------
[+] example0.com        <domain-ip>     status_code     <CA Name>    9/15/1995
[+] example1.com        <domain-ip>     status_code     <CA Name>    9/15/1995
[+] example2.com        <domain-ip>     status_code     <CA Name>    9/15/1995
------------------------------------------------------------------------------

[=== Discovered Emails ===]

------------------------------------------------------------------------------
[+] admin@example.com
[+] dev@example.com
[+] support@example.com
------------------------------------------------------------------------------
"""

# [=== Global Variables ===] #

# user-agent pool for HTTP(S) requests
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
]

# [=== Special Functions ===] #

def exit_program():
    print("\n")
    print(f"{Fore.MAGENTA}\n\nשיהיה לך יום שקט ולהתראות לעת עתה!{Fore.RESET}")
    exit()

# Clears the users terminal
def clear_terminal():
    if os.name == "posix":  # For Linux or MacOS
        os.system("clear")
    else:
        os.system("cls")  # For Windows

# [=== Functionality ===]

"""
validates the subdomains for each record, makes a new record for each subdomain with the IPv4 address and status code if the status code is not 
in the blacklist, then adds each new record to the cleaned_records (if there are any)
"""
def validate_and_clean_records(records: dict) -> dict:
    dirty_records = records
    blacklisted_status_codes = [
        404,  # Not Found
        410,  # Gone
        451,  # Unavailable For Legal Reasons
        503,  # Service Unavailable
    ]
    cleaned_records = []
    cache = {}

    resolver = dns.resolver.Resolver()
    resolver.nameservers = [
        "8.8.8.8", "8.8.4.4",         # Google
        "1.1.1.1", "1.0.0.1",         # Cloudflare
        "9.9.9.9", "149.112.112.112", # Quad9
    ]

    for index, record in enumerate(dirty_records, start=0):
        subdomains = dirty_records[index]["subdomains"]
        resolved_subdomains = []

        for subdomain in subdomains:
            try:
                answers = resolver.resolve(subdomain, "A")
                # this is a list of all the IPv4 address used for that domain
                ips = [answer.to_text() for answer in answers]
                # selects one IPv4 address from the list of ips to use to check for the domain status code
                """
                NOTE:
                    * The IPv4 address belongs to the reverse proxy or web server
                    * This is the most time efficient way to check the status code of each domain but it also means the status code may not be accurate
                """
                ip = ips[0]
                if ip in cache:
                    status_code = cache[ip]
                else:
                    # NOTE: user_agents is global
                    headers = {
                        'User-Agent': random.choice(user_agents),
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Host': subdomain
                    }
                    response = requests.get(f"http://{ip}", headers=headers, timeout=7)
                    status_code = response.status_code
                    if status_code not in blacklisted_status_codes:
                        # add the ip and status code to the cache
                        cache[ip] = status_code
                    else:
                        # moves to the next subdomain
                        continue
                
                # creates a new record using the status code, ip, subdomain, record CA name, and record issue data
                new_record = {
                    "subdomain": subdomain,
                    "status_code": status_code,
                    "emails": record["emails"],
                    "CA_name": record["CA_name"],
                    "cert_issue_date": record["cert_issue_date"],
                }
                # adds the new record to the cleaned_records list 
                cleaned_records.append(new_record)
                
            except KeyboardInterrupt:
                exit_program()
            except requests.exceptions.Timeout:
                continue
            except requests.exceptions.RequestException:
                continue
            except Exception as e:
                print(e)
        
        return cleaned_records

class Serikandor:
    def __init__(self, settings):
        # NOTE: save_file will be None or a string of a file path
        self.target = settings["target"]
        self.save_file = settings["save_file"]
        # placeholder for records
        self.records = {}

    def clean_url(self) -> str:
        # cleans the domain name (target) using a regex pattern
        pattern = r"https?://(?:www\.)?([^/]+)"
        match = re.search(pattern, self.target)
        
        if match:
            # extracts the domain
            full_domain = match.group(1)
            # split the domain to get the main part (last two segments)
            domain_parts = full_domain.split(".")
            if len(domain_parts) > 2:
                # returns the last two segments for subdomains
                return ".".join(domain_parts[-2:])
            else:
                # returns the domain if it's already in the correct format
                return full_domain
        else:
            print(f"{Fore.RED}[!] Error: Unknown.{Fore.RESET}")
            exit_program()
    
    def fetch_records(self) -> None:
        working_indicator = Halo(text="fetching subdomain information", spinner="bouncingBar")
        target_url = self.clean_url()

        working_indicator.start()

        api_url = f"https://crt.sh/?q=%25.{target_url}&output=json"
        headers = {'User-Agent': random.choice(user_agents)}

        try:
            response = requests.get(api_url, headers=headers, timeout=15)
        except KeyboardInterrupt:
            exit_program()
        except requests.Timeout:
            print(f"{Fore.RED}[!] Error: The initial request timed out, please check your internet connection and try again.{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error: Unknown{Fore.RESET}\n")
            print(e)
            exit_program()
