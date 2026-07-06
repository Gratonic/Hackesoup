"""
# :: Author Information and Program Details :: #

File Name: hs_validator.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.10.12
Dependencie(s): colorama
Last Modified: February 8th, 2025

# :: Description :: #

This python file contains the functions used to validate the input given by the user in the UX menu interface. This code
is imported and used in the hs_prompts.py file.

# :: Important :: #

0: All-Good Status Code
1: Error Status Code
"""

# :: Imports :: #

import tldextract # Copyright (c) 2025, John Kurkowski, All Rights Reserved
import colorama # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
import requests
import random
import utils
import time
import os
import re

# :: Global Variables :: #

# Colors
reset = colorama.Fore.RESET
blue = colorama.Fore.BLUE
light_blue = colorama.Fore.LIGHTBLUE_EX
cyan = colorama.Fore.CYAN
light_cyan = colorama.Fore.LIGHTCYAN_EX
red = colorama.Fore.RED
light_red = colorama.Fore.LIGHTRED_EX
green = colorama.Fore.GREEN
light_green = colorama.Fore.LIGHTGREEN_EX
yellow = colorama.Fore.YELLOW
light_yellow = colorama.Fore.LIGHTYELLOW_EX
magenta = colorama.Fore.MAGENTA
light_magenta = colorama.Fore.LIGHTMAGENTA_EX
white = colorama.Fore.WHITE
gray = colorama.Fore.LIGHTBLACK_EX

# :: Functionality :: #

def exit_program() -> None:
    utils.exit_program(tool_name="hackesoup")

def check_user_choice(choice: int, first: int, last: int) -> int:
    try:
        if choice >= first and choice <= last:
            return 0
        elif choice < first:
            print(f"{red}[!] Error: Invalid Option{reset}")
            return 1
        elif choice > last:
            print(f"{red}[!] Error: Invalid Option{reset}")
            return 1

    except ValueError:
        print(f"{red}[!] Error: Invalid Option{reset}")
        exit()

def check_int(integer: str) -> int:
    try:
        integer = int(integer)
        return 0
    except ValueError:
        print(f"{red}[!] Error: Invalid Input{reset}")
        return 1

def check_str(string) -> int:
    try:
        string = str(string)
        return 0
    except ValueError:
        print(f"{red}[!] Error: Invalid Input{reset}")
        return 1

# Used to check each octet in an IPv4 address
# NOTE: this was made because there was an issue using a for loop in the check_IPv4_target
def check_octets(octs: list) -> int:
    for octet in octs:
        if int(octet) > 0 and int(octet) < 255:
            pass
        else:
            return 1
    return 0

def check_IPv4_target(IPv4_addr: str) -> int:
    octets = IPv4_addr.split(".")
    keep_going = True
    # There should not be more than 4 octets
    if len(octets) == 4:
        pass
    else:
        print(f"{red}[!] Erorr: Invalid IPv4 Address{reset}")
        keep_going = False
    
    # Validates every octet in the IP Address
    if keep_going != False:
        octet_check_status_code = check_octets(octets)
        if octet_check_status_code == 0:
            return 0
        else:
            print(f"{red}[!] Error: One or More Octets Are Invalid, Please Check Your Ip Address{reset}")
            return 1
    else:
        return 1

def check_web_target(url: str) -> list:
    # extracts the components of the domain name
    extracted = tldextract.extract(url=url)

    # checks if the domain name is valid
    if not extracted.domain or not extracted.suffix:
        return [1, "N/A"]
    
    # constructs the root domain with the extracted components
    if extracted.subdomain:
        domain_name = f"{extracted.subdomain}.{extracted.domain}.{extracted.suffix}"
    else:
        domain_name =  f"{extracted.domain}.{extracted.suffix}"

    # checks if the root domain is valid
    try:
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
        ]

        response = requests.get(
            url=f"http://{domain_name}",
            headers={
                "User-Agent": random.choice(user_agents), 
                "Accept": "text/html"
            },
            timeout=5
        )
        if response.status_code == 200:
            return [0, domain_name]
    except requests.ConnectionError:
        print(f"{red}[!] Error: The connection attempt for the initial request to validate the domain name failed.{reset}")
        exit_program()
    except requests.Timeout:
        print(f"{red}[!] Error: The initial request made to validate the domain name timed out.{reset}")
        exit_program()
    except KeyboardInterrupt:
        exit_program()
    except Exception as e:
        print(f"\n{red}[!] Error: Unknown.{reset}\n{e}")
        exit_program()

def check_web_target_with_params_or_endpoints(url: str) -> list:
    # extracts the components of the domain name
    extracted = tldextract.extract(url=url)

    # checks if the domain name is valid
    if not extracted.domain or not extracted.suffix:
        return [False, "N/A"]
    
    # removes the http/https from the target URL if it exists in it
    # NOTE: the requets module requires either http or https but I don't know if the user provided it, therefore...
    if url.startswith("https://"):
        url_parts = url.split("https://")
        url = url_parts[1]
    if url.startswith("http://"):
        url_parts = url.split("http://")
        url =  url_parts[1]

    try:
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
        ]

        response = requests.get(
            url=f"http://{url}",
            headers={
                "User-Agent": random.choice(user_agents), 
                "Accept": "text/html"
            },
            timeout=5
        )

        if response.status_code == 200:
            return [True, url]
        else:
            return [False, "NA"]
    except requests.ConnectionError:
        print(f"{red}[!] Error: The connection attempt for the initial request to validate the domain name failed.{reset}")
        exit_program()
    except requests.Timeout:
        print(f"{red}[!] Error: The initial request made to validate the domain name timed out.{reset}")
        exit_program()
    except KeyboardInterrupt:
        exit_program()
    except Exception as e:
        print(f"\n{red}[!] Error: Unknown.{reset}\n{e}")
        exit_program()

def check_port(port: str) -> int:
    try:
        port = int(port)
        if port > 0 and port <= 65535:
            return 0
        else:
            print(f"{red}[!] Erorr: Invalid Port{reset}")
            return 1
    except ValueError:
        print(f"{red}[!] Error: Invalid Port{reset}")
        return 1

def check_port_range(port_range: str) -> int:
    try:
        ports = port_range.split("-")
        start_port = int(ports[0])
        end_port = int(ports[1])
        if start_port > 0 and start_port <= 65535 and end_port > 0 and end_port <= 65535:
            return 0
        else:
            print(f"{red}[!] Error: Invalid Port Range{reset}")
            return 1
    except:
        print(f"{red}[!] Error: Invalid Port Range{reset}")
        return 1

# Returns a list, the list will have 2 elements in the case of an error and one in the case of a valid file path
# NOTE: The first position is the status code
# NOTE: This function does not work at the moment and the payload file options are currently unavailable
def check_file_path(file_path: str) -> list:
    # Regex pattern for a valid file path on Linux and MacOS
    pattern = r"^(\/(?:[^\/\0]+(?:\/[^\/\0]+)*)?|(?:[^\/\0]+(?:\/[^\/\0]+)*))?$"
    # Checks if the path matches the Linux and MacOS file path pattern and also checks if the file has an extension
    if re.match(pattern, file_path) and re.search(r'\.[^\/\.]+$', file_path):
        return [0, file_path]
    else:
        while True:
            print(f"{red}[!] Error: Invalid File Path, A Valid File Path Would Be {yellow}'/home/users/username/example_file.txt'{reset}")
            try:
                new_file_path = input(f"{magenta}Please Enter A Valid File Path: {reset}")
                if re.match(pattern, new_file_path) and re.search(r'\.[^\/\.]+$', new_file_path):
                    return [1, new_file_path]
            except KeyboardInterrupt:
                exit_program()