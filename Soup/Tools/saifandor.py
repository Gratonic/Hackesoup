# [=== Imports ===] #
from colorama import Fore
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

    Domain Name         Domain IPv4     Status Code       CA        CA Issued
-----------------------------------------------------------------------------
[+] example0.com        <domain-ip>     status_code     <CA Name>   9/15/1995
-----------------------------------------------------------------------------
[+] example1.com        <domain-ip>     status_code     <CA Name>   9/15/1995
-----------------------------------------------------------------------------
[+] example2.com        <domain-ip>     status_code     <CA Name>   9/15/1995
-----------------------------------------------------------------------------

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

# target placeholder
target = None

# user-agent pool for HTTP(S) requests
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15"
]

# [=== Functionality ===] #

# fetches the target and save_file info
with open("../Soup/Lib/Data/Input_Data/input.json", "r") as settings_file:
    settings = json.load(settings_file)
    target = settings["target"]
    if settings["save_file"] == None:
        save_file = False
    else:
        # gets the save file path
        save_file = settings["save_file"]
