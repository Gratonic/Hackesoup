"""
# :: Author Information and Program Details :: #

File Name: hs_menus.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.10.12
Dependencie(s): minotaur, hs_menu_titles
Last Modified: February 8th, 2025

# :: Description :: #

This Python file contains the menu functions used to build the UX Menu Interface. The most critical function is the menu_builder()
function, which is responsible for building the menu portion of every menu and printing it to the output console. The other
functions simply use the menu_builder() function to build the menus for each tool or in the case of the main menu, the tool menu.
This code is imported and used in the hs_UX_menus.py file.
"""

# :: Imports :: #

import menataur
import hs_menu_titles

# :: Functions :: #

# Creates and prints the menu portion of the UX menu
def menu_builder(menu_title_func_name: str, mops: dict, meds: dict, tool_version: str) -> vars:
    # Title Content
    _title_func = getattr(hs_menu_titles, menu_title_func_name)
    _title_contents = _title_func()
    _ascii_title = _title_contents[0]
    _title_bar = _title_contents[1]
    _title_colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    _small_title = _title_contents[2]
    # Menu Options and Option Numbers
    _menu_opt_nums = list(mops.keys())
    _menu_opts = list(mops.values())
    # Menu Option Descriptions
    _menu_descriptions = list(meds.values())
    # Initalizes the menu
    menu = menataur.Menataur()
    # Builds the menu header (title, program support info, etc.)
    menu.add_header(
        ascii_art_title=_ascii_title,
        title_bar=_title_bar,
        title_colors = ["red", "yellow", "green", "cyan", "blue", "magenta"],
        small_title=_small_title,
        program_version_color = "green",
        program_version_num = tool_version,
        os_support_message_color = "black",
        os_support_highlight_color = "yellow",
        os_support_color = "magenta",
        os_support_info = ["Linux"]
    )
    # Adds the Exit Option to the menu
    menu.add_body(
    accent_color="grey", 
    menu_option_number=0, 
    menu_option_color="grey", 
    menu_option="Exit"
    )
    _pos = 0
    _opt_num = 1
    _last_option = 1
    for element in range(len(_menu_opts)):
        menu.add_paragraph(
            text_color="blue", 
            text=_menu_descriptions[_pos]
        )
        menu.add_body(
            accent_color="yellow", 
            menu_option_number=_opt_num, 
            menu_option_color="magenta", 
            menu_option=_menu_opts[_pos]
        )
        _pos += 1
        _opt_num += 1
        _last_option += 1
    # Adds the Previous Menu Option to the menu
    menu.add_body(
    accent_color="grey", 
    menu_option_number=_last_option, 
    menu_option_color="grey", 
    menu_option="Previous Menu"
    )
    # Prints the menu portion of the UX menu
    menu.execute()

# Main Menu - Toolbox Menu
def main_menu() -> None:
    options = {
        1: " Port Scanner (Clam Chowder Soup - American)", 2: " Subdomain Finder (Kartoffelsuppe Soup - German)", 3: " XSS Vulnerability Scanner (Chicken Noodle Soup - Chinese)",
        4: " Directory Traversal Vulnerability Scanner (Onion Soup - French)", 5: " SQLI Vulnerability Scanners (Tom Yum Soup - Indonesian)", 6: " Destroyer (Mulligatawny Soup - Indian)"
    }
    descriptions = {
        1: "scans port to see if they are open, closed, or filtered", 2: "finds the subdomains of a websites",
        3: "scans a website for XSS vulnerabilities", 4: "scans a website for directory traversal vulnerabilities",
        5: "scans a website for SQLI vulnerabilities", 6: "adds a junk data to a file, encrypts it with aes, then overwrites it and deletes it"
    }
    # Builds the menu portion of the main UX menu and prints it
    menu_builder(menu_title_func_name="hackesoup", mops=options, meds=descriptions, tool_version="1.0")

# Port Scanner Menus
def port_scanner_setup_1() -> None:
    menu_1_options = {
        1: "Single Port", 2: "Port Range"
    }
    menu_1_descriptions = {
        1: "scan a single port", 2: "scan a range of ports"
    }
    menu_builder(menu_title_func_name="port_scanner", mops=menu_1_options, meds=menu_1_descriptions, tool_version="1.0")

def port_scanner_setup_2() -> None:
    menu_2_options = {
        1: "Basic Scan", 2: "Advanced Scan", 3: "Stealth Scan"
    }
    menu_2_descriptions = {
        1: "scan without any stealth and/or firewall evasion features",
        2: "configure the scanner settings for this scan",
        3: "use stealth and firewall evasion features - NSFW"
    }
    menu_builder(menu_title_func_name="port_scanner", mops=menu_2_options, meds=menu_2_descriptions, tool_version="1.0")

def port_scanner_setup_3():
    menu_3_options = {
        1: "Adjust Thread Count", 2: "Adjust Timeout", 
        3: "Adjust Thread Count and Timeout", 4: "Adjust Thread Count and Preform A Stealth Scan", 
        5: "Adjust Timeout and Preform A Stealth Scan", 6: "Adjust Thread Count, Adjust Timeout, and Preform A Stealth Scan"
    }
    menu_3_descriptions = {
        1: "adjust the amount of threads", 2: "adjust the timeout", 
        3: "adjust both the thread amount and timeout", 4: "adjust the thread amount and use stealth/firewall evasion features - NSFW", 
        5: "adjust the timeout and use stealth/firewall evasion features - NSFW", 6: "adjust both the thread count and timeout and use stealth/firewall evasion features - NSFW"
    }
    menu_builder(menu_title_func_name="port_scanner", mops=menu_3_options, meds=menu_3_descriptions, tool_version="1.0")

# Sub Domain Finder Menus
def sub_domain_finder_setup_1() -> None:
    menu_1_options = {
        1: "Basic Search",
        2: "Advanced Search",
        3: "Stealth Search"
    }
    menu_1_descriptions = {
        1: "preform a search without stealth/firewall evasion features",
        2: "configure the subdomain finder settings for this search",
        3: "preform a search with stealth/firewall evasion features - NSFW"
    }
    menu_builder(menu_title_func_name="sub_domain_finder", mops=menu_1_options, meds=menu_1_descriptions, tool_version="1.0")

def sub_domain_finder_setup_2() -> None:
    menu_2_options = {
        1: "Adjust Thread Amount", 2: "Adjust Timeout",
        3: "Use stealth/firewall evasion features", 4: "Adjust Thread Amount and Timeout", 
        5: "Use Stealth Features and Adjust Thread Amount", 6: "Use Steatlh Features and Adjust Timeout", 
        7: "Use Stealth Features, Adjust Thread Amount, and Adjust Timeout", 8: "Use Custom Payload File", 
        9: "Use Custom Payload File and Stealth Features", 10: "Use Custom Payload File and Adjust Thread Amount", 
        11: "Use Custom Payload File and Adjust Timeout", 12: "Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features"
    }
    menu_2_descriptions = {
        1: "adjust the thread count", 2: "adjust the timeout",
        3: "use stealth/firewall evasion features", 4: "adjust both the thread count and timeout", 
        5: "use stealth/firewall evasion features and adjust the thread count - NSFW", 6: "use stealth/firewall evasion features and adjust the timeout - NSFW", 
        7: "use stealth/firewall evasion features and adjust both the thread count and timeout - NSFW", 8: "use a custom payload file", 
        9: "use a custom payload file and stealth/firewall evasion features - NSFW", 10: "use a custom payload file and adjust the thread count",
        11: "use a custom payload file and adjust the timeout", 12: "use a custom payload file, adjust both the thread count and timeout, and use stealth/firewall evasion features - NSFW"
    }
    menu_builder(menu_title_func_name="sub_domain_finder", mops=menu_2_options, meds=menu_2_descriptions, tool_version="1.0")

# XSS Scanner Menus
def xss_scanner_setup_1() -> None:
    menu_1_options = {
        1: "Basic Search",
        2: "Advanced Search",
        3: "Stealth Search"
    }
    menu_1_descriptions = {
        1: "preform a search without stealth/firewall evasion features",
        2: "configure the subdomain finder settings for this search",
        3: "preform a search with stealth/firewall evasion features - NSFW"
    }
    menu_builder(menu_title_func_name="xss_scanner", mops=menu_1_options, meds=menu_1_descriptions, tool_version="1.0")

def xss_scanner_setup_2() -> None:
    menu_2_options = {
        1: "Adjust Thread Amount", 2: "Adjust Timeout",
        3: "Use stealth/firewall evasion features", 4: "Adjust Thread Amount and Timeout", 
        5: "Use Stealth Features and Adjust Thread Amount", 6: "Use Steatlh Features and Adjust Timeout", 
        7: "Use Stealth Features, Adjust Thread Amount, and Adjust Timeout", 8: "Use Custom Payload File", 
        9: "Use Custom Payload File and Stealth Features", 10: "Use Custom Payload File and Adjust Thread Amount", 
        11: "Use Custom Payload File and Adjust Timeout", 12: "Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features"
    }
    menu_2_descriptions = {
        1: "adjust the thread count", 2: "adjust the timeout",
        3: "use stealth/firewall evasion features", 4: "adjust both the thread count and timeout", 
        5: "use stealth/firewall evasion features and adjust the thread count - NSFW", 6: "use stealth/firewall evasion features and adjust the timeout - NSFW", 
        7: "use stealth/firewall evasion features and adjust both the thread count and timeout - NSFW", 8: "use a custom payload file", 
        9: "use a custom payload file and stealth/firewall evasion features - NSFW", 10: "use a custom payload file and adjust the thread count",
        11: "use a custom payload file and adjust the timeout", 12: "use a custom payload file, adjust both the thread count and timeout, and use stealth/firewall evasion features - NSFW"
    }
    menu_builder(menu_title_func_name="xss_scanner", mops=menu_2_options, meds=menu_2_descriptions, tool_version="1.0")

# Directory Traversal Scanner Menus
def dir_traversal_scanner_setup_1() -> None:
    menu_1_options = {
        1: "Basic Search",
        2: "Advanced Search",
        3: "Stealth Search"
    }
    menu_1_descriptions = {
        1: "preform a search without stealth/firewall evasion features",
        2: "configure the subdomain finder settings for this search",
        3: "preform a search with stealth/firewall evasion features - NSFW"
    }
    menu_builder(menu_title_func_name="dir_trav_scanner", mops=menu_1_options, meds=menu_1_descriptions, tool_version="1.0")

def dir_traversal_scanner_setup_2() -> None:
    menu_2_options = {
        1: "Adjust Thread Amount", 2: "Adjust Timeout",
        3: "Use stealth/firewall evasion features", 4: "Adjust Thread Amount and Timeout", 
        5: "Use Stealth Features and Adjust Thread Amount", 6: "Use Steatlh Features and Adjust Timeout", 
        7: "Use Stealth Features, Adjust Thread Amount, and Adjust Timeout", 8: "Use Custom Payload File", 
        9: "Use Custom Payload File and Stealth Features", 10: "Use Custom Payload File and Adjust Thread Amount", 
        11: "Use Custom Payload File and Adjust Timeout", 12: "Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features"
    }
    menu_2_descriptions = {
        1: "adjust the thread count", 2: "adjust the timeout",
        3: "use stealth/firewall evasion features", 4: "adjust both the thread count and timeout", 
        5: "use stealth/firewall evasion features and adjust the thread count - NSFW", 6: "use stealth/firewall evasion features and adjust the timeout - NSFW", 
        7: "use stealth/firewall evasion features and adjust both the thread count and timeout - NSFW", 8: "use a custom payload file", 
        9: "use a custom payload file and stealth/firewall evasion features - NSFW", 10: "use a custom payload file and adjust the thread count",
        11: "use a custom payload file and adjust the timeout", 12: "use a custom payload file, adjust both the thread count and timeout, and use stealth/firewall evasion features - NSFW"
    }
    menu_builder(menu_title_func_name="dir_trav_scanner", mops=menu_2_options, meds=menu_2_descriptions, tool_version="1.0")

# SQLI Scanner Menus
def sqli_scanner_setup_1() -> None:
    menu_1_options = {
        1: "Basic Search",
        2: "Advanced Search",
        3: "Stealth Search"
    }
    menu_1_descriptions = {
        1: "preform a search without stealth/firewall evasion features",
        2: "configure the subdomain finder settings for this search",
        3: "preform a search with stealth/firewall evasion features - NSFW"
    }
    menu_builder(menu_title_func_name="sqli_scanner", mops=menu_1_options, meds=menu_1_descriptions, tool_version="1.0")

def sqli_scanner_setup_2() -> None:
    menu_2_options = {
        1: "Adjust Thread Amount", 2: "Adjust Timeout",
        3: "Use stealth/firewall evasion features", 4: "Adjust Thread Amount and Timeout", 
        5: "Use Stealth Features and Adjust Thread Amount", 6: "Use Steatlh Features and Adjust Timeout", 
        7: "Use Stealth Features, Adjust Thread Amount, and Adjust Timeout", 8: "Use Custom Payload File", 
        9: "Use Custom Payload File and Stealth Features", 10: "Use Custom Payload File and Adjust Thread Amount", 
        11: "Use Custom Payload File and Adjust Timeout", 12: "Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features"
    }
    menu_2_descriptions = {
        1: "adjust the thread count", 2: "adjust the timeout",
        3: "use stealth/firewall evasion features", 4: "adjust both the thread count and timeout", 
        5: "use stealth/firewall evasion features and adjust the thread count - NSFW", 6: "use stealth/firewall evasion features and adjust the timeout - NSFW", 
        7: "use stealth/firewall evasion features and adjust both the thread count and timeout - NSFW", 8: "use a custom payload file", 
        9: "use a custom payload file and stealth/firewall evasion features - NSFW", 10: "use a custom payload file and adjust the thread count",
        11: "use a custom payload file and adjust the timeout", 12: "use a custom payload file, adjust both the thread count and timeout, and use stealth/firewall evasion features - NSFW"
    }
    menu_builder(menu_title_func_name="sqli_scanner", mops=menu_2_options, meds=menu_2_descriptions, tool_version="1.0")

# Destroyer Menus
def destroyer_setup_1() -> None:
    menu_1_options = {
        1: "Basic Destruction", 2: "Advanced Destruction"
    }
    menu_1_descriptions = {
        1: "add random data to the file, encrypt it with a modern AES based cipher (256-bit key), overwrite it 10 times, and delete it",
        2: "choose what the destroyer does to the file"
    }
    menu_builder(menu_title_func_name="destroyer", mops=menu_1_options, meds=menu_1_descriptions, tool_version="1.0")

def destroyer_setup_2() -> None:
    menu_2_options = {
        1: "Permanently Encrypt File with a Modern AES Cipher",
        2: "Overwrite The File with Random Data X Amount of Times",
        3: "Permanently Encrypt File with a Modern AES Cipher and Overwrite The File with Random Data X Amount Of Times",
        4: "Delete The File",
        5: "Permanently Encrypt File with a Modern AES Cipher, Overwrite The File X Amount Of Times, and Delete The File"
    }
    menu_2_descriptions = {
        1: "encrypt the file using a 256-bit key with a modern AES cipher",
        2: "overwrite the file with random data X amount of times (default: 10)",
        3: "encrypt the file using a 256-bit key with a modern AES cipher and overwrite it X amount of times (default: 10)",
        4: "simply delete the file",
        5: "encrypt the file using a 256-bit key with a modern AES cipher, overwrite it X amount of times (default: 10), and delete it"
    }
    menu_builder(menu_title_func_name="destroyer", mops=menu_2_options, meds=menu_2_descriptions, tool_version="1.0")
