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
"""

# [=== Imports ===] #

import os
import random
import json
import re

from colorama import Fore  # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
from halo import Halo
import requests
from iteration_utilities import unique_everseen

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


    Domain Name            CA       Cert Issued
------------------------------------------------------------------------------
[+] example0.com        <CA Name>    9/15/1995
[+] example1.com        <CA Name>    9/15/1995
[+] example2.com        <CA Name>    9/15/1995
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

class Serikandor:
    def __init__(self, settings: dict):
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
    
    # returns list of records (each record is a dictionary)
    def fetch_records(self) -> list:
        working_indicator = Halo(text="fetching subdomains and emails", spinner="bouncingBar")
        target_url = self.clean_url()

        working_indicator.start()

        api_url = f"https://crt.sh/?q=%25.{target_url}&output=json"
        headers = {'User-Agent': random.choice(user_agents)}

        try:
            response = requests.get(api_url, headers=headers, timeout=30)
            if response.status_code == 200:
                self.records = response.json()
            else:
                print(f"\n{Fore.RED}[!] Error: The initial request failed with the status code: {Fore.YELLOW}{response.status_code}{Fore.RED}.{Fore.RESET}")
                exit_program()
        except KeyboardInterrupt:
            exit_program()
        except requests.Timeout:
            print(f"\n{Fore.RED}[!] Error: The initial request timed out, please check your internet connection and try again.{Fore.RESET}")
        except Exception as e:
            print(f"\n{Fore.RED}[!] Error: Unknown{Fore.RESET}\n")
            print(e)
            exit_program()

        self.process_records()
        self.clean_records()

        if self.save_file != None:
            with open(self.save_file, "w") as save_file:
                json.dump(self.records, save_file)

        working_indicator.stop()

        return self.records

    def process_records(self) -> list:
        records = self.records
        processed_records = []

        for record in records:
            common_name = record["common_name"]
            name_value = record["name_value"]
            dirty_issuer_name = record["issuer_name"]
            cert_issue_date = record["not_before"]

            subdomains = []
            emails = []

            for entry in [common_name, name_value]:
                data = entry.split("\n")
                for chunk in data:
                    chunk = chunk.strip()
                    if "@" in chunk:
                        emails.append(chunk)
                    else:
                        # this will remove any invalid subdomains (*.example.com)
                        if "*" in chunk:
                            continue
                        else:
                            subdomains.append(chunk)

            # [0] is the date, [1] is the time the certificate was issued
            cert_issue_date = cert_issue_date.split("T")[0]

            cleaned_issuer_name = re.search(r'(?<=CN=)[^,]*', dirty_issuer_name)
            if cleaned_issuer_name:
                cleaned_issuer_name = cleaned_issuer_name.group()
            else:
                cleaned_issuer_name = "Unknown"

            # creates a new record containing the wanted data found in the current record
            record = {
                "subdomains": subdomains,
                "emails": emails,
                "CA_name": cleaned_issuer_name,
                "cert_issue_date": cert_issue_date,
            }

            processed_records.append(record)

        self.records = processed_records

    def clean_records(self) -> None:
        dirty_records = self.records
        cleaned_records = []

        for index, record in enumerate(dirty_records, start=0):
            subdomains = dirty_records[index]["subdomains"]
            for subdomain in subdomains:
                try:      
                    # creates a new record with the current subdomain (this makes things a lot easier to work with for the output)
                    new_record = {
                        "subdomain": subdomain,
                        "emails": record["emails"],
                        "CA_name": record["CA_name"],
                        "cert_issue_date": record["cert_issue_date"],
                    }
                    # adds the new record to the cleaned_records list 
                    cleaned_records.append(new_record)
                except KeyboardInterrupt:
                    exit_program()
                except Exception as e:
                    print(f"\n{Fore.RED}[!] Error: Unknown{Fore.RESET}\n")
                    print(e)
                    exit_program()

        # removes duplicate record entries without changing the order of each records contents
        final_records = list(unique_everseen(cleaned_records))

        self.records = final_records

def run():
    # fetches the tool settings from the input file
    with open("../Soup/Lib/Data/Input_Data/input.json", "r") as settings_file:
        settings = json.load(settings_file)
    
    serikandor = Serikandor(settings=settings)
    # list of dictionaries which contain the data you must work with
    records = serikandor.fetch_records()

    """
    # output goal
    print(\"""
    <ascii title>
    ___________________/
    Serikandor v1.0
    
    [*] WARNING: These results may not be entirely accurate, it is up to you verify them. This is simply a tool.

    [=== Discovered Domains ===]
    \""")

    # Define fixed widths for the columns
    domain_width = 30  # Adjusted width for domain names
    ca_width = 50      # Width for CA names
    date_width = 15    # Width for certificate issue dates

    # Define the header
    header = f"{'Domain Name':<{domain_width}} {'CA':<{ca_width}} {'Cert Issued':<{date_width}}"
    separator_length = max(len(header), 80)  # Ensure separator is at least 80 characters
    separator = '-' * separator_length

    # Print the header and separator
    print(header)
    print(separator)

    # Set to collect unique emails
    unique_emails = set()

    # Print each record
    for record in records:
        domain = record.get('subdomain', '<Domain Not Found>')
        ca = record.get('CA_name', '<CA Name>')
        cert_issued = record.get('cert_issue_date', '<Date Not Found>')
        
        # Extract emails and add to the set
        emails = record.get('emails', [])
        unique_emails.update(emails)

        # Print the domain record
        print(f"[+] {domain:<{domain_width}} {ca:<{ca_width}} {cert_issued:<{date_width}}")

    # Print the final separator
    print(separator)

    # Print discovered emails
    print(\"""
    [=== Discovered Emails ===]
    ------------------------------------------------------------------------------
    \""")
    for email in unique_emails:
        print(f"[+] {email}")

    # Print the final separator for emails
    print("------------------------------------------------------------------------------")
    """