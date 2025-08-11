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

# [=== Global Variables ===] #

# creates the header for the tool output (also used when the loading bar starts)
title = r"""
 _____           _ _                   _            
/  ___|         (_) |                 | |           
\ `--.  ___ _ __ _| | ____ _ _ __   __| | ___  _ __ 
 `--. \/ _ \ '__| | |/ / _` | '_ \ / _` |/ _ \| '__|
/\__/ /  __/ |  | |   < (_| | | | | (_| | (_) | |   
\____/ \___|_|  |_|_|\_\__,_|_| |_|\__,_|\___/|_|   """
title_colors = [Fore.BLUE, Fore.WHITE]
colorful_title = ''.join(title_colors[char % len(title_colors)] + title[char] for char in range(len(title)))
title_bar = f"{Fore.YELLOW}__________________________________________________________/"
tool_version_info = f"{Fore.CYAN}Serikandor v1.0{Fore.RESET}"
header = f"{colorful_title}\n{title_bar}\n{tool_version_info}\n"

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
        self.target = settings["target"]
        # False if the user chose not to save the tool output, else it is a file path
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

        print(header)
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

        working_indicator.stop()
        clear_terminal()

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

def run() -> list:
    # fetches the tool settings from the input file
    with open("../Soup/Lib/Data/Input_Data/input.json", "r") as settings_file:
        settings = json.load(settings_file)
    
    serikandor = Serikandor(settings=settings)
    # list of dictionaries which contain the data you must work with
    records = serikandor.fetch_records()

    warning_message = f"{Fore.RED}[*] WARNING: These results may not be entirely accurate, it is up to you verify them. This is simply a tool.\n{Fore.RESET}"

    # used to keep things organized
    divider_line = f"{Fore.LIGHTBLACK_EX}-------------------------------------------------------------------------------------------------------------------------{Fore.RESET}"

    # determines the len of each item (except the emails) in each record and how many spaces should be added for neat output
    # NOTE: certain entries will be removed if the length of one of their items exceeds the following limits, this keeps the output neat
    max_domain_name_len = 50
    max_CA_name_len = 50

    # used to collect all of the emails from the records
    emails = set()

    # removes duplicate entries
    unique_records = []

    for index, record in enumerate(records, start=0):
        if record not in unique_records:
            unique_records.append(records)
        else:
            records.pop(index)

    for index, record in enumerate(records, start=0):
        # gets the length of the necessary items in the record
        domain_len = len(record["subdomain"])
        CA_name_len = len(record["CA_name"])

        # determines and adds the spaces that need to be added to each item in the record
        records[index]["subdomain"] = f"{record["subdomain"]}{" " * ((max_domain_name_len - domain_len) + 3)}"
        records[index]["CA_name"] = f"{record["CA_name"]}{" " * ((max_CA_name_len - CA_name_len) + 3)}"
        # just adding the color to this item in the list
        records[index]["cert_issue_date"] = f"{record["cert_issue_date"]}"
        
        # collects all the emails from the current record (if any) and adds them to the emails list
        for email in record["emails"]:
            emails.add(email)

    # the actual displaying
    print(header)
    print(warning_message)
    print(f"{Fore.BLUE}[=== Discovered Subdomains ===]\n{Fore.RESET}")
    print(f"{Fore.WHITE}Domain Name{" " * 46}CA Name{" " * 30}Issue Date{Fore.RESET}")
    print(divider_line)
    # very rarely no subdomains are found
    if records != list():
        for record in records:
            print(f"{Fore.GREEN}[+] {Fore.MAGENTA}{record["subdomain"]}{Fore.CYAN}{record["CA_name"]}{Fore.YELLOW}{record["cert_issue_date"]}{Fore.RESET}")
    else:
        print(f"{Fore.RED}[-] {Fore.MAGENTA}no subdomains were found{Fore.RESET}")
    print(divider_line)
    print("\n")
    print(f"{Fore.BLUE}[=== Discovered Emails ===]{Fore.RESET}")
    print("\n")
    print(divider_line)
    # sometimes the emails list is empty
    if emails != set():
        for email in emails:
            print(f"{Fore.GREEN}[+] {Fore.CYAN}{email}{Fore.RESET}")
    else:
        print(f"{Fore.RED}[-] {Fore.CYAN}no emails were found{Fore.RESET}")
    print(divider_line)

    # returns the tool output without whitespace (will be saved in a file using code in hsmi.py if the user chose to save the tool output)
    records_without_whitespace = [
        {key: value.strip() if isinstance(value, str) else value for key, value in record.items()} for record in records
    ]
    return records_without_whitespace