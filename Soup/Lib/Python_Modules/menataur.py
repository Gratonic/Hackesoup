"""
# :: Author Information and Program Details :: #

File Name: menataur.py
Author(s): Gratonic (https://github.com/Gratonic) and FailurePoint (https://github.com/FailurePoint)
Written In: Python 3.12.3
Dependencie(s): colorama
Last Modified: October 3, 2025

# :: Description :: #

This module is used to build the actual menu portion of the UX menus, by that I mean everything except for the input field. In order to
make things easy to understand, here is the purpose of each function...

<-- Special Functions --->

validate_foreground_color(): used to validate the foreground colors provided for menu construction and retrieve their escape strings
validate_background_color(): used to validate the background colors provided for menu construction and retrieve their escape strings

<--- Main Functions/Methods -->

add_header(): adds the top portion of the menu (the colorful ASCII art title, OS support information, etc.)
add_description(): adds a description to the menu (the blue text located above each menu option)
add_option(): adds an option to the menu (the magenta/gray text with a yellow/gray numerical label to the left of it)

display(): displays the constructed menu

construct_menu(): used with menu_data.py to construct an entire menu

# :: Example Usage :: #

# Import the module
import minotaur

# Create an instance of Menataur (the menu constructor class)
menu = menataur.Menataur()

# Define the menu elements
ascii_art_title =
___  ___                 _                   
|  \/  |                | |                  
| .  . | ___ _ __   __ _| |_ __ _ _   _ _ __ 
| |\/| |/ _ \ '_ \ / _` | __/ _` | | | | '__|
| |  | |  __/ | | | (_| | || (_| | |_| | |   
\_|  |_/\___|_| |_|\__,_|\__\__,_|\__,_|_|   

small_title = "Minotaur"
title_colors = ["red", "white", "blue"]
title_bar = "_______________________________________________________________________________________/"
program_version_color = "green"
program_version_num = "1.0"
os_support_message_color = "yellow"
os_support_highlight_color = "light_green"
os_support_color = "light_cyan"
os_support_info = ["Windows", "Linux", "MacOS"]

# Add the menu header
menu.add_header(
    ascii_art_title=ascii_art_title,
    small_title=small_title,
    title_colors=title_colors,
    title_bar=title_bar,
    program_version_color=program_version_color,
    program_version_num=program_version_num,
    os_support_message_color=os_support_message_color,
    os_support_highlight_color=os_support_highlight_color,
    os_support_color=os_support_color,
    os_support_info=os_support_info
)

# Add the menu descriptions and options
menu.add_description(text_color="grey", text="Have some fun at a party")
menu.add_option(accent_color="magenta", menu_option_number=1, menu_option_color="light_cyan", menu_option="Party")

menu.add_description(text_color="grey", text="Drink way too much")
menu.add_option(accent_color="magenta", menu_option_number=2, menu_option_color="light_cyan", menu_option="Get Drunk")

menu.add_description(text_color="grey", text="Go to bed and sleep")
menu.add_option(accent_color="magenta", menu_option_number=3, menu_option_color="light_cyan", menu_option="Sleep")

menu.add_description(text_color="grey", text="All three")
menu.add_option(accent_color="magenta", menu_option_number=4, menu_option_color="light_cyan", menu_option="The Works")

# Display the menu
menu.display()
"""

# [=== Imports ===] #

from itertools import zip_longest
from colorama import Fore, Back # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
import menu_data
import utils
import os

# [=== Special Functions ===] #

def clear_terminal():
    # Check the operating system and clear the terminal
    if os.name == 'posix':
        # For Unix-like systems (Linux, macOS)
        os.system('clear')
    else:
        # For Windows
        os.system('cls')

def exit_program() -> None:
    utils.exit_program(tool_name="hackesoup")

def validate_foreground_color(fore_color: str) -> str:
    foreground_colors = {
        "blue": Fore.BLUE, "light_blue": Fore.LIGHTBLUE_EX, 
        "cyan": Fore.CYAN, "light_cyan": Fore.LIGHTCYAN_EX,
        "red": Fore.RED, "light_red": Fore.LIGHTRED_EX,
        "green": Fore.GREEN, "light_green": Fore.LIGHTGREEN_EX, 
        "yellow": Fore.YELLOW, "light_yellow": Fore.LIGHTYELLOW_EX,
        "magenta": Fore.MAGENTA, "light_magenta": Fore.LIGHTMAGENTA_EX,
        "black": Fore.BLACK, "white": Fore.WHITE, "grey": Fore.LIGHTBLACK_EX
    }

    color = fore_color.lower()
    if color in foreground_colors:
        return foreground_colors[color]
    else:
        print(f"{Fore.RED}[!] Minotaur Error: One or more foreground colors are invalid or unsupported.{Fore.RESET}")
        print(f"{Fore.GREEN}The following foreground colors are supported:{Fore.RESET}")
        for color_str in foreground_colors.keys():
            print(f"{Fore.BLUE}{color_str}{Fore.RESET}")
        raise ValueError("Invalid color provided.")

def validate_background_color(back_color: str) -> str:
    background_colors = {
        "blue": Back.BLUE, "light_blue": Back.LIGHTBLUE_EX, 
        "cyan": Back.CYAN, "light_cyan": Back.LIGHTCYAN_EX,
        "red": Back.RED, "light_red": Back.LIGHTRED_EX,
        "green": Back.GREEN, "light_green": Back.LIGHTGREEN_EX, 
        "yellow": Back.YELLOW, "light_yellow": Back.LIGHTYELLOW_EX,
        "magenta": Back.MAGENTA, "light_magenta": Back.LIGHTMAGENTA_EX,
        "black": Back.BLACK, "white": Back.WHITE, "grey": Back.LIGHTBLACK_EX
    }

    color = back_color.lower()
    if color in background_colors:
        return background_colors[color]
    else:
        print(f"{Fore.RED}[!] Minotaur Error: One or more background colors are invalid or unsupported.{Fore.RESET}")
        print(f"{Fore.GREEN}The following background colors are supported:{Fore.RESET}")
        for color_str in background_colors.keys():
            print(f"{Fore.BLUE}{color_str}{Fore.RESET}")
        raise ValueError("Invalid color provided.")

# [=== Functionality ===] #

class Menataur():
    def __init__(self):
        # Format Strings
        self._menu = ""
        self._header = "{ascii_art_title}\n{title_bar}\n{program_version_color}{small_title} v{program_version_num}\n{os_support_message}\n{reset}"
        self._body = "{accent_color}{menu_option_number}) {menu_option_color}{menu_option}{reset}"
        self._paragraph = "{text_color}{text}{reset}"
        self._footer = "{text_color}{text}{reset}"
    
    # Formally adds an element to the menu interface
    def _include(self, menu_element) -> None:
        self._menu = self._menu + f"{menu_element}\n"
    
    def add_header(self, ascii_art_title: str, small_title: str, title_colors: list, title_bar: str, program_version_color: str, program_version_num: str, os_support_back_color: str, os_support_fore_color: str, os_support_info: list) -> None:
        # validates the title colors, retrives their escape strings, and then uses them with the ascii art title to create a colorful version of the ascii title
        validated_title_colors = [validate_foreground_color(fore_color=color) for color in title_colors]
        colorful_title = "".join(validated_title_colors[char % len(validated_title_colors)] + ascii_art_title[char] for char in range(len(ascii_art_title)))

        title_bar = f"{Fore.RESET}{title_bar}"

        # validates the colots, retrieves their escape string, and then builds an OS support message with them
        os_support_fore_color = validate_foreground_color(fore_color=os_support_fore_color)
        os_support_back_color = validate_background_color(back_color=os_support_back_color)
        os_support_message = f"{os_support_fore_color}This Program Supports:"
        
        for os in os_support_info:
            if os != os_support_info[-1]:
                os_support_message = os_support_message + f" {os_support_back_color}{os}{Back.RESET},"
            else:
                os_support_message = os_support_message + f" {os_support_back_color}{os}{Back.RESET}"
        
        self._include(menu_element=self._header.format(
            ascii_art_title=colorful_title,
            small_title=small_title,
            title_bar=title_bar,
            program_version_color=validate_foreground_color(fore_color=program_version_color),
            program_version_num=program_version_num,
            os_support_message=os_support_message,
            reset=Fore.RESET
        ))
    
    def add_description(self, text_color: str, text: str) -> None:
        self._include(menu_element=self._paragraph.format(
            text_color=validate_foreground_color(fore_color=text_color),
            text=text,
            reset=Fore.RESET
        ))
    
    def add_option(self, accent_color: str, menu_option_number: int, menu_option_color: str, menu_option: str) -> None:
        self._include(menu_element=self._body.format(
            accent_color=validate_foreground_color(fore_color=accent_color),
            menu_option_number=menu_option_number,
            menu_option_color=validate_foreground_color(fore_color=menu_option_color),
            menu_option=menu_option,
            reset=Fore.RESET
        ))
    
    def display(self) -> None:
        print(self._menu)

# creates and returns a menu
def construct_menu(menu_func_name: str) -> object:
    menu_func = getattr(menu_data, menu_func_name)
    menu_contents = menu_func()

    ascii_title = menu_contents["ascii_title"]
    title_colors = menu_contents["title_colors"]

    title_bar = menu_contents["title_bar"]

    small_title = menu_contents["small_title"]
    tool_version = menu_contents["tool_version"]

    meds = menu_contents["descriptions"]
    mops = menu_contents["options"]


    # initalizes the menu
    menu = Menataur()

    # if there are no descriptions there is no options either
    if meds["1"] != None:
        # menu options and descriptions
        menu_descriptions = list(meds.values())
        menu_opts = list(mops.values())

        # constructs the menu header (title, program support info, etc.)
        menu.add_header(
            ascii_art_title=ascii_title,
            title_bar=title_bar,
            title_colors = title_colors,
            small_title=small_title,
            program_version_color = "green",
            program_version_num = tool_version,
            os_support_back_color = "yellow",
            os_support_fore_color = "magenta",
            os_support_info = ["Linux", "MacOS"]
        )

        # adds the exit option to the menu
        menu.add_option(
        accent_color="grey", 
        menu_option_number=0, 
        menu_option_color="grey", 
        menu_option="Exit"
        )

        last_option = 1

        # constructs the main portion of the menu (options with their descriptions)
        for description, option in zip_longest(menu_descriptions, menu_opts):
            menu.add_description(
                text_color="blue",
                text=description
            )

            menu.add_option(
                accent_color="yellow",
                menu_option_number=last_option,
                menu_option_color="magenta",
                menu_option=option
            )

            # increments the option number by one
            last_option += 1


        # adds the previous menu option to the menu
        menu.add_option(
        accent_color="grey", 
        menu_option_number=last_option, 
        menu_option_color="grey", 
        menu_option="Previous Menu"
        )
    else:
        # constructs the menu header (title, program support info, etc.)
        menu.add_header(
            ascii_art_title=ascii_title,
            title_bar=title_bar,
            title_colors = title_colors,
            small_title=small_title,
            program_version_color = "green",
            program_version_num = tool_version,
            os_support_back_color = "yellow",
            os_support_fore_color = "magenta",
            os_support_info = ["Linux"]
        )

    return menu

def floppy_disk_heaven_easter_egg():
        clear_terminal()

        floppy_party = menu_data.floppy_disk_heaven_easter_egg()

        colors = [Fore.RED, Fore.WHITE, Fore.BLUE]
        colorful_floppy_party = ''.join(colors[char % len(colors)] + floppy_party[char] for char in range(len(floppy_party)))

        print(colorful_floppy_party)

        exit_program()