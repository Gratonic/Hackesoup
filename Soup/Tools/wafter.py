"""
[=== Author Information and Program Details ===]

File Name: patch_pirate.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.12.3
Dependencie(s):
Last Modified: October 26, 2025

[=== Description ===]

This tool is used to scan websites for WAF's and detect the WAF type.
"""

# [=== Imports ===] #

from colorama import Fore # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
from halo import Halo
import requests
import random
import json
import re

# [=== Global Variables ===] #

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
]

# [=== Functionality ===] #

def exit_program() -> None:
    print(f"{Fore.MAGENTA}\n\nCuídese!{Fore.RESET}")
    exit()

# post_webpage = ""
# post_headers = ""
# 
# put_webpage = ""
# put_headers = ""
# 
# get_webpage = ""
# get_headers = ""

def detect_waf(target: str):
    with open("../Soup/DB/Wafter/waf_signatures.json", "r") as file:
        waf_signatures = json.load(file)

    # makes 3 requests with different methods because some firewalls may be triggered by one method but not the other
    try:
        post_response = requests.post(
            url=target, 
            headers={
                "User-Agent": random.choice(user_agents), 
                "Accept": "text/html"
            },
            timeout=5,
            allow_redirects=True
        )

        put_response = requests.put(
            url=target, 
            headers={
                "User-Agent": random.choice(user_agents), 
                "Accept": "text/html"
            },
            timeout=5,
            allow_redirects=True
        )

        get_response = requests.get(
            url=target, 
            headers={
                "User-Agent": random.choice(user_agents), 
                "Accept": "text/html"
            },
            timeout=5,
            allow_redirects=True
        )
    except requests.Timeout:
        print(f"\n{Fore.RED}[!] Error: The WAF detection request timed out.{Fore.RESET}")
        exit_program()
    except requests.ConnectionError:
        print(f"\n{Fore.RED}[!] Error: Failed to connect to the target.{Fore.RESET}")
        exit_program()
    except KeyboardInterrupt:
        exit_program()
    except Exception as e:
        print(f"\n{e}")
        exit_program()
    
    # The status codes and webpage contents are used to detect the WAF and WAF type.
    post_webpage = str(post_response.text)
    post_headers = str(post_response.headers)

    put_webpage = str(put_response.text)
    put_headers = str(put_response.headers)

    get_webpage = str(get_response.text)
    get_headers = str(get_response.headers)

    # [0] stores the confidence score, [1] stores the waf_name
    best_match = [0, None]

    # compares the POST data with the signature data to detect the WAF
    if post_response.status_code >= 400:
        for waf_name, waf_signature in waf_signatures.items():
            confidence_score = 0

            page_signature = waf_signature["page_content"]
            headers_signature = waf_signature["headers"]

            if page_signature and re.search(pattern=page_signature, string=post_webpage, flags=re.IGNORECASE):
                confidence_score += 1
            if headers_signature and re.search(pattern=headers_signature, string=post_headers, flags=re.IGNORECASE):
                confidence_score += 1

            if confidence_score > best_match[0]:
                best_match[0] = confidence_score
                best_match[1] = waf_name

    # a better match can not be found, so the waf_name is returned
    if best_match[0] == 2:
        return best_match[1]
    
    # compares the PUT data with the signature data to detect the WAF
    if put_response.status_code >= 400:
        for waf_name, waf_signature in waf_signatures.items():
            confidence_score = 0

            page_signature = waf_signature["page_content"]
            headers_signature = waf_signature["headers"]

            if page_signature and re.search(pattern=page_signature, string=put_webpage, flags=re.IGNORECASE):
                confidence_score += 1
            if headers_signature and re.search(pattern=headers_signature, string=put_headers, flags=re.IGNORECASE):
                confidence_score += 1

            if confidence_score > best_match[0]:
                best_match[0] = confidence_score
                best_match[1] = waf_name

    # a better match can not be found, so the waf_name is returned
    if best_match[0] == 2:
        return best_match[1]

    # compares the GET data with the signature data to detect the WAF
    if get_response.status_code >= 400 | get_response.status_code == 200:
        for waf_name, waf_signature in waf_signatures.items():
            confidence_score = 0

            page_signature = waf_signature["page_content"]
            headers_signature = waf_signature["headers"]

            if page_signature and re.search(pattern=page_signature, string=get_webpage, flags=re.IGNORECASE):
                confidence_score += 1
            if headers_signature and re.search(pattern=headers_signature, string=get_headers, flags=re.IGNORECASE):
                confidence_score += 1

            if confidence_score > best_match[0]:
                best_match[0] = confidence_score
                best_match[1] = waf_name
    
    # returns the WAF Type or None if no match was found
    return best_match[1]

def run(settings: dict):
    # http is used because some websites may not have support for https and if it is, the connection is usually updated to https
    target = settings["target"]

    loading_bar = Halo(text=f"scanning {Fore.YELLOW}{target}{Fore.RESET}", spinner="bouncingBar", color="yellow")

    target = f"http://{settings["target"]}"

    ascii_title = r"""
     _    _        __ _            
    | |  | |      / _| |           
    | |  | | __ _| |_| |_ ___ _ __ 
    | |/\| |/ _` |  _| __/ _ \ '__|
    \  /\  / (_| | | | ||  __/ |   
     \/  \/ \__,_|_|  \__\___|_|   """
    title_colors = [
        Fore.BLUE, Fore.RED, Fore.WHITE, Fore.YELLOW, 
        Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX
    ]
    banner = "".join(title_colors[char % len(title_colors)] + ascii_title[char] for char in range(len(ascii_title)))
    banner_bar = "___________________________________/"
    small_title = "wafter"
    tool_version = "1.0"

    print(f"{banner}\n{banner_bar}\n{Fore.LIGHTCYAN_EX}{small_title} {tool_version}{Fore.RESET}\n")
    
    loading_bar.start()

    waf = detect_waf(target=target)

    loading_bar.stop()

    if waf != None:
        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} The site {Fore.YELLOW}{target}{Fore.RESET} is behind {Fore.MAGENTA}{waf}{Fore.RESET}")
        print(f"{Fore.BLUE}[*]{Fore.RESET} Number of requests: 3")
    else:
        print(f"{Fore.RED}[-]{Fore.RESET} No WAF was detected")

    if waf != None:
        return waf
    else:
        return "No WAF detected."