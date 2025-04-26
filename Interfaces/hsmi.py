"""
# :: Author Information and Program Details :: #

File Name: hsmi.py
Author(s): Gratonic (https://github.com/Gratonic) and ibrahim-sisar (https://github.com/ibrahim-sisar) and Br0k3nPix3l (https://github.com/FailurePoint)
Written In: Python 3.10.12
Dependencie(s): sys, os, importlib, colorama
Last Modified: April 25th, 2025

# :: Description :: #

This python file is responsible for running the entire menu interface version of Hackesoup.

"""

import sys
import os
import importlib
import colorama

module_path = os.path.join(os.path.dirname(__file__), '..', 'Soup', 'Lib', 'Python_Modules')

sys.path.append(module_path)

hs_UX_menus = importlib.import_module('hs_UX_menus')

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
    # clears the input file and output file in case their is any sensitive information, last step
    clear_input_file()
    clear_output_file()

