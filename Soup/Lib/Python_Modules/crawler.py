"""
[=== Author Information and Program Details ===]

File Name: crawler.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.12.3
Dependencie(s): bs4, urllib3, colorama, requests, random
Last Modified: October 27, 2025

[=== Description ===]

This module is used to retrive data from a website and analyze it. It is also able to submit forms with provided values (ex: payloads).
"""

# [=== Imports ===] #

from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from colorama import Fore # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
import requests
import random
import utils

# [=== Global Variables ===] #

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
]

def exit_program(tool_name: str) -> None:
    utils.exit_program(tool_name=tool_name)

def get_all_forms(target: str, tool_name: str) -> list:
    try:
        webpage = requests.get(
            url=target,
            headers={
                "User-Agent": random.choice(user_agents), 
                "Accept": "text/html"
            },
            timeout=7
        ).text

        soup = bs(webpage, "html.parser")

        return soup.find_all("form")
    except requests.Timeout:
        print(f"\n{Fore.RED}[!] Error: The request to {Fore.YELLOW}{target}{Fore.RED} timed out, while attempting to retrieve its form fields.{Fore.RESET}")
        exit_program(tool_name=tool_name)
    except requests.ConnectionError:
        print(f"\n{Fore.RED}[!] Error: Failed to connect to {Fore.YELLOW}{target}{Fore.RED} failed, while attempting to retrieve its form fields.{Fore.RESET}")
        exit_program(tool_name=tool_name)
    except KeyboardInterrupt:
        exit_program(tool_name=tool_name)
    except Exception as e:
        print(f"\n{e}\n")
        exit_program(tool_name=tool_name)

def get_form_details(form: dict) -> dict:
    form_details = {}

    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()

    input_elements = []
    for input_element in form.find_all("input"):
        input_type = input_element.attrs.get("type", "text")
        input_name = input_element.attrs.get("name")
        input_elements.append({"type": input_type, "name": input_name})
    
    form_details["action"] = action
    form_details["method"] = method
    
    form_details["input_elements"] = input_elements

    return form_details

def submit_form(target: str, form_details: dict, payload: str, tool_name: str) -> requests.Response:
    # constructs the absolute form action URL
    target_url = urljoin(target, form_details["action"])
    # gets the form input data (type, name, method, etc.)
    inputs = form_details["input_elements"]

    # forms the target url using the payload and input data
    if "?" in target:
        for input in inputs:
            if input["name"] != None:
                target_url += f"&{input["name"]}={payload}"
    else:
        for input in inputs:
            if input == inputs[0] and input["name"] != None:
                target_url += f"?{input["name"]}={payload}"
            else:
                if input["name"] != None:
                    target_url += f"&{input["name"]}={payload}"
    
    try:
        if form_details["method"] == "post":
            response = requests.post(
                url=f"{target_url}", 
                headers={
                    "User-Agent": random.choice(user_agents), 
                    "Accept": "text/html"
                },
                timeout=7
            )
        else:
            response = requests.get(
                url=f"{target_url}",
                headers={
                    "User-Agent": random.choice(user_agents), 
                    "Accept": "text/html"
                },
                timeout=7
            )

        return [response, target_url]
    except requests.Timeout:
        print(f"\n{Fore.RED}[!] Error: The request to {Fore.YELLOW}{target_url}{Fore.RED} timed out.{Fore.RESET}\n")
        exit_program(tool_name=tool_name)
    except requests.ConnectionError:
        print(f"\n{Fore.RED}[!] Error: Failed to connect to {Fore.YELLOW}{target_url}{Fore.RED} failed.{Fore.RESET}\n")
        exit_program(tool_name=tool_name)
    except KeyboardInterrupt:
        exit_program(tool_name=tool_name)
    except Exception as e:
        print(f"\n{e}\n")
        exit_program(tool_name=tool_name)