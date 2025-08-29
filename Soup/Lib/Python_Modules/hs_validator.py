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

import tldextract # # Copyright (c) 2025, John Kurkowski, All Rights Reserved
import colorama # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
import requests
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

# Says "Goodbye!" to the user in German and exits the program
def exit_program() -> None:
    print(f"{magenta}\n\nTschüss!{reset}")
    exit()

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

def check_web_target(url: str) -> int:
    # extracts the components of the domain name
    extracted = tldextract.extract(url=url)

    # checks if the domain name is valid
    if not extracted.domain or not extracted.suffix:
        return [1, "N/A"]
    
    # constructs the root domain with the extracted components
    root_domain = f"{extracted.domain}.{extracted.suffix}"

    # checks if the root domain is valid
    try:
        response = requests.get(url=f"https://{root_domain}", timeout=30)
        if response.status_code == 200:
            return [0, root_domain]
    except requests.ConnectionError:
        print(f"{red}[!] Error: The connection attempt for the initial request to validate the domain name failed.{reset}")
        exit_program()
    except requests.Timeout:
        print(f"{red}[!] Error: The initial request made to validate the domain name timed out.{reset}")
        exit_program()
    except Exception as e:
        print(f"{red}[!] Error: Unknown.{reset}\n{e}")
        exit_program()

def combo_target(target: "str") -> int:
    # Gets the target type
    while True:
        try:
            target_type = int(input(f"{magenta}Is Your Target Address A Website or IP Address? {green}[Enter 1: For A Website, Enter 2: For An IPv4 Address]: {reset}"))
            if target_type == 1 or target_type == 2:
                break
            else:
                print(f"{red}[!] Error: Invalid Target Type{reset}")
        except KeyboardInterrupt:
            exit_program()
        except:
            print(f"{red}[!] Error: Invalid Target Type{reset}")
    try:
        if target_type == 1:
            status_code = check_web_target(target)
            return status_code
        elif target_type == 2:
            status_code = check_IPv4_target(target)
            return status_code
    except:
        print(f"{red}[!] Error: Unknown{reset}")

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

# Returns a list, the list will have 2 elements
# NOTE: The first element is the status code
def check_timeout(timeout: int) -> list:
    if timeout >= 1 and timeout <= 5:
        return [0, timeout]
    else:
        try:
            print(f"{red}[!] Warning: Timeout Is To Low or To High, Setting It To {yellow}2{reset}")
            # Without this pause the next menu will be displayed before the user can see the above message because -->
            # the terminal will be cleared for the next UX menu
            time.sleep(3)
            timeout = 2
            return [1, timeout]
        except KeyboardInterrupt:
            exit_program()

def check_thread_amount(requested_thread_amount: int) -> list:
    logical_cores = os.cpu_count()
    safe_thread_amount = logical_cores // 4
    if safe_thread_amount > 1 and requested_thread_amount <= safe_thread_amount:
        return [0, requested_thread_amount]
    else:
        try:
            print(f"{red}[!] Warning: Your Thread Amount Exceeds Your CPU's Safe Thread Amount, Defaulting To {yellow}1{reset}")
            # Without this pause the next menu will be displayed before the user can see the above message because -->
            # the terminal will be cleared for the next UX menu
            time.sleep(3)
            new_thread_amount = 1
            return [1, new_thread_amount]
        except KeyboardInterrupt:
            exit_program()

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