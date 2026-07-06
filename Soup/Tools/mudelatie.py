"""
[=== Author Information and Program Details ===]

File Name: mudelatie.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.12.3
Dependencie(s): halo, piratescanner, colorama, json, os
Last Modified: April 26th, 2025

[=== Description ===]

This is an XSS Vulnerability Scanner. It can test for Reflected and Stored XSS (excluding DOM XSS).
"""

# [=== Imports ===] #

from colorama import Fore # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
from halo import Halo
import importlib
import requests
import random
import sys
import os

python_modules_path = os.path.join(os.path.dirname(__file__), "..", "Soup", "Lib", "Python_Modules")
sys.path.append(python_modules_path)

crawler = importlib.import_module("crawler")

utils = importlib.import_module("utils")

def exit_program() -> None:
    utils.exit_program(tool_name="mudelatie")

# [=== Functionality ===] #

def load_payloads() -> list:
    payloads = utils.load_payloads(filename="../Soup/DB/Mudelatie/payloads.txt")
    
    return payloads

def check_for_stored_xss(target: str, payload: str) -> bool:
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
    ]
    try:
        response = requests.get(
            url=target,
            headers={
                "User-Agent": random.choice(user_agents), 
                "Accept": "text/html"
            },
            timeout=7
        )
    except requests.Timeout:
        print(f"\n{Fore.RED}[!] Error: The request to {Fore.YELLOW}{target}{Fore.RED} timed out while checking for SXSS{Fore.RESET}\n")
        exit_program()
    except requests.ConnectionError:
        print(f"\n{Fore.RED}[!] Error: Failed to connect to {Fore.YELLOW}{target}{Fore.RED} failed while attempting to check for SXSS.{Fore.RESET}\n")
        exit_program()
    except KeyboardInterrupt:
        exit_program()
    except Exception as e:
        print(f"\n{e}\n")
        exit_program()

    return payload in response.text

def scan_for_xss(settings: dict) -> list:
    target = f"http://{settings["target"]}"
    payloads = load_payloads()
    forms = crawler.get_all_forms(target=target, tool_name="mudelatie")
    successful_rxss_payloads = []
    successful_sxss_payloads = []

    loading_bar = Halo(text=f"Scanning for XSS. This may take a while...", spinner="bouncingBar", color="red")
    loading_bar.start()

    for form in forms:
        for payload in payloads:
            reflected_xss = False
            stored_xss = False

            form_details = crawler.get_form_details(form=form)

            response = crawler.submit_form(target=target, form_details=form_details, payload=payload, tool_name="mudelatie")

            # checks for Reflected Cross-Site Scripting (RXSS)
            webpage = response[0].text
            if payload in webpage:
                reflected_xss = True

            # checks for Stored Cross-Site Scripting (SXSS)
            stored_xss = check_for_stored_xss(target=target, payload=payload)

            if reflected_xss and stored_xss:
                loading_bar.stop()
                print(f"{Fore.GREEN}[+] {Fore.RESET}Reflected XSS Found: {Fore.LIGHTCYAN_EX}{response[1]}{Fore.RESET}")
                print(f"{Fore.YELLOW}[+] {Fore.RESET}Stored XSS Found: {Fore.LIGHTCYAN_EX}{response[1]}{Fore.RESET}")
                loading_bar.start()

                successful_rxss_payloads.append(response[1])
                successful_sxss_payloads.append(response[1])
            elif stored_xss:
                loading_bar.stop()
                print(f"{Fore.YELLOW}[+] {Fore.RESET}Stored XSS Found: {Fore.LIGHTCYAN_EX}{response[1]}{Fore.RESET}")
                loading_bar.start()

                successful_sxss_payloads.append(response[1])
            elif reflected_xss:
                loading_bar.stop()
                print(f"{Fore.GREEN}[+] {Fore.RESET}Reflected XSS Found: {Fore.LIGHTCYAN_EX}{response[1]}{Fore.RESET}")
                loading_bar.start()

                successful_rxss_payloads.append(response[1])
            else:
                continue
            
            loading_bar.stop()

        return [successful_rxss_payloads, successful_sxss_payloads]

def run(settings: dict) -> dict:
    ascii_title = r"""
    ___  ___          _      _       _   _      
    |  \/  |         | |    | |     | | (_)     
    | .  . |_   _  __| | ___| | __ _| |_ _  ___ 
    | |\/| | | | |/ _` |/ _ \ |/ _` | __| |/ _ \
    | |  | | |_| | (_| |  __/ | (_| | |_| |  __/
    \_|  |_/\__,_|\__,_|\___|_|\__,_|\__|_|\___|"""
    title_colors = [
        Fore.RED, Fore.WHITE, 
        Fore.BLUE, Fore.GREEN
    ]
    banner = "".join(title_colors[char % len(title_colors)] + ascii_title[char] for char in range(len(ascii_title)))
    banner_bar = "_______________________________________________________________/"
    small_title = "mudelatie"
    tool_version = "1.0"

    print(f"{banner}\n{banner_bar}\n{Fore.LIGHTCYAN_EX}{small_title} {tool_version}{Fore.RESET}\n")

    xss_vulns = scan_for_xss(settings=settings)
    rxss_vulns = xss_vulns[0]
    sxss_vulns = xss_vulns[1]
    
    divider_bar = f"{Fore.LIGHTBLACK_EX}----------------------------------------------------------------{Fore.RESET}"

    utils.clear_terminal()

    print(f"{banner}\n{banner_bar}\n{Fore.LIGHTCYAN_EX}{small_title} {tool_version}{Fore.RESET}\n")

    print(divider_bar)

    if len(rxss_vulns) >= 1:
        print(f"\n{Fore.GREEN}Reflected Cross-Site Scripting (RXSS) Vulnerabilities{Fore.RESET}\n")
        for payload in rxss_vulns:
            print(f"{Fore.GREEN}[+] {Fore.LIGHTCYAN_EX}{payload}{Fore.RESET}")
        print("\n")
    else:
        print(f"\n{Fore.GREEN}Reflected Cross-Site Scripting (RXSS) Vulnerabilities{Fore.RESET}\n")
        print(f"{Fore.RED}[-] {Fore.LIGHTCYAN_EX}No RXSS Vulnerabilites Found{Fore.RESET}")
    
    print(divider_bar)

    if len(sxss_vulns) >= 1:
        print(f"\n{Fore.YELLOW}Stored Cross-Site Scripting (RXSS) Vulnerabilities{Fore.RESET}\n")
        for payload in sxss_vulns:
            print(f"{Fore.YELLOW}[+] {Fore.LIGHTCYAN_EX}{payload}{Fore.RESET}")
        print("\n")
    else:
        print(f"\n{Fore.YELLOW}Reflected Cross-Site Scripting (RXSS) Vulnerabilities{Fore.RESET}\n")
        print(f"{Fore.RED}[-] {Fore.LIGHTCYAN_EX}No SXSS Vulnerabilites Found{Fore.RESET}")
    
    print(f"\n{divider_bar}")

    return {"RXSS": rxss_vulns, "SXSS": sxss_vulns}