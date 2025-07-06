"""
# :: Author Information and Program Details :: #

File Name: hsmi.py
Author(s): Gratonic (https://github.com/Gratonic) and ibrahim-sisar (https://github.com/ibrahim-sisar) and Br0k3nPix3l (https://github.com/FailurePoint)
Written In: Python 3.10.12
Dependencie(s): sys, os, importlib, colorama, hs_UX_menus, patch_pirate, json, datetime
Last Modified: April 26th, 2025

# :: Description :: #

This python file is responsible for running the entire menu interface version of Hackesoup.

"""

# :: Imports :: #

import sys
import os
import asyncio
import importlib
import colorama # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
import json
from datetime import datetime

# -- Python Module Imports -- #

python_modules_path = os.path.join(os.path.dirname(__file__), '..', 'Soup', 'Lib', 'Python_Modules')

sys.path.append(python_modules_path)

# menu interface module
hs_UX_menus = importlib.import_module('hs_UX_menus')

# -- Tool Imports -- #

tools_path = os.path.join(os.path.dirname(__file__), '..', 'Soup', 'Tools')
sys.path.append(tools_path)
# saifandor module
# Saifandor_path = os.path.join(os.path.dirname(__file__), '..', 'Soup', 'Tools', 'Saifandor')
# sys.path.append(Saifandor_path)

# patch_pirate_module - hspatchpirate scanner only works on Linux Mint 21.x (not even 22)
# patch_pirate = importlib.import_module('patch_pirate')

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

# :: Global Variables :: #

# placeholder for the tool settings, just need to get the tool chosen
settings = None

# placeholder for the tool output, used when the user wants to save the tool output
output = None

# clears the input JSON file
def clear_input_file() -> None:
    # recreates the file
    with open("../Soup/Lib/Data/Input_Data/input.json", "w"):
        pass

def clear_output_file() -> None:
    # recreates the file
    with open("../Soup/Lib/Data/Output_Data/output.json", "w"):
        pass

# reads the input JSON
def read_input_file() -> None:
    global settings
    with open("../Soup/Lib/Data/Input_Data/input.json", "r") as settings_file:
        settings = json.load(settings_file)

# read the output JSON
def read_output_file() -> None:
    global output
    with open("../Soup/Lib/Data/Output_Data/output.json", "r") as output_file:
        output = json.load(output_file)

# saves the output file
def save_output_to_file() -> None:
    # grabs the output data
    read_output_file()
    # forms the file path to write the output data to for the save
    now = datetime.now()
    formatted_time = now.strftime('%Y-%m-%d_%H-%M-%S')
    save_file_path = f"../Saves/save_{formatted_time}.json"
    with open(save_file_path, "w") as save_file:
        json.dump(output, save_file, indent=4)

if __name__ == "__main__":
    # clears the input file and output file in case their is any sensitive information, first step
    # NOTE: Will be uncommented when all tools have been added to the menu
    clear_input_file()
    clear_output_file()
    
    # calls the menu interface, first step
    hs_UX_menus.menu_interface(start_point=1, code=0)
    # grabs the settings
    read_input_file()
    # checks the tool and determines which one to call
    if settings["tool"] == 'subdomain_finder':
        # importlib.import_module('Saifandor').cli_entry_point()
        saifandor = importlib.import_module('saifandor')
        asyncio.run(saifandor.test())

    elif settings["tool"] == "patch_pirate":
        print(f"{yellow} [*] Notice: Patch Pirate is currently unavailable, sorry {blue}:({reset}")
        # runs patch pirate
        # patch_pirate.run()
    else:
        print(f"{red}Tool not implemented yet{reset}")

    # clears the input file and output file again in case their is any sensitive information, last step
    # NOTE: Will be uncommented when all tools have been added to the menu
    clear_input_file()
    clear_output_file()