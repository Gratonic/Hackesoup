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

import colorama
import requests
import psutil # Written and Licensed by Giampaolo Rodola, https://github.com/giampaolo/psutil
import os

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

def check_int(integer: int) -> int:
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

def check_IPv4_target(IPv4_addr: str) -> str:
    octets = IPv4_addr.split(".")
    # There should not be more than 4 octets
    if len(octets) == 4:
        pass
    else:
        print(f"{red}[!] Erorr: Invalid IPv4 Address{reset}")
        return 1
    # Validates each octet
    for octet in octets:
        try:
            octet = int(octet)
            # The IPv4 Address should not be a network or broadcast address and all octets should be within the range of 1-254
            if octet < 255 and octet > 0:
                return 0
            else:
                print(f"{red}[!] Erorr: Invalid IPv4 Address{reset}")
                return 1
        except ValueError:
            print(f"{red}[!] Erorr: Invalid IPv4 Address{reset}")
            return 1

# NOTE: URL must be in this format: https://example.com or http://example.com
def check_web_target(url: str) -> int:
    try:
        response = requests.head(url, allow_redirects=True)
        # Checks if the response status code is in the range of 200-399
        if response.status_code >= 200 and response.status_code < 400:
            return 0
        else:
            print(f"{red}[!] Error: Invalid Website {yellow}[Ex: https://example.com or http://example.com]{reset}")
            return 1
    except:
        print(f"{red}[!] Error: Invalid Website {yellow}[Ex: https://example.com or http://example.com]{reset}")
        return 1

def combo_target(target: "str"):
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


def check_thread_amount(thead_amount: int) -> int:
    # Determines the safe thread amount and checks it against the provided thread amount
    thread_count = psutil.cpu_count(logical=True)
    safe_thread_amount = round(int(thread_count // 2))
    if thead_amount > safe_thread_amount:
        print(f"{red}[!] Error: Too many threads, you may only use up to {yellow}{safe_thread_amount}{reset}")
        return 1
    else:
        return 0

def check_port(port: int) -> int:
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

# Returns an amount of seconds to timeout for
def timeout(timeout_amount: int) -> int:
    if timeout < 0 and timeout > 1000:
        return timeout
    else:
        print(f"{red}[!] Warning: Timeout Amount Is Crazy High, Reducing It To {yellow}1000{reset}")
        timeout = 1000
        return timeout

def file_path(file_path: str) -> int:
    # Check if the file path exists
    if not os.path.exists(file_path):
        print(f"{red}[!] Error: The path '{file_path}' does not exist{reset}")
        return 1
    # Check if the path is a file
    if not os.path.isfile(file_path):
        print(f"{red}[!] Error: The path '{file_path}' is not a file{reset}")
        return 1
    # If everything went well
    return 0