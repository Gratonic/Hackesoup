"""
# :: Author Information and Program Details :: #

File Name: hs_validator.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.10.12
Dependencie(s): colorama
Last Modified: February 8th, 2025

# :: Description :: #

This python file contains the title information used in the hs_menus.py file to build the portion of the header for the menu
portion of the UX menus.
"""

# :: Imports :: #

import hs_menu_titles # for the main menu easter egg
import hs_menus
import hs_prompts
import colorama # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
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

# Used in the menu packs to keep track of the UX menu the user is currently on
current_tool_menu = 1

# This dictionary will change as the user configures the tool they chose
# NOTE: Some tools may not change all the settings because either A) the user doesn't change the setting(s) or B) the chosen tool doesn't use all the settings
hs_config = {
    "tool": "Undefined",
    "target": "192.168.1.1", "port": 3389, "port_range": 1-49151,
    "timeout_amount": 0, "thread_amount": 0,
    "stealth_features": False, 
    "payload_file": None
}

# :: Functionality :: #

# -- Special Functions -- #

# Says "Goodbye!" to the user in German and exits the program
def exit_program() -> None:
    print(f"{magenta}\n\nTschüss!{reset}")
    exit()

# Checks the users chosen configuration option to see if they want to exit the program
def exit_check(user_choice: int) -> None:
    if user_choice == 0:
        exit_program()
    else:
        pass

# -- Individual UX Menu Functions-- #

# Main/Tool UX Menu

def main_UX_menu() -> None:
    hs_menus.main_menu()
    tool_choice = hs_prompts.menu_prompt(first=0, last=7)
    exit_check(tool_choice)
    if tool_choice == 1:
        hs_config["tool"] = "port_scanner"
    elif tool_choice == 2:
        hs_config["tool"] = "subdomain_finder"
    elif tool_choice == 3:
        hs_config["tool"] = "XSS_vuln_scanner"
    elif tool_choice == 4:
        hs_config["tool"] = "dir_trav_vuln_scanner"
    elif tool_choice == 5:
        hs_config["tool"] = "SQLI_vuln_scanner"
    elif tool_choice == 6:
        hs_config["tool"] = "destroyer"
    elif tool_choice == 7:
        floppy_party = hs_menu_titles.floppy_drive_heaven_easter_egg()
        colors = [red, white, blue]
        colorful_floppy_party = ''.join(colors[char % len(colors)] + floppy_party[char] for char in range(len(floppy_party)))
        print(colorful_floppy_party)
        exit_program()

# Port Scanner UX Menus

def port_scanner_UX_menu_1():
    hs_menus.port_scanner_setup_1()
    config_choice = hs_prompts.menu_prompt(first=0, last=3)
    # Will be changed to combo target in future versions
    target = hs_prompts.target_IPv4()
    hs_config["target"] = target
    exit_check(config_choice)
    if config_choice == 1:
        port = hs_prompts.port()
        hs_config["port"] = port
    elif config_choice == 2:
        port_range = hs_prompts.port_range()
        hs_config["port_range"] = port_range
    elif config_choice == 3:
        # 1000 is code for "return to the main menu"
        return 1000

def port_scanner_UX_menu_2():
    # The safe thread amount will be set if the users configuration choice is 1 or 3
    logical_cores = os.cpu_count()
    safe_thread_amount = logical_cores // 4
    hs_menus.port_scanner_setup_2()
    config_choice = hs_prompts.menu_prompt(first=0, last=4)
    exit_check(config_choice)
    if config_choice == 1:
        hs_config["thread_amount"] = safe_thread_amount
        hs_config["timeout_amount"] = 1
        hs_config["stealth_features"] = False
    elif config_choice == 2:
        # status code for "call the advanced settings UX menu (port_scanner_UX_menu_3)"
        return 100
    elif config_choice == 3:
        thread_amount = 4
        if thread_amount > safe_thread_amount or thread_amount < safe_thread_amount:
            thread_amount = safe_thread_amount
        hs_config["thread_amount"] = safe_thread_amount
        hs_config["timeout_amount"] = 3
        hs_config["thread_amount"] = thread_amount
        hs_config["stealth_features"] = True
    elif config_choice == 4:
        # 500 is code for "return to the previous menu"
        return 500

def port_scanner_UX_menu_3():
    pass

# Subdomain Finder UX Menus