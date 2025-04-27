"""
# :: Author Information and Program Details :: #

File Name: hsmi.py
Author(s): Gratonic (https://github.com/Gratonic) and ibrahim-sisar (https://github.com/ibrahim-sisar) and Br0k3nPix3l (https://github.com/FailurePoint)
Written In: Python 3.10.12
Dependencie(s): sys, os, importlib, colorama
Last Modified: April 26th, 2025

# :: Description :: #

This python file is responsible for running the entire menu interface version of Hackesoup.

"""

# :: Imports :: #

import sys
import os
import importlib
import colorama # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved


# -- Python Module Imports -- #

python_modules_path = os.path.join(os.path.dirname(__file__), '..', 'Soup', 'Lib', 'Python_Modules')

sys.path.append(python_modules_path)

# menu interface module
hs_UX_menus = importlib.import_module('hs_UX_menus')

# -- Tool Imports -- #

tools_path = os.path.join(os.path.dirname(__file__), '..', 'Soup', 'Tools')
sys.path.append(tools_path)

# patch_pirate_module
patch_pirate = importlib.import_module('patch_pirate')

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


# clears the input JSON file
def clear_input_file():
    # recreates the file
    with open("../Soup/Lib/Data/Input_Data/input.json", "w"):
        pass

def clear_output_file():
    # recreates the file
    with open("../Soup/Lib/Data/Output_Data/output.json", "w"):
        pass



if __name__ == "__main__":
    # calls the menu interface, first step
    hs_UX_menus.menu_interface(start_point=1, code=0)
    # runs patch pirate
    patch_pirate.run()
    # clears the input file and output file in case their is any sensitive information, last step
    # NOTE: Will be uncommented when all tools have been added to the menu
    # clear_input_file()
    # clear_output_file()

