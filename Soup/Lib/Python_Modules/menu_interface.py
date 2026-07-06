"""
# :: Author Information and Program Details :: #

File Name: menu_interface.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.12.3
Dependencie(s): hs_menu_titles, hs_menus, hs_prompts, colorama, json, os
Last Modified: October 31, 2025

# :: Description :: #

This is the core menu interface file that puts everything together using the other menu modules.

"""

# [=== Imports ===] #

from colorama import Fore, Back # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
import menataur
import prompts
import json
import os

# [=== Global Variables ===] #

settings = {
    "target": None,
    "tool": None,
    "tool_class": None,
    "API_token": None,
    "port": None, "port_range": None,
    "scan_type": None,
    "save_file": None
}

# [=== Special Functions ===] #

# Clears the users terminal
def clear_terminal():
    if os.name == "posix": # For Linux or MacOS
        os.system("clear")
    else:
        os.system("cls") # For Windows

def save_tool_output() -> None:
    save_to_file = prompts.save_to_file(tool_name=settings["tool"])
    # True or False...
    if save_to_file[0]:
        # stores a file path
        settings["save_file"] = save_to_file[1]
    else:
        # save_to_file is set to None by default
        pass

# checks the user menu choice to see if they want to exit the program and if they do, it will print an exit message and end the program
def exit_check(user_choice: int, tool_name: str) -> None:
    goodbye_messages = {
        "main_menu": "\n\nTschüss!",
        "patchpirate": "\n\nSvako dobro i doviđenja!",
        "serikandor": "\n\nשיהיה לך יום שקט ולהתראות לעת עתה!",
        "dabijar": "\n\nFino alla prossima volta! Arrivederci!",
        "mudelatie": "\n\nWees voorzichtig!",
        "baumspinne": "\n\nVielen Dank für Ihre Unterstützung und die Zusammenarbeit. Wünschend Ihnen alles Gute für die Zukunft. Auf Wiedersehen!",
        "wafter": "\n\nCuídese!",
        "soupemapper": "\n\nGood luck and goodbye!"
    }

    if user_choice == 0:
        exit_message = f"{Fore.MAGENTA}{goodbye_messages[tool_name]}{Fore.RESET}"
        print(exit_message)
        exit()

# -- Settings Reset Functions -- #

def main_menu_settings_reset() -> None:
    settings["target"] = None
    settings["tool"] = None
    settings["tool_class"] = None
    settings["api_token"] = None
    settings["port"] = None
    settings["port_range"] = None
    settings["scan_type"] = None
    settings["save_file"] = None

def patchpirate_menu_settings_reset() -> None:
    settings["target"] = None
    settings["api_token"] = None
    settings["save_file"] = None

def serikandor_menu_1_settings_reset() -> None:
    settings["target"] = None
    settings["save_file"] = None

def dabijar_menu_1_settings_reset() -> None:
    settings["target"] = None
    settings["save_file"] = None

def mudelatie_menu_1_settings_reset() -> None:
    settings["target"] = None
    settings["save_file"] = None

def baumspinne_menu_1_settings_reset() -> None:
    settings["target"] = None
    settings["save_file"] = None

def wafter_menu_1_settings_reset() -> None:
    settings["target"] = None
    settings["save_file"] = None

def soupemapper_menu_1_settings_reset() -> None:
    settings["target"] = None
    settings["port"] = None
    settings["port_range"] = None

def soupemapper_menu_2_settings_reset() -> None:
    settings["scan_type"] = None
    settings["save_file"] = None

# [=== Functionality ===] #

"""
Menu Interface Status Codes:

next_menu - call next menu for the selected tool
previous_menu - return to previous menu
main_menu - return to main menu
done - the user is happy with the configuration and ready to run the selected tool
"""

# -- Menu Construction Functions -- #

# < Main Menu > #

def main_menu() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="main_menu")

    return menu

# < Tool Class Menus > #

def osint_tool_menu() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="osint_tool_menu")

    return menu

def web_tool_menu() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="web_tool_menu")

    return menu


def lan_tool_menu() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="lan_tool_menu")

    return menu

# < PatchPirate Menu(s) > #

def patchpirate_menu_1() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="patchpirate_menu_1")

    return menu

# < Serikanodr Menu(s) > #

def serikandor_menu_1() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="serikandor_menu_1")

    return menu


# < Dabijar Menu(s) > #

def dabijar_menu_1() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="dabijar_menu_1")

    return menu

# < Mudelatie Menu(s) > #

def mudelatie_menu_1() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="mudelatie_menu_1")

    return menu

# < Baumspinne Menu(s) > #

def baumspinne_menu_1() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="baumspinne_menu_1")

    return menu

# < Wafter Menu(s) > #

def wafter_menu_1() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="wafter_menu_1")

    return menu

# < Soupemapper Menu(s) > #

def soupemapper_menu_1() -> object:
    clear_terminal()

    menu = menataur.construct_menu(menu_func_name="soupemapper_menu_1")

    return menu

def soupemapper_menu_2() -> object:
    clear_terminal()
    
    menu = menataur.construct_menu(menu_func_name="soupemapper_menu_2")

    return menu

# -- Menu Input Functions --- #

# < Main Menu Input Functions > #

def handle_main_menu_input() -> str:
    user_choice = prompts.menu_prompt(first=0, last=4, tool_name="NA")
    exit_check(user_choice=user_choice, tool_name="main_menu")

    if user_choice == 1:
        settings["tool_class"] = "osint"
    if user_choice == 2:
        settings["tool_class"] = "web"
    if user_choice == 3:
        settings["tool_class"] = "lan"
    if user_choice == 4:
        clear_terminal()
        # prints some colorful ascii art and exits the program
        menataur.floppy_disk_heaven_easter_egg()
    
    return "next_menu"

# < Tool Class Menus Input Functions > #

def handle_osint_tool_menu_input() -> str:
    user_choice = prompts.menu_prompt(first=0, last=2, tool_name="NA")
    exit_check(user_choice=user_choice, tool_name="main_menu")

    if user_choice == 1:
        settings["tool"] = "patchpirate"
    if user_choice == 2:
        return "main_menu"
    
    return "next_menu"

def handle_web_tool_menu_input() -> str:
    user_choice = prompts.menu_prompt(first=0, last=6, tool_name="NA")
    exit_check(user_choice=user_choice, tool_name="main_menu")

    if user_choice == 1:
        settings["tool"] = "serikandor"
    if user_choice == 2:
        settings["tool"] = "dabijar"
    if user_choice == 3:
        settings["tool"] = "mudelatie"
    if user_choice == 4:
        settings["tool"] = "baumspinne"
    if user_choice == 5:
        settings["tool"] = "wafter"
    if user_choice == 6:
        return "main_menu"
    
    return "next_menu"


def handle_lan_tool_menu_input() -> str:
    user_choice = prompts.menu_prompt(first=0, last=2, tool_name="NA")
    exit_check(user_choice=user_choice, tool_name="main_menu")

    if user_choice == 1:
        settings["tool"] = "soupemapper"
    if user_choice == 2:
        return "main_menu"
    
    return "next_menu"

# < PatchPirate Menu(s) Input Function(s) > #

def handle_patchpirate_menu_1_input() -> str:
    settings["target"] = prompts.target_username(tool_name="patchpirate")

    user_choice =  prompts.menu_prompt(first=0, last=3, tool_name="patchpirate")
    exit_check(user_choice=user_choice, tool_name="patchpirate")

    if user_choice == 1:
        api_token = prompts.api_token(tool_name="patchpirate")
        settings["api_token"] = api_token
        save_tool_output()
    if user_choice == 2:
        save_tool_output()
    if user_choice == 3:
        return "previous_menu"
    
    return "done"

# < Serikanodr Menu(s) Input Function(s) > #

def handle_serikandor_menu_1_input() -> str:
    settings["target"] = prompts.target_website(tool_name="serikandor")
    save_tool_output()

    return "done"


# < Dabijar Menu(s) Input Function(s) > #

def handle_dabijar_menu_1_input() -> str:
    settings["target"] = prompts.target_website_with_params_or_endpoints(tool_name="dabijar")
    save_tool_output()

    return "done"

# < Mudelatie Menu(s) Input Function(s) > #

def handle_mudelatie_menu_1_input() -> str:
    settings["target"] = prompts.target_website_with_params_or_endpoints(tool_name="mudelatie")
    save_tool_output()

    return "done"

# < Baumspinne Menu(s) Input Function(s) > #

def handle_baumspinne_menu_1_input() -> str:
    settings["target"] = prompts.target_website(tool_name="baumspinne")
    save_tool_output()

    return "done"

# < Wafter Menu(s) Input Function(s) > #

def handle_wafter_menu_1_input() -> str:
    settings["target"] = prompts.target_website(tool_name="wafter")
    save_tool_output()

    return "done"

# < Soupemapper Menu(s) Input Function(s) > #

def handle_soupemapper_menu_1_input() -> str:
    user_choice = prompts.menu_prompt(first=0, last=3, tool_name="soupemapper")
    exit_check(user_choice=user_choice, tool_name="soupemapper")

    if user_choice == 1:
        port = prompts.port(tool_name="soupemapper")
        settings["target"] = prompts.target_ipv4(tool_name="soupemapper")
        settings["port"] = port
    if user_choice == 2:
        port_range = prompts.port_range(tool_name="soupemapper")
        settings["target"] = prompts.target_ipv4(tool_name="soupemapper")
        settings["port_range"] = port_range
    if user_choice == 3:
        return "previous_menu"
    
    return "next_menu"

def handle_soupemapper_menu_2_input() -> str:
    user_choice = prompts.menu_prompt(first=0, last=6, tool_name="soupemapper")
    exit_check(user_choice=user_choice, tool_name="soupemapper")

    if user_choice == 1:
        settings["scan_type"] = "TCP_Connect"
        save_tool_output()
    if user_choice == 2:
        settings["scan_type"] = "SYN"
        save_tool_output()
    if user_choice == 3:
        settings["scan_type"] = "UDP"
        save_tool_output()
    if user_choice == 4:
        settings["scan_type"] = "Xmas_Scan"
        save_tool_output()
    if user_choice == 5:
        settings["scan_type"] = "Service_Scan"
        save_tool_output()
    if user_choice == 6:
        return "previous_menu"
    
    return "done"

# -- Menu Interface Function(s) -- #

def handle_status_code(menu_func_name: str, status_code: str)-> str:
    if status_code == "next_menu":
        if settings["tool"] == None:
            next_menu = f"{settings["tool_class"]}_tool_menu"
            response = next_menu # here, never ends func
        else:
            menu_name_parts = menu_func_name.split("_")

            if menu_name_parts[-1].isdigit():
                next_menu_number = str(int(menu_name_parts[-1]) + 1)
                next_menu_name = "_".join(menu_name_parts[:-1] + [next_menu_number])
            
                response = next_menu_name
            else:
                # the user must be in a tool class menu, so the first tool menu is created
                response = f"{settings['tool']}_menu_1"
    if status_code == "previous_menu":
        # resets the current menu's settings
        curr_settings_reset_func_name = f"{menu_func_name}_settings_reset"
        curr_settings_reset_func = globals()[curr_settings_reset_func_name]
        curr_settings_reset_func()

        # because the tool class menu's return status_code of "main_menu" when previous menu is selected...
        prev_menu_number = f"{str(int(menu_func_name.split("_")[-1]) - 1)}"

        """
        if the previous menu number is 0, they must have reached the end of the tool menu loop, so
        this check ensures they will return to the tool selection menu if thats the case

        PS: I know, I know, this part looks a little shit but...
        """
        if int(prev_menu_number) == 0:
            response = f"{settings['tool_class']}_tool_menu"
            return response

        menu_func_name_parts = menu_func_name.split("_")

        # because the number at the end is known about but the exact size of the menu name is unknown...
        menu_func_name = "".join(part + "_" for part in menu_func_name_parts if part != menu_func_name_parts[-1])
            
        prev_menu_name = f"{menu_func_name}{prev_menu_number}"

        response = prev_menu_name

        # resets the previous menu's settings
        prev_settings_reset_func_name = f"{prev_menu_name}_settings_reset"
        prev_settings_reset_func = globals()[prev_settings_reset_func_name]
        prev_settings_reset_func()
    if status_code == "main_menu":
        # resets all settings
        main_menu_settings_reset()

        response = "main_menu"
    if status_code == "done":
        return status_code

    return response

def call_menu(menu_func_name: str) -> None:
    # stores the menu objects and input functions to avoid repeated computation when the user goes back a menu
    menu_cache = {}

    if menu_func_name in menu_cache:
        menu = menu_cache[menu_func_name][0]

        menu_input_func_name = f"handle_{menu_func_name}_input"
        menu_input_func = menu_cache[menu_func_name][1]

        # NOTE: the menu object returned will just be dropped from the function scope here
        menu.display()
        status_code = menu_input_func()

        response = handle_status_code(menu_func_name=menu_func_name, status_code=status_code)

        if response != "done":
            clear_terminal()
            call_menu(menu_func_name=response)
        else:
            clear_terminal()
    else:
        menu_construction_func = globals()[menu_func_name]
        menu = menu_construction_func()

        menu_input_func_name = f"handle_{menu_func_name}_input"
        menu_input_func =  globals()[menu_input_func_name]

        menu_cache[menu_func_name] = [menu, menu_input_func]


        menu.display()
        status_code = menu_input_func()

        response = handle_status_code(menu_func_name=menu_func_name, status_code=status_code)

        if response != "done":
            clear_terminal()
            call_menu(menu_func_name=response)
        else:
            clear_terminal()

def run() -> dict:
    call_menu(menu_func_name="main_menu")
    return settings