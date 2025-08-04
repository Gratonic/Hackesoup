# [=== Program Metadata ===] #

"""
# :: Author Information and Program Details :: #

File Name: serikandor.py
Author(s): ibrahim-sisar (https://github.com/ibrahim-sisar) and Gratonic (https://github.com/Gratonic)
Written In: Python 3.13.5
Dependencie(s): colorama, halo, asyncio, random, httpx, json, re, os
Last Modified: 7/6/2025

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

    Domain              Domain IPv4        Email
-----------------------------------------------------------------------------
[+] example0.com        <domain-ip>     admin@example.com
[+] example1.com        <domain-ip>     devteam@example.com
[+] example2.com        <domain-ip>     support@example.com
-----------------------------------------------------------------------------

"""

# [=== Global Variables ===] #

# user-agent pool for HTTP(S) requests
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
]

# used to check for status codes that indicate the domain in no longer valid
blacklisted_status_codes = [
    404,  # Not Found
    410,  # Gone
    451,  # Unavailable For Legal Reasons
    521,  # Web Server Is Down
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

def resolve_domains(records: dict):
    dirty_records = records
    cleaned_records = {}
    # used to cache known IP's with their status codes
    cache = {}
    resolver = dns.resolver.Resolver()

class Resolver():
    def __init__(self, records: dict):
        self.records = records
        self.cache = {}

    def resolve_domains(self) -> dict:
        records = self.records

        resolver = dns.resolver.Resolver()
        resolver.nameservers = [
            "8.8.8.8", "8.8.4.4",         # Google
            "1.1.1.1", "1.0.0.1",         # Cloudflare
            "9.9.9.9", "149.112.112.112"  # Quad9
        ]




    # dumps the current cache of ip addresses 
    def dump_cache(self) -> dict:
        return self.cache
