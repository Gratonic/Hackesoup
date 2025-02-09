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

import hs_menus
import hs_prompts

# :: Global Variables :: #

current_tool_menu = 1

# :: Functionality :: #

# Main UX Menu
def main_UX_menu():
    hs_menus.main_menu()

# Tool UX Menu Packs
def port_scanner_UX_menu():
    pass

def sub_domain_finder_UX_menu():
    pass

def xss_scanner_UX_menu():
    pass

def dir_traversal_UX_menu():
    pass

def sqli_scanner_UX_menu():
    pass

def destroyer_UX_menu():
    pass