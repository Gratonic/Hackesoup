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

from colorama import Fore # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
from datetime import datetime
import importlib
import json
import sys
import os

# :: Python Module Imports :: #

python_modules_path = os.path.join(os.path.dirname(__file__), "..", "Soup", "Lib", "Python_Modules")

sys.path.append(python_modules_path)

# menu interface module
menu_interface = importlib.import_module("menu_interface")

# :: Tool Imports :: #

tools_path = os.path.join(os.path.dirname(__file__), "..", "Soup", "Tools")
sys.path.append(tools_path)

# :: Serikandor :: #

serikandor = importlib.import_module("serikandor")

# :: PatchPirate :: #

patchpirate = importlib.import_module("patchpirate")

# :: Mudelatie :: #

mudelatie = importlib.import_module("mudelatie")

# :: Wafter :: #

wafter = importlib.import_module("wafter")

# [=== Global Variables ===] #

# placeholder for the tool output, used when the user wants to save the tool output
output = None

# [=== Functionality ===] #

if __name__ == "__main__":
    # runs the menu interface
    settings = menu_interface.run()

    # checks the tool and determines which one to call
    if settings["tool"] == "patchpirate":
        tool_output = patchpirate.run(settings=settings)
    elif settings["tool"] == "serikandor":
        tool_output = serikandor.run(settings=settings)
    elif settings["tool"] == "mudelatie":
        tool_output = mudelatie.run(settings=settings)
    elif settings["tool"] == "wafter":
        tool_output = wafter.run(settings=settings)
    else:
        print(f"{Fore.RED}[!] Alert: This tool has not implemented yet.{Fore.RESET}")

    # checks if the user chose to save the tool output, saves it if they did
    save_file_path = settings["save_file"]

    if save_file_path != None:
        with open(save_file_path, "w") as save_file:
            json.dump(obj=tool_output, fp=save_file, indent=4)
    else:
        pass