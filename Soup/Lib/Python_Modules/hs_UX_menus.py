"""
# :: Author Information and Program Details :: #

File Name: hs_UX_menus.py
Author(s): Gratonic (https://github.com/Gratonic) and ibrahim-sisar (https://github.com/ibrahim-sisar)
Written In: Python 3.12.3
Dependencie(s): hs_menu_titles, hs_menus, hs_prompts, colorama, json, os
Last Modified: June 15th, 2025

# :: Description :: #

This python file contains the title information used in the hs_menus.py file to build the portion of the header for the menu
portion of the UX menus.

"""

# TODO: Fix the minor bug causing you have to enter the target file twice after going back to the first destroyer UX menu -->
# in the destroyer_UX_menu_pack() function or one of the individual UX menus, functions are somewhere between line -->
# 700 and line 807

# :: Imports :: #

from datetime import datetime
import hs_menu_titles # for the main menu easter egg
import hs_menus
import hs_prompts
import colorama # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
import json
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
    "target": None,
    "tool": None,
    "tool_class": None,
    "API_token": None,
    "port": None, "port_range": None,
    "scan_type": None,
    "save_file": None
}

# :: Functionality :: #

# -- Special Functions -- #

# Clears the users terminal
def clear_terminal():
    if os.name == "posix": # For Linux or MacOS
        os.system("clear")
    else:
        os.system("cls") # For Windows

# offers the user a chance to save the tools output
def save_tool_output() -> None:
    save_to_file = hs_prompts.save_to_file(tool_name=hs_config["tool"])
    if save_to_file == True:
        hs_config["save_file"] = f"./Hackesoup/Saves/{hs_config['tool']}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    else:
        hs_config["save_file"] = False

# -- Exit Functions -- #

# Says a simple "Goodbye!" to the user in German and exits the program
def exit_program() -> None:
    print(f"{magenta}\n\nTschüss!{reset}")
    exit()

# Says "Goodbye!" to the user and exits the program
def exit_program_soupemapper() -> None:
    print(f"{magenta}\n\nGood luck and goodbye!{reset}")
    exit()

# Says "Goodbye!" to the user in Arabic and exits the program
def exit_program_serikandor() -> None:
    print(f"{magenta}\n\nغزة تنهي هذا اللقاء، لكنها لا تنتهي!{reset}")
    exit()

# Says "Goodbye!" to the user in Spanish and exits the program
def exit_program_mudelatie() -> None:
    print(f"{magenta}\n\nRecuerda, cada final es un nuevo comienzo. ¡Adios por ahora!{reset}")
    exit()

# Says "Goodbye!" to the user in German and exits the program
def exit_program_baumspinne() -> None:
    print(f"{magenta}\n\nVielen Dank für Ihre Unterstützung und die Zusammenarbeit. Wünschend Ihnen alles Gute für die Zukunft. Auf Wiedersehen!{reset}")
    exit()

def exit_program_dabijar() -> None:
    print(f"{magenta}\n\nFino alla prossima volta! Arrivederci!{reset}")
    exit()

# Says "Goodbye!" and best of luck in Croation
def exit_program_patchpirate() -> None:
    print(f"{magenta}\n\nSvako dobro i doviđenja!{reset}")
    exit()

# Checks the users chosen configuration option to see if they want to exit the program
def exit_check(user_choice: int, tool_name: str) -> None:
    if user_choice == 0 and tool_name == "main_menu":
        exit_program()
    elif user_choice == 0 and tool_name == "patchpirate":
        exit_program_patchpirate()
    elif user_choice == 0 and tool_name == "serikandor":
        exit_program_serikandor()
    elif user_choice == 0 and tool_name == "dabijar":
        exit_program_dabijar()
    elif user_choice == 0 and tool_name == "mudelatie":
        exit_program_mudelatie()
    elif user_choice == 0 and tool_name == "baumspinne":
        exit_program_baumspinne()
    elif user_choice == 0 and tool_name == "soupemapper":
        exit_program_soupemapper()
    else:
        pass

# -- Settings Reset Functions -- #

def total_settings_reset():
    hs_config["target"] = None
    hs_config["tool"] = None
    hs_config["tool_class"] = None
    hs_config["API_token"] = None
    hs_config["port"] = None
    hs_config["port_range"] = None
    hs_config["scan_type"] = None
    hs_config["save_file"] = None

# OSINT Tool Settings Reset Functions #

def patchpirate_menu_settings_reset():
    hs_config["target"] = None
    hs_config["API_token"] = None
    hs_config["save_file"] = None

# Web Tool Settings Reset Functions #

# *Since all of the web tools have the same exact settings*
def web_tool_menu_settings_reset():
    hs_config["target"] = None
    hs_config["save_file"] = None

# Network Tools Settings Reset Functions #

def soupemapper_UX_menu_1_settings_reset():
    hs_config["target"] = None
    hs_config["port"] = None
    hs_config["port_range"] = None

def soupemapper_UX_menu_2_settings_reset():
    hs_config["scan_type"] = None
    hs_config["save_file"] = None

# -- Individual UX Menu Functions-- #

"""
Status Codes For The Menu Interface Functions:

100 - Call next menu for the selected tool
500 - Return to previous menu
1000 - Return to main menu
1500 - Lets the program know the user is happy with the configuration and ready to run the selected tool
"""

# Main and Tool UX Menus

def main_UX_menu()  -> int:
    # Clears the terminal and calls the main menu from hs_menus
    clear_terminal()
    hs_menus.main_menu()
    # Prompts the user for input - last=4 because of easter egg
    tool_class_choice = hs_prompts.menu_prompt(first=0, last=4, tool_name="NA")
    # Preforms an exit check
    exit_check(user_choice=tool_class_choice, tool_name="main_menu")
    # configures the settings based on the users tool choice
    if tool_class_choice == 1:
        hs_config["tool_class"] = "OSINT"
        # menu code for move to the next menu code
        return 100
    elif tool_class_choice == 2:
        hs_config["tool_class"] = "WEB"
        # menu code for move to the next menu code
        return 100
    elif tool_class_choice == 3:
        hs_config["tool_class"] = "LAN"
        # menu code for move to the next menu code
        return 100
    elif tool_class_choice == 4:
        # Clears the terminal
        clear_terminal()
        # Prints the easter egg and exits the program
        floppy_party = hs_menu_titles.floppy_drive_heaven_easter_egg()
        colors = [red, white, blue]
        colorful_floppy_party = ''.join(colors[char % len(colors)] + floppy_party[char] for char in range(len(floppy_party)))
        print(colorful_floppy_party)
        exit_program()

def OSINT_tools_UX_menu() -> int:
    # Clears the terminal and calls the OSINT tool menu from hs_menus
    clear_terminal()
    hs_menus.OSINT_tool_menu()
    # Prompts the user for input
    tool_choice = hs_prompts.menu_prompt(first=0, last=2, tool_name="NA")
    # Preforms an exit check
    exit_check(user_choice=tool_choice, tool_name="main_menu")
    # configures the settings based on the users tool choice
    if tool_choice == 1:
        hs_config["tool"] = "patchpirate"
    elif tool_choice == 2:
        # returns to the main menu
        return 1000
    
    # only way the menu code: 100 is returned for some unknown reason
    if hs_config["tool"] != None:
        # lets the program know the next menu can be called, will be returned if 1000 is not returned
        return 100

def web_tool_UX_menu() -> int:
    # Clears the terminal and calls the web tool menu from hs_menus
    clear_terminal()
    hs_menus.web_tool_menu()
    # Prompts the user for input
    tool_choice = hs_prompts.menu_prompt(first=0, last=5, tool_name="NA")
    # Preforms an exit check
    exit_check(user_choice=tool_choice, tool_name="main_menu")
    # configures the settings based on the users tool choice
    if tool_choice == 1:
        hs_config["tool"] = "serikandor"
    elif tool_choice == 2:
        hs_config["tool"] = "dabijar"
    elif tool_choice == 3:
        hs_config["tool"] = "mudelatie"
    elif tool_choice == 4:
        hs_config["tool"] = "baumspinne"
    elif tool_choice == 5:
        # returns to the main menu
        return 1000
    
    # only way the menu code: 100 is returned for some unknown reason
    if hs_config["tool"] != None:
        # lets the program know the next menu can be called, will be returned if 1000 is not returned
        return 100

def LAN_tool_UX_menu() -> int:
    # Clears the terminal and calls the LAN tool menu from hs_menus
    clear_terminal()
    hs_menus.LAN_tool_menu()
    # Prompts the user for input
    tool_choice = hs_prompts.menu_prompt(first=0, last=2, tool_name="NA")
    # Preforms an exit check
    exit_check(user_choice=tool_choice, tool_name="main_menu")
    # configures the settings based on the users tool choice
    if tool_choice == 1:
        hs_config["tool"] = "soupemapper"
    elif tool_choice == 2:
        # returns to the main menu
        return 1000

    # only way the menu code: 100 is returned for some unknown reason
    if hs_config["tool"] != None:
        # lets the program know the next menu can be called, will be returned if 1000 is not returned
        return 100

# OSINT Tool UX Menus

def patchpirate_UX_menu() -> int | None:
    # promtps the user for their target
    hs_config["target"] = hs_prompts.target_username(tool_name="patchpirate")
    # asks the user if they would like to save the tools output to a file
    save_tool_output()
    # clears the terminal and calls the patchpirate menu again
    clear_terminal()
    hs_menus.patchpirate_menu()
    # prompts the user to choose an option from the menu
    config_choice = hs_prompts.menu_prompt(first=0, last=3, tool_name="patchpirate")
    # preforms an exit check
    exit_check(user_choice=config_choice, tool_name="patchpirate")
    # configures the tool settings based on the users choice
    if config_choice == 1:
        api_token = hs_prompts.api_token(tool_name="patchpirate")
        hs_config["API_token"] = api_token
    elif config_choice == 2:
        hs_config["API_token"] = None
    elif config_choice == 3:
        # returns to the previous menu
        return 500
    
# Web Tool UX Menus

def serikandor_UX_menu() -> int:
     # prompts the user for their target
    hs_config["target"] = hs_prompts.target_website(tool_name="serikandor")
    # asks the user if they would like to save the tools output to a file
    save_tool_output()
    clear_terminal()
    return 1500

def dabijar_UX_menu() -> int:
    # prompts the user for their target
    hs_config["target"] = hs_prompts.target_website(tool_name="dabijar")
    # asks the user if they would like to save the tools output to a file
    save_tool_output()
    clear_terminal()
    return 1500

def mudelatie_UX_menu() -> int:
    # prompts the user for their target
    hs_config["target"] = hs_prompts.target_website(tool_name="mudelatie")
    # asks the user if they would like to save the tools output to a file
    save_tool_output()
    clear_terminal()
    return 1500

def baumspinne_UX_menu() -> int:
    # prompts the user for their target
    hs_config["target"] = hs_prompts.target_website(tool_name="baumspinne")
    # asks the user if they would like to save the tools output to a file
    save_tool_output()
    clear_terminal()
    return 1500

# LAN Tool UX Menus

def soupemapper_UX_menu_1() -> int:
    # clears the terminal and calls the 1st soupemapper menu
    clear_terminal()
    hs_menus.soupemapper_menu_1()
    # prompts the user to choose an option from the menu
    config_choice = hs_prompts.menu_prompt(first=0, last=3, tool_name="soupemapper")
    # preforms an exit check
    exit_check(user_choice=config_choice, tool_name="soupemapper")
    # configures the tool settings based on the users choice
    if config_choice == 1:
        port = hs_prompts.port(tool_name="soupemapper")
        hs_config["port"] = port
        # moves to the next soupemapper menu (required menu)
        return 100
    elif config_choice == 2:
        port_range = hs_prompts.port_range(tool_name="soupemapper")
        hs_config["port_range"] = port_range
        # moves to the next soupemapper menu (required menu)
        return 100
    elif config_choice == 3:
        # returns to the previous menu
        return 500

def soupemapper_UX_menu_2() -> int:
    # clears the terminal and calls the 2nd soupemapper menu
    clear_terminal()
    hs_menus.soupemapper_menu_2()
    # prompts the user to choose an option from the menu
    config_choice = hs_prompts.menu_prompt(first=0, last=11, tool_name="soupemapper")
    # performs an exit check
    exit_check(user_choice=config_choice, tool_name="soupemapper")
    # asks the user if they want to save the tool ouput to a JSON file
    save_tool_output()
    # configures the tool settings based on the user's choice
    if config_choice == 1:
        hs_config["scan_type"] = "TCP_Connect"
    elif config_choice == 2:
        hs_config["scan_type"] = "SYN"
    elif config_choice == 3:
        hs_config["scan_type"] = "FIN"
    elif config_choice == 4:
        hs_config["scan_type"] = "Xmas_Tree"
    elif config_choice == 5:
        hs_config["scan_type"] = "Null"
    elif config_choice == 6:
        hs_config["scan_type"] = "UDP"
    elif config_choice == 7:
        hs_config["scan_type"] = "Service_Version_Detection"
    elif config_choice == 8:
        hs_config["scan_type"] = "Idle"
    elif config_choice == 9:
        hs_config["scan_type"] = "TCP_ACK"
    elif config_choice == 10:
        hs_config["scan_type"] = "ARP"
    elif config_choice == 11:
        # returns to the previous menu
        return 500

# -- UX Menu Packs -- #

# Tool Class UX Menu Pack

def tool_class_menu_pack():
    tool_class = hs_config["tool_class"]
    if tool_class == "OSINT":
        code = OSINT_tools_UX_menu()
        return code
    elif tool_class == "WEB":
        code = web_tool_UX_menu()
        return code
    elif tool_class == "LAN":
        code = LAN_tool_UX_menu()
        return code
    else:
        print(f"{red}[!] Error: The Follwing Error(s) Has/Have Occured{reset}")

# OSINT Tool UX Menu Packs

def patchpirate_UX_menu_pack(current_UX_tool_menu: int) -> int:
    if current_UX_tool_menu == 1:
        code = patchpirate_UX_menu()
        if code == 500:
            patchpirate_menu_settings_reset()
            return code
        else:
            # the user must be happy with the current tool config, so menu code 1500 is returned
            return 1500
    else:
        print(f"{red}[!] Error: Invalid UX Menu Number For Patch Pirate{reset}")
        exit_program()

# Web Tool UX Menu Packs

def serikandor_UX_menu_pack(current_UX_tool_menu: int):
    if current_UX_tool_menu == 1:
        code = serikandor_UX_menu()
        if code == 500:
            web_tool_menu_settings_reset()
            return code
        else:
            # the user must be happy with the current tool config, so menu code 1500 is returned
            return 1500
    else:
        print(f"{red}[!] Error: Invalid UX Menu Number For Subdomain Finder{reset}")
        exit()

def dabijar_UX_menu_pack(current_UX_tool_menu: int):
    if current_UX_tool_menu == 1:
        code = dabijar_UX_menu()
        if code == 500:
            web_tool_menu_settings_reset()
            return code
        else:
            # the user must be happy with the current tool config, so menu code 1500 is returned
            return 1500
    else:
        print(f"{red}[!] Error: Invalid UX Menu Number For SQLI Vuln Scanner{reset}")
        exit()

def mudelatie_UX_menu_pack(current_UX_tool_menu: int):
    if current_UX_tool_menu == 1:
        code = mudelatie_UX_menu()
        if code == 500:
            web_tool_menu_settings_reset()
            return code
        else:
            # the user must be happy with the current tool config, so menu code 1500 is returned
            return 1500
    else:
        print(f"{red}[!] Error: Invalid UX Menu Number For XSS Vuln Scanner{reset}")
        exit()

def baumspinne_UX_menu_pack(current_UX_tool_menu: int):
    if current_UX_tool_menu == 1:
        code = baumspinne_UX_menu()
        if code == 500:
            web_tool_menu_settings_reset()
            return code
        else:
            # the user must be happy with the current tool config, so menu code 1500 is returned
            return 1500
    else:
        print(f"{red}[!] Error: Invalid UX Menu Number For Dir Trav Vuln Scanner{reset}")
        exit()

# LAN Tool UX Menu Packs

def soupemapper_UX_menu_pack() -> int:
    # prompts the user for their target
    hs_config["target"] = hs_prompts.target_IPv4(tool_name="soupemapper")
    while True:
        # Step 1: Run soupemapper menu 1
        code = soupemapper_UX_menu_1()
        if code == 500:
            # User chose to go back to LAN tool menu
            soupemapper_UX_menu_1_settings_reset()
            return 500
        elif code == 100:
            # Step 2: Run soupemapper menu 2
            while True:
                code2 = soupemapper_UX_menu_2()
                if code2 == 500:
                    # User chose to go back to menu 1
                    soupemapper_UX_menu_2_settings_reset()
                    # Break to go back to outer loop (menu 1)
                    break
                else:
                    # User is happy with configuration, ready to run tool
                    return 1500

# :: UX Menu Interface Functions :: #

def write_settings_JSON_to_file(settings: dict):
    # writes the tool config to the input json file
    with open("../Soup/Lib/Data/Input_Data/input.json", "w") as input_file:
        json.dump(settings, input_file, indent=4)

# NOTE: this code can be cleaned up but it works as is, one area it can be cleaned up is the web tool menu section
def menu_interface(start_point: int, code: int):
    if start_point == 1:
        clear_terminal()
        main_menu_code = main_UX_menu()
        menu_interface(start_point=2, code=main_menu_code)
    elif start_point == 2:
        if code == 100:
            code = tool_class_menu_pack()
            if code == 1000:
                # Return to main menu
                menu_interface(start_point=1, code=0)
            elif code == 100:
                if hs_config["tool_class"] == "OSINT":
                    if hs_config["tool"] == "patchpirate":
                        code = patchpirate_UX_menu_pack(1)
                        if code == 500:
                            menu_interface(start_point=2, code=100)  # Go back to OSINT tool menu
                        elif code == 1500:
                            # ready to run the tool
                            save_tool_output()
                            write_settings_JSON_to_file(settings=hs_config)
                            pass
                elif hs_config["tool_class"] == "WEB":
                    if hs_config["tool"] == "serikandor":
                        code = serikandor_UX_menu_pack(1)
                        if code == 500:
                            menu_interface(start_point=2, code=100)
                        elif code == 1500:
                            # ready to run the tool
                            write_settings_JSON_to_file(settings=hs_config)
                            pass
                    elif hs_config["tool"] == "dabijar":
                        code = dabijar_UX_menu_pack(1)
                        if code == 500:
                            menu_interface(start_point=2, code=100)
                        elif code == 1500:
                            # ready to run the tool
                            write_settings_JSON_to_file(settings=hs_config)
                            pass
                    elif hs_config["tool"] == "mudelatie":
                        code = mudelatie_UX_menu_pack(1)
                        if code == 500:
                            menu_interface(start_point=2, code=100)
                        elif code == 1500:
                            # ready to run the tool
                            write_settings_JSON_to_file(settings=hs_config)
                            pass
                    elif hs_config["tool"] == "baumspinne":
                        code = baumspinne_UX_menu_pack(1)
                        if code == 500:
                            menu_interface(start_point=2, code=100)
                        elif code == 1500:
                            # ready to run the tool
                            write_settings_JSON_to_file(settings=hs_config)
                            pass
                elif hs_config["tool_class"] == "LAN":
                    if hs_config["tool"] == "soupemapper":
                        code = soupemapper_UX_menu_pack()
                        if code == 500:
                            menu_interface(start_point=2, code=100)  # Go back to LAN tool menu
                        elif code == 1500:
                            # ready to run the tool
                            write_settings_JSON_to_file(settings=hs_config)
                            pass
                else:
                    print(f"{red}[!] Error: Tool Class Does Not Exist{reset}")
        else:
            print(f"{red}Error: Unknown.{reset}")
            exit_program()