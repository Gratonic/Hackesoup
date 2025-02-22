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

# This dictionary will change as the user configures the tool they chose
# NOTE: Some tools may not change all the settings because either A) the user doesn't change the setting(s) or B) the chosen tool doesn't use all the settings
hs_config = {
    "tool": "NA",
    "target": "NA", "port": "NA", "port_range": "NA",
    "timeout_amount": "NA", "thread_amount": "NA",
    "stealth_features": "NA", 
    "payload_file": "NA"
}

# :: Functionality :: #

# -- Special Functions -- #

def determine_safe_thread_amount() -> int:
    # The safe thread amount will be set if the users configuration choice is 1 or 3
    logical_cores = os.cpu_count()
    safe_thread_amount = logical_cores // 4
    if safe_thread_amount < 1:
        safe_thread_amount = 1
    return safe_thread_amount

# Says a simple "Goodbye!" to the user in German and exits the program
def exit_program() -> None:
    print(f"{magenta}\n\nTschüss!{reset}")
    exit()

# Says "Goodbye!" to the user and exits the program
def exit_program_port_scanner() -> None:
    print(f"{magenta}\n\nGood luck and goodbye!{reset}")
    exit()

# Says "Goodbye!" to the user in Arabic and exits the program
def exit_program_subdomain_finder() -> None:
    print(f"{magenta}\n\nغزة تنهي هذا اللقاء، لكنها لا تنتهي!{reset}")
    exit()

# Says "Goodbye!" to the user in Spanish and exits the program
def exit_program_XSS_scanner() -> None:
    print(f"{magenta}\n\nRecuerda, cada final es un nuevo comienzo. ¡Adios por ahora!{reset}")
    exit()

# Says "Goodbye!" to the user in German and exits the program
def exit_program_dir_trav_scanner() -> None:
    print(f"{magenta}\n\nVielen Dank für Ihre Unterstützung und die Zusammenarbeit. Wünschend Ihnen alles Gute für die Zukunft. Auf Wiedersehen!{reset}")
    exit()

def exit_program_SQLI_scanner() -> None:
    print(f"{magenta}\n\nFino alla prossima volta! Arrivederci!{reset}")
    exit()

def exit_program_destroyer() -> None:
    print(f"{magenta}\n\nज्ञान को अपने जीवन का हिस्सा बनाइए क्योंकि यह आपकी सबसे बड़ी शक्ति है, लेकिन इसका इस्तेमाल दुनिया को बेहतर बनाने के लिए करें, न कि उसे नष्ट करने के लिए। अभी के लिए अलविदा!{reset}")
    exit()

# Checks the users chosen configuration option to see if they want to exit the program
def exit_check(user_choice: int, tool_name: str) -> None:
    if user_choice == 0 and tool_name == "port_scanner":
        exit_program_port_scanner()
    elif user_choice == 0 and tool_name == "subdomain_finder":
        exit_program_subdomain_finder()
    elif user_choice == 0 and tool_name == "XSS_scanner":
        exit_program_XSS_scanner()
    elif user_choice == 0 and tool_name == "dir_trav_scanner":
        exit_program_dir_trav_scanner()
    elif user_choice == 0 and tool_name == "SQLI_scanner":
        exit_program_SQLI_scanner()
    elif user_choice == 0 and tool_name == "destroyer":
        exit_program_destroyer()
    else:
        pass

# Setting Reset Functions

def total_settings_reset():
    hs_config["tool"] = "NA"
    hs_config["payload_file"] = "NA"
    hs_config["port"] = "NA"
    hs_config["port_range"] = "NA"
    hs_config["stealth_features"] = "NA"
    hs_config["target"] = "NA"
    hs_config["thread_amount"] = "NA"
    hs_config["timeout_amount"] = "NA"

# Port Scanner Setting Reset Functions

def port_scanner_UX_menu_1_settings_reset():
    hs_config["target"] = "NA"
    hs_config["port"] = "NA"
    hs_config["port_range"] = "NA"

def port_scanner_UX_menu_2_settings_reset():
    hs_config["thread_amount"] = "NA"
    hs_config["timeout_amount"] = "NA"
    hs_config["stealth_features"] = "NA"

# Sub Domain Finder, XSS Scanner, Directory Traversal Scanner, and SQLI Scanner Reset Functions
# NOTE: These 4 tools have the same menu options and settings, just to make things simple...they're reffered to as squad members
# NOTE: If the previous menu is requested with this menu, all settings must be reset because there is only 2 UX menus

def squad_member_settings_reset():
    hs_config["target"] = "NA"
    hs_config["thread_amount"] = "NA"
    hs_config["timeout_amount"] = "NA"
    hs_config["stealth_features"] = "NA"
    hs_config["payload_file"] = "NA"

# -- Individual UX Menu Functions-- #

# Main/Tool UX Menu

def main_UX_menu() -> None:
    hs_menus.main_menu()
    tool_choice = hs_prompts.menu_prompt(first=0, last=7, tool_name="NA")
    exit_check(tool_choice, tool_name="NA")
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
    config_choice = hs_prompts.menu_prompt(first=0, last=3, tool_name="port_scanner")
    exit_check(config_choice, tool_name="port_scanner")
    if config_choice == 1:
        # Will be changed to combo target in future versions
        target = hs_prompts.target_IPv4(tool_name="port_scanner")
        hs_config["target"] = target
        port = hs_prompts.port(tool_name="port_scanner")
        hs_config["port"] = port
    elif config_choice == 2:
        # Will be changed to combo target in future versions
        target = hs_prompts.target_IPv4(tool_name="port_scanner")
        hs_config["target"] = target
        port_range = hs_prompts.port_range(tool_name="port_scanner")
        hs_config["port_range"] = port_range
    elif config_choice == 3:
        # 1000 is code for "return to the main menu"
        return 1000

def port_scanner_UX_menu_2():
    safe_thread_amount = determine_safe_thread_amount()
    hs_menus.port_scanner_setup_2()
    config_choice = hs_prompts.menu_prompt(first=0, last=4, tool_name="port_scanner")
    exit_check(config_choice, tool_name="port_scanner")
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
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = 3
        hs_config["stealth_features"] = True
    elif config_choice == 4:
        # 500 is code for "return to the previous menu"
        return 500

def port_scanner_UX_menu_3():
    hs_menus.port_scanner_setup_3()
    config_choice = hs_prompts.menu_prompt(first=0, last=7, tool_name="port_scanner")
    exit_check(config_choice, tool_name="port_scanner")
    if config_choice == 1:
        thread_amount = hs_prompts.thread_amount()
        hs_config["thread_amount"] = thread_amount
    elif config_choice == 2:
        timeout_amount = hs_prompts.timeout()
        hs_config["timeout_amount"] = timeout_amount
    elif config_choice == 3:
        thread_amount = hs_prompts.thread_amount()
        timeout_amount = hs_prompts.timeout()
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
    elif config_choice == 4:
        thread_amount = hs_prompts.thread_amount()
        hs_config["thread_amount"] = thread_amount
        hs_config["stealth_features"] = True
    elif config_choice == 5:
        timeout_amount = hs_prompts.timeout()
        hs_config["timeout_amount"] = timeout_amount
        hs_config["stealth_features"] = True
    elif config_choice == 6:
        thread_amount = hs_prompts.thread_amount()
        timeout_amount = hs_prompts.timeout()
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
        hs_config["stealth_features"] = True
    elif config_choice == 7:
        # 500 is code for "return to the previous menu"
        return 500

# Subdomain Finder UX Menus

def subdomain_finder_UX_menu_1():
    hs_menus.sub_domain_finder_setup_1()
    config_choice = hs_prompts.menu_prompt(first=0, last=7, tool_name="subdomain_finder")
    exit_check(config_choice, tool_name="subdomain_finder")
    if config_choice == 1:
        target = hs_prompts.target_website(tool_name="subdomain_finder")
        safe_thread_amount = determine_safe_thread_amount()
        hs_config["target"] = target
        hs_config["thread_amount"] = safe_thread_amount
        hs_config["timeout_amount"] = 1
        hs_config["stealth_features"] = False
        hs_config["payload_file"] = "default"
    elif config_choice == 2:
        target = hs_prompts.target_website(tool_name="subdomain_finder")
        hs_config["target"] = target
        # Tells the program to call the advanced subdomain finder dsettings UX menu
        return 100
    elif config_choice == 3:
        target = hs_prompts.target_website(tool_name="subdomain_finder")
        safe_thread_amount = determine_safe_thread_amount()
        hs_config["thread_amount"] = safe_thread_amount
        hs_config["timeout_amount"] = 3
        hs_config["stealth_features"] = True
        hs_config["payload_file"] = "default"
    elif config_choice == 4:
        # 1000 is code for "return to the main menu"
        return 1000

def subdomain_finder_UX_menu_2():
    hs_menus.sub_domain_finder_setup_2()
    config_choice = hs_prompts.menu_prompt(first=0, last=13, tool_name="subdomain_finder")
    exit_check(config_choice, tool_name="subdomain_finder")
    if config_choice == 1:
        thread_amount = hs_prompts.thread_amount(tool_name="subdomain_finder")
        hs_config["thread_amount"] = thread_amount
    elif config_choice == 2:
        timeout_amount = hs_prompts.timeout(tool_name="subdomain_finder")
        hs_config["timeout_amount"] = timeout_amount
    elif config_choice == 3:
        hs_config["stealth_features"] = True
    elif config_choice == 4:
        thread_amount = hs_prompts.thread_amount(tool_name="subdomain_finder")
        timeout_amount = hs_prompts.timeout(tool_name="subdomain_finder")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
    elif config_choice == 5:
        thread_amount = hs_prompts.thread_amount(tool_name="subdomain_finder")
        hs_config["thread_amount"] = thread_amount
        hs_config["stealth_features"] = True
    elif config_choice == 6:
        timeout_amount = hs_prompts.timeout(tool_name="subdomain_finder")
        hs_config["timeout_amount"] = timeout_amount
        hs_config["stealth_features"] = True
    elif config_choice == 7:
        thread_amount = hs_prompts.thread_amount(tool_name="subdomain_finder")
        timeout_amount = hs_prompts.timeout(tool_name="subdomain_finder")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
        hs_config["stealth_features"] = True
    elif config_choice == 8:
        payload_file = hs_prompts.payload_file_path(tool_name="subdomain_finder")
        hs_config["payload_file"] = payload_file
    elif config_choice == 9:
        payload_file = hs_prompts.payload_file_path(tool_name="subdomain_finder")
        hs_config["payload_file"] = payload_file
        hs_config["stealth_features"] = True
    elif config_choice == 10:
        thread_amount = hs_prompts.thread_amount(tool_name="subdomain_finder")
        payload_file = hs_prompts.payload_file_path(tool_name="subdomain_finder")
        hs_config["thread_amount"] = thread_amount
        hs_config["payload_file"] = payload_file
    elif config_choice == 11:
        timeout_amount = hs_prompts.timeout(tool_name="subdomain_finder")
        payload_file = hs_prompts.payload_file_path(tool_name="subdomain_finder")
        hs_config["timeout_amount"] = timeout_amount
        hs_config["payload_file"] = payload_file
    elif config_choice == 12:
        thread_amount = hs_prompts.thread_amount(tool_name="subdomain_finder")
        timeout_amount = hs_prompts.timeout(tool_name="subdomain_finder")
        payload_file = hs_prompts.payload_file_path(tool_name="subdomain_finder")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
        hs_config["payload_file"] = payload_file
        hs_config["stealth_features"] = True
    elif config_choice == 13:
        # 500 is code for "return to the previous menu"
        return 500

# XSS Scanner UX Menus

def XSS_scanner_UX_menu_1():
    hs_menus.xss_scanner_setup_1()
    config_choice = hs_prompts.menu_prompt(first=0, last=7, tool_name="XSS_scanner")
    exit_check(config_choice, tool_name="XSS_scanner")
    if config_choice == 1:
        target = hs_prompts.target_website(tool_name="XSS_scanner")
        safe_thread_amount = determine_safe_thread_amount()
        hs_config["target"] = target
        hs_config["thread_amount"] = safe_thread_amount
        hs_config["timeout_amount"] = 1
        hs_config["stealth_features"] = False
        hs_config["payload_file"] = "default"
    elif config_choice == 2:
        target = hs_prompts.target_website(tool_name="XSS_scanner")
        hs_config["target"] = target
        # Tells the program to call the advanced subdomain finder dsettings UX menu
        return 100
    elif config_choice == 3:
        target = hs_prompts.target_website(tool_name="XSS_scanner")
        safe_thread_amount = determine_safe_thread_amount()
        hs_config["thread_amount"] = safe_thread_amount
        hs_config["timeout_amount"] = 3
        hs_config["stealth_features"] = True
        hs_config["payload_file"] = "default"
    elif config_choice == 4:
        # 1000 is code for "return to the main menu"
        return 1000

def XSS_scanner_UX_menu_2():
    hs_menus.xss_scanner_setup_2()
    config_choice = hs_prompts.menu_prompt(first=0, last=13, tool_name="XSS_scanner")
    exit_check(config_choice, tool_name="XSS_scanner")
    if config_choice == 1:
        thread_amount = hs_prompts.thread_amount(tool_name="XSS_scanner")
        hs_config["thread_amount"] = thread_amount
    elif config_choice == 2:
        timeout_amount = hs_prompts.timeout(tool_name="XSS_scanner")
        hs_config["timeout_amount"] = timeout_amount
    elif config_choice == 3:
        hs_config["stealth_features"] = True
    elif config_choice == 4:
        thread_amount = hs_prompts.thread_amount(tool_name="XSS_scanner")
        timeout_amount = hs_prompts.timeout(tool_name="XSS_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
    elif config_choice == 5:
        thread_amount = hs_prompts.thread_amount(tool_name="XSS_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["stealth_features"] = True
    elif config_choice == 6:
        timeout_amount = hs_prompts.timeout(tool_name="XSS_scanner")
        hs_config["timeout_amount"] = timeout_amount
        hs_config["stealth_features"] = True
    elif config_choice == 7:
        thread_amount = hs_prompts.thread_amount(tool_name="XSS_scanner")
        timeout_amount = hs_prompts.timeout(tool_name="XSS_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
        hs_config["stealth_features"] = True
    elif config_choice == 8:
        payload_file = hs_prompts.payload_file_path(tool_name="XSS_scanner")
        hs_config["payload_file"] = payload_file
    elif config_choice == 9:
        payload_file = hs_prompts.payload_file_path(tool_name="XSS_scanner")
        hs_config["payload_file"] = payload_file
        hs_config["stealth_features"] = True
    elif config_choice == 10:
        thread_amount = hs_prompts.thread_amount(tool_name="XSS_scanner")
        payload_file = hs_prompts.payload_file_path(tool_name="XSS_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["payload_file"] = payload_file
    elif config_choice == 11:
        timeout_amount = hs_prompts.timeout(tool_name="XSS_scanner")
        payload_file = hs_prompts.payload_file_path(tool_name="XSS_scanner")
        hs_config["timeout_amount"] = timeout_amount
        hs_config["payload_file"] = payload_file
    elif config_choice == 12:
        thread_amount = hs_prompts.thread_amount(tool_name="XSS_scanner")
        timeout_amount = hs_prompts.timeout(tool_name="XSS_scanner")
        payload_file = hs_prompts.payload_file_path(tool_name="XSS_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
        hs_config["payload_file"] = payload_file
        hs_config["stealth_features"] = True
    elif config_choice == 13:
        # 500 is code for "return to the previous menu"
        return 500

# Directory Traversal Scanner UX Menus

def dir_trav_scanner_UX_menu_1():
    hs_menus.sub_domain_finder_setup_1()
    config_choice = hs_prompts.menu_prompt(first=0, last=7, tool_name="dir_trav_scanner")
    exit_check(config_choice, tool_name="dir_trav_scanner")
    if config_choice == 1:
        target = hs_prompts.target_website(tool_name="dir_trav_scanner")
        safe_thread_amount = determine_safe_thread_amount()
        hs_config["target"] = target
        hs_config["thread_amount"] = safe_thread_amount
        hs_config["timeout_amount"] = 1
        hs_config["stealth_features"] = False
        hs_config["payload_file"] = "default"
    elif config_choice == 2:
        target = hs_prompts.target_website(tool_name="dir_trav_scanner")
        hs_config["target"] = target
        # Tells the program to call the advanced subdomain finder dsettings UX menu
        return 100
    elif config_choice == 3:
        target = hs_prompts.target_website(tool_name="dir_trav_scanner")
        safe_thread_amount = determine_safe_thread_amount()
        hs_config["thread_amount"] = safe_thread_amount
        hs_config["timeout_amount"] = 3
        hs_config["stealth_features"] = True
        hs_config["payload_file"] = "default"
    elif config_choice == 4:
        # 1000 is code for "return to the main menu"
        return 1000

def dir_trav_scanner_UX_menu_2():
    hs_menus.sub_domain_finder_setup_2()
    config_choice = hs_prompts.menu_prompt(first=0, last=13, tool_name="dir_trav_scanner")
    exit_check(config_choice, tool_name="dir_trav_scanner")
    if config_choice == 1:
        thread_amount = hs_prompts.thread_amount(tool_name="dir_trav_scanner")
        hs_config["thread_amount"] = thread_amount
    elif config_choice == 2:
        timeout_amount = hs_prompts.timeout(tool_name="dir_trav_scanner")
        hs_config["timeout_amount"] = timeout_amount
    elif config_choice == 3:
        hs_config["stealth_features"] = True
    elif config_choice == 4:
        thread_amount = hs_prompts.thread_amount(tool_name="dir_trav_scanner")
        timeout_amount = hs_prompts.timeout(tool_name="dir_trav_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
    elif config_choice == 5:
        thread_amount = hs_prompts.thread_amount(tool_name="dir_trav_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["stealth_features"] = True
    elif config_choice == 6:
        timeout_amount = hs_prompts.timeout(tool_name="dir_trav_scanner")
        hs_config["timeout_amount"] = timeout_amount
        hs_config["stealth_features"] = True
    elif config_choice == 7:
        thread_amount = hs_prompts.thread_amount(tool_name="dir_trav_scanner")
        timeout_amount = hs_prompts.timeout(tool_name="dir_trav_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
        hs_config["stealth_features"] = True
    elif config_choice == 8:
        payload_file = hs_prompts.payload_file_path(tool_name="dir_trav_scanner")
        hs_config["payload_file"] = payload_file
    elif config_choice == 9:
        payload_file = hs_prompts.payload_file_path(tool_name="dir_trav_scanner")
        hs_config["payload_file"] = payload_file
        hs_config["stealth_features"] = True
    elif config_choice == 10:
        thread_amount = hs_prompts.thread_amount(tool_name="dir_trav_scanner")
        payload_file = hs_prompts.payload_file_path(tool_name="dir_trav_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["payload_file"] = payload_file
    elif config_choice == 11:
        timeout_amount = hs_prompts.timeout(tool_name="dir_trav_scanner")
        payload_file = hs_prompts.payload_file_path(tool_name="dir_trav_scanner")
        hs_config["timeout_amount"] = timeout_amount
        hs_config["payload_file"] = payload_file
    elif config_choice == 12:
        thread_amount = hs_prompts.thread_amount(tool_name="dir_trav_scanner")
        timeout_amount = hs_prompts.timeout(tool_name="dir_trav_scanner")
        payload_file = hs_prompts.payload_file_path(tool_name="dir_trav_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
        hs_config["payload_file"] = payload_file
        hs_config["stealth_features"] = True
    elif config_choice == 13:
        # 500 is code for "return to the previous menu"
        return 500

# SQLI Scanner UX Menus

def SQLI_scanner_UX_menu_1():
    hs_menus.sub_domain_finder_setup_1()
    config_choice = hs_prompts.menu_prompt(first=0, last=7, tool_name="SQLI_scanner")
    exit_check(config_choice, tool_name="SQLI_scanner")
    if config_choice == 1:
        target = hs_prompts.target_website(tool_name="SQLI_scanner")
        safe_thread_amount = determine_safe_thread_amount()
        hs_config["target"] = target
        hs_config["thread_amount"] = safe_thread_amount
        hs_config["timeout_amount"] = 1
        hs_config["stealth_features"] = False
        hs_config["payload_file"] = "default"
    elif config_choice == 2:
        target = hs_prompts.target_website(tool_name="SQLI_scanner")
        hs_config["target"] = target
        # Tells the program to call the advanced subdomain finder dsettings UX menu
        return 100
    elif config_choice == 3:
        target = hs_prompts.target_website(tool_name="SQLI_scanner")
        safe_thread_amount = determine_safe_thread_amount()
        hs_config["thread_amount"] = safe_thread_amount
        hs_config["timeout_amount"] = 3
        hs_config["stealth_features"] = True
        hs_config["payload_file"] = "default"
    elif config_choice == 4:
        # 1000 is code for "return to the main menu"
        return 1000

def SQLI_scanner_UX_menu_2():
    hs_menus.sub_domain_finder_setup_2()
    config_choice = hs_prompts.menu_prompt(first=0, last=13, tool_name="SQLI_scanner")
    exit_check(config_choice, tool_name="SQLI_scanner")
    if config_choice == 1:
        thread_amount = hs_prompts.thread_amount(tool_name="SQLI_scanner")
        hs_config["thread_amount"] = thread_amount
    elif config_choice == 2:
        timeout_amount = hs_prompts.timeout(tool_name="SQLI_scanner")
        hs_config["timeout_amount"] = timeout_amount
    elif config_choice == 3:
        hs_config["stealth_features"] = True
    elif config_choice == 4:
        thread_amount = hs_prompts.thread_amount(tool_name="SQLI_scanner")
        timeout_amount = hs_prompts.timeout(tool_name="SQLI_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
    elif config_choice == 5:
        thread_amount = hs_prompts.thread_amount(tool_name="SQLI_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["stealth_features"] = True
    elif config_choice == 6:
        timeout_amount = hs_prompts.timeout(tool_name="SQLI_scanner")
        hs_config["timeout_amount"] = timeout_amount
        hs_config["stealth_features"] = True
    elif config_choice == 7:
        thread_amount = hs_prompts.thread_amount(tool_name="SQLI_scanner")
        timeout_amount = hs_prompts.timeout(tool_name="SQLI_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
        hs_config["stealth_features"] = True
    elif config_choice == 8:
        payload_file = hs_prompts.payload_file_path(tool_name="SQLI_scanner")
        hs_config["payload_file"] = payload_file
    elif config_choice == 9:
        payload_file = hs_prompts.payload_file_path(tool_name="SQLI_scanner")
        hs_config["payload_file"] = payload_file
        hs_config["stealth_features"] = True
    elif config_choice == 10:
        thread_amount = hs_prompts.thread_amount(tool_name="SQLI_scanner")
        payload_file = hs_prompts.payload_file_path(tool_name="SQLI_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["payload_file"] = payload_file
    elif config_choice == 11:
        timeout_amount = hs_prompts.timeout(tool_name="SQLI_scanner")
        payload_file = hs_prompts.payload_file_path(tool_name="SQLI_scanner")
        hs_config["timeout_amount"] = timeout_amount
        hs_config["payload_file"] = payload_file
    elif config_choice == 12:
        thread_amount = hs_prompts.thread_amount(tool_name="SQLI_scanner")
        timeout_amount = hs_prompts.timeout(tool_name="SQLI_scanner")
        payload_file = hs_prompts.payload_file_path(tool_name="SQLI_scanner")
        hs_config["thread_amount"] = thread_amount
        hs_config["timeout_amount"] = timeout_amount
        hs_config["payload_file"] = payload_file
        hs_config["stealth_features"] = True
    elif config_choice == 13:
        # 500 is code for "return to the previous menu"
        return 500

# Destroyer UX Menus

def destroyer_UX_menu_1():
    pass

def destroyer_UX_menu_2():
    pass

# :: UX Menu Pack Functions :: #

# Port Scanner UX Menu Pack

def port_scanner_UX_menu_pack(current_UX_tool_menu: int):
    if current_UX_tool_menu == 1:
        requested_UX_menu = port_scanner_UX_menu_1()
        if requested_UX_menu == None:
            port_scanner_UX_menu_pack(2)
        # 1000 is code for "go back to the main/tool UX menu"
        elif requested_UX_menu == 1000:
            # Resets the program configuration
            total_settings_reset()
            # Calls the main/tool UX menu
            main_UX_menu()
    elif current_UX_tool_menu == 2:
        requested_UX_menu = port_scanner_UX_menu_2()
        # 100 == call the advanced settings menu (port_scanner_UX_menu_3)
        if requested_UX_menu == 100:
            port_scanner_UX_menu_pack(3)
        # 500 == call the previous menu
        elif requested_UX_menu == 500:
            # Resets any possible settings that may have been conifgured in the last UX menu
            port_scanner_UX_menu_1_settings_reset()
            # Calls the previous UX menu
            port_scanner_UX_menu_pack(1)
        else:
            # This code lets the program know the user is happy with the current configuration
            return 1500
    elif current_UX_tool_menu == 3:
        requested_UX_menu = port_scanner_UX_menu_3()
        # 500 == call the previous menu
        if requested_UX_menu == 500:
            # Resets any possible settings that may have been conifgured in the last UX menu
            port_scanner_UX_menu_2_settings_reset()
            # Calls the previous UX menu
            port_scanner_UX_menu_pack(2)
        else:
            # This code lets the program know the user is happy with the current configuration
            return 1500

# Subdomain Finder UX Menu Pack

def subdomain_finder_UX_menu_pack(current_UX_menu: int):
    if current_UX_menu == 1:
        requested_UX_menu = subdomain_finder_UX_menu_1()
        if requested_UX_menu == None:
            # This code lets the program know the user is happy with the current configuration
            return 1500
        elif requested_UX_menu == 100:
            requested_UX_menu = subdomain_finder_UX_menu_2()
            if requested_UX_menu == 500:
                squad_member_settings_reset()
                subdomain_finder_UX_menu_pack(1)
        elif requested_UX_menu == 1000:
            squad_member_settings_reset()
            main_UX_menu()

# XSS Scanner UX Menu Pack

def XSS_scanner_UX_menu_pack(current_UX_menu: int):
    if current_UX_menu == 1:
        requested_UX_menu = XSS_scanner_UX_menu_1()
        if requested_UX_menu == None:
            # This code lets the program know the user is happy with the current configuration
            return 1500
        elif requested_UX_menu == 100:
            requested_UX_menu = XSS_scanner_UX_menu_2()
            if requested_UX_menu == 500:
                squad_member_settings_reset()
                XSS_scanner_UX_menu_pack(1)
        elif requested_UX_menu == 1000:
            squad_member_settings_reset()
            main_UX_menu()

# Directory Traversal Scanner UX Menu Pack

def dir_trav_scanner_UX_menu_pack(current_UX_menu: int):
    if current_UX_menu == 1:
        requested_UX_menu = dir_trav_scanner_UX_menu_1()
        if requested_UX_menu == None:
            # This code lets the program know the user is happy with the current configuration
            return 1500
        elif requested_UX_menu == 100:
            requested_UX_menu = dir_trav_scanner_UX_menu_2()
            if requested_UX_menu == 500:
                squad_member_settings_reset()
                dir_trav_scanner_UX_menu_pack(1)
        elif requested_UX_menu == 1000:
            squad_member_settings_reset()
            main_UX_menu()

# SQLI Scanner UX Menu Pack

def SQLI_scanner_UX_menu_pack(current_UX_menu: int):
    if current_UX_menu == 1:
        requested_UX_menu = SQLI_scanner_UX_menu_1()
        if requested_UX_menu == None:
            # This code lets the program know the user is happy with the current configuration
            return 1500
        elif requested_UX_menu == 100:
            requested_UX_menu = SQLI_scanner_UX_menu_2()
            if requested_UX_menu == 500:
                squad_member_settings_reset()
                SQLI_scanner_UX_menu_pack(1)
        elif requested_UX_menu == 1000:
            squad_member_settings_reset()
            main_UX_menu()

# Destroyer UX Menu Pack