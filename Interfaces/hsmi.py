# [=== Program Metadata ===] #

"""
# :: Author Information and Program Details :: #

File Name: hsmi.py
Author(s): Gratonic (https://github.com/Gratonic) and ibrahim-sisar (https://github.com/ibrahim-sisar) and Br0k3nPix3l (https://github.com/FailurePoint)
Written In: Python 3.10.12
Dependencie(s): colorama, datetime, importlib, asyncio, json, sys, os
Last Modified: 7/6/2025

# :: Description :: #

This python file is responsible for running the entire menu interface and tools of Hackesoup.

"""

# [=== Imports ===] #

import asyncio
import importlib
import json
import os
import sys
from datetime import datetime

from colorama import Fore # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved

# :: Python Module Imports :: #

python_modules_path = os.path.join(
    os.path.dirname(__file__), "..", "Soup", "Lib", "Python_Modules"
)

sys.path.append(python_modules_path)

# menu interface module
hs_UX_menus = importlib.import_module("hs_UX_menus")

# :: Tool Imports :: #

tools_path = os.path.join(os.path.dirname(__file__), "..", "Soup", "Tools")
sys.path.append(tools_path)

# :: Serikandor :: #

# serikandor = importlib.import_module("serikandor")
# serikandor = getattr(serikandor, "Serikandor")

# :: PatchPirate :: #

# NOTE: This tool must be rewritten because it only works on Linux Mint 21 (not even Linux Mint 22)

# [=== Global Variables ===] #

# placeholder for the tool settings, just need to get the tool chosen
settings = None

# placeholder for the tool output, used when the user wants to save the tool output
output = None

# [=== Special Functions ===] #


def clear_input_file() -> None:
    lines = ["{\n", "    \n", "}\n"]
    # recreates the file
    with open("../Soup/Lib/Data/Input_Data/input.json", "w") as input_file:
        """
        something must be written to the file with the correct syntax, otherwise the computer
        will not acknowledge the files existence, despite it existing physically on the HDD/SSD
        """
        # something must be written to the file with the correct syntax, otherwise the computer ->
        # not
        input_file.writelines(lines)


def clear_output_file() -> None:
    lines = ["{\n", "    \n", "}\n"]
    # recreates the input file in order to clear it
    with open("../Soup/Lib/Data/Output_Data/output.json", "w") as output_file:
        """
        something must be written to the file with the correct syntax, otherwise the computer
        will not acknowledge the files existence, despite it existing physically on the HDD/SSD
        """
        output_file.writelines(lines)


def read_input_file() -> None:
    global settings
    with open("../Soup/Lib/Data/Input_Data/input.json", "r") as settings_file:
        settings = json.load(settings_file)


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
    formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")
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
    if settings["tool"] == "serikandor":
        pass
    elif settings["tool"] == "patchpirate":
        print(
            f"{Fore.RED} [!] Alert: Patch Pirate is currently unavailable. {Fore.BLUE}:({Fore.RESET}"
        )
    else:
        print(f"{Fore.RED}[!] Alert: Tool not implemented yet.{Fore.RESET}")

    if settings["save_file"] == True:
        save_output_to_file()
    else:
        pass

    # clears the input and output files for the next time the suite is run
    clear_input_file()
    clear_output_file()
