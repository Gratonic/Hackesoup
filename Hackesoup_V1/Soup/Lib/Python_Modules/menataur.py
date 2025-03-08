"""
# :: Author Information and Program Details :: #

File Name: menataur.py
Author(s): Gratonic (https://github.com/Gratonic), FailurePoint (https://github.com/FailurePoint)
Written In: Python 3.10.12
Dependencie(s): colorama
Last Modified: February 7th, 2025

# :: Description :: #

This Python file contains the code used to buid the menu interface menu's utilizing the colorama module. The add_header() function
is used to build the header portion of a menu (ASCII Art Title, OS Support Information, etc.). The add_body() function is used to
add a menu option to the menu. The add_paragraph() function is used to add a description to the menu. The add_footer()
function is used to add a sentence/description at a desired location on the menu (likely the bottom) with padding. The color
validation function are used to validate the colors passed to the function by checking the given color or colors against a 
dictionary of the colors supported by the program and then set the color to the chosen colors actual value. When add_header(),
add_body(), add_paragraph(), and_footer() are called, the parameters are used to format place holder strings which are then added
to the _placeholder format string (the actual menu) with the _include() function, which is responsible for tacking the pieces
of the menu onto the menu. Think of this program like a lego project, each piece of the menu is like a lego structure and the
pieces of that lego structure are the configuration settings for that lego structure, and think of the _include() function as the
function that attaches that lego structure to the lego project. Alternatively, you can think of it sort of like a webpage written
in just HTML and CSS.

# :: Example Usage :: #

# Imports the module
import minotaur

# Creates an instance of Minotaur (the menu class)
menu = menataur.Menataur()

# Define the elements for the menu
ascii_art_title = r\"""
 _______ _________ _        _______ _________ _______           _______ 
(       )\__   __/( (    /|(  ___  )\__   __/(  ___  )|\     /|(  ____ )
| () () |   ) (   |  \  ( || (   ) |   ) (   | (   ) || )   ( || (    )|
| || || |   | |   |   \ | || |   | |   | |   | (___) || |   | || (____)|
| |(_)| |   | |   | (\ \) || |   | |   | |   |  ___  || |   | ||     __)
| |   | |   | |   | | \   || |   | |   | |   | (   ) || |   | || (\ (   
| )   ( |___) (___| )  \  || (___) |   | |   | )   ( || (___) || ) \ \__
|/     \|\_______/|/    )_)(_______)   )_(   |/     \|(_______)|/   \__/
\"""
small_title = "Minotaur"
title_colors = ["red", "white", "blue"]
title_bar = "_______________________________________________________________________________________/"
program_version_color = "green"
program_version_num = "1.0"
os_support_message_color = "yellow"
os_support_highlight_color = "light_green"
os_support_color = "light_cyan"
os_support_info = ["Windows", "Linux", "MacOS"]

# Add the header to the menu
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

# Add body elements (menu options)
menu.add_paragraph(text_color="grey", text="Have some fun at a party")
menu.add_body(accent_color="magenta", menu_option_number=1, menu_option_color="light_cyan", menu_option="Party")
menu.add_paragraph(text_color="grey", text="Drink way too much")
menu.add_body(accent_color="magenta", menu_option_number=2, menu_option_color="light_cyan", menu_option="Get Drunk")
menu.add_paragraph(text_color="grey", text="Go to bed and sleep")
menu.add_body(accent_color="magenta", menu_option_number=3, menu_option_color="light_cyan", menu_option="Sleep")
menu.add_paragraph(text_color="grey", text="All three")
menu.add_body(accent_color="magenta", menu_option_number=4, menu_option_color="light_cyan", menu_option="The Works")

# Add a footer (thank you message)
menu.add_footer(text_color="light_yellow", text="Thank you for using Minotaur!")

# Completes and calls the menu
menu.execute()
"""

# :: Imports :: #

import colorama # Colorama - Copyright (c) 2013-2023, Anthony Sottile, All Rights Reserved

# :: Global Variables :: #

# Color objects, used for nicer output
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
grey = colorama.Fore.LIGHTBLACK_EX
black = colorama.Fore.BLACK

# Used to reset the highlight color
highlight_reset = colorama.Back.RESET

# Used to check the provided colors
supported_colors = {
    "blue": blue, "light_blue": light_blue, 
    "cyan": cyan, "light_cyan": light_cyan,
    "red": red, "light_red": light_red,
    "green": green, "light_green": light_green, 
    "yellow": yellow, "light_yellow": light_yellow,
    "magenta": magenta, "light_magenta": light_magenta,
    "black": black, "white": white, "grey": grey
}

# Validates the colors provided by the user
def validate_color(color: str) -> str:
    color = color.lower()
    if color in supported_colors:
        return supported_colors[color]
    else:
        print(f"{red}[!] Minotaur Error: {light_red}One or more color(s) is/are not valid or is/are unsupported.{reset}")
        print(f"{green}The following colors are supported:{reset}")
        for color_str in supported_colors.keys():
            print(f"{blue}{color_str}{reset}")
        raise ValueError("Invalid color provided.")

# Validates the higlight color provided by the user
def validate_highlight_color(high_color: str) -> str:
        if high_color.lower() in supported_colors and high_color == "blue":
            high_color = colorama.Back.BLUE
            return high_color
        elif high_color.lower() in supported_colors and high_color == "light_blue":
            high_color = colorama.Back.LIGHTBLUE_EX
            return high_color
        elif high_color.lower() in supported_colors and high_color == "cyan":
            high_color = colorama.Back.CYAN
            return high_color
        elif high_color.lower() in supported_colors and high_color == "light_cyan":
            high_color = colorama.Back.LIGHTCYAN_EX
            return high_color
        elif high_color.lower() in supported_colors and high_color == "red":
            high_color = colorama.Back.RED
            return high_color
        elif high_color.lower() in supported_colors and high_color == "light_red":
            high_color = colorama.Back.LIGHTRED_EX
            return high_color
        elif high_color.lower() in supported_colors and high_color == "green":
            high_color = colorama.Back.GREEN
            return high_color
        elif high_color.lower() in supported_colors and high_color == "light_green":
            high_color = colorama.Back.LIGHTGREEN_EX
            return high_color
        elif high_color.lower() in supported_colors and high_color == "yellow":
            high_color = colorama.Back.YELLOW
            return high_color
        elif high_color.lower() in supported_colors and high_color == "light_yellow":
            high_color = colorama.Back.LIGHTYELLOW_EX
            return high_color
        elif high_color.lower() in supported_colors and high_color == "magenta":
            high_color = colorama.Back.MAGENTA
            return high_color
        elif high_color.lower() in supported_colors and high_color == "light_magenta":
            high_color = colorama.Back.LIGHTMAGENTA_EX
            return high_color
        elif high_color.lower() in supported_colors and high_color == "white":
            high_color = colorama.Back.WHITE
            return high_color
        elif high_color.lower() in supported_colors and high_color == "black":
            high_color = colorama.Back.BLACK
            return high_color
        elif high_color.lower() in supported_colors and high_color == "grey":
            high_color = colorama.Back.LIGHTBLACK_EX
            return high_color
        else:
            print(f"{red}[!] Minotaur Error (line 79): {yellow}{high_color}{highlight_reset} {light_red} is not a valid color or is unsupported.{reset}")
            print(f"{green}The following colors are supported:{reset}")
            for color_str in supported_colors:
                print(f"{blue}{color_str}{reset}")
            exit()

# Menu Builder Class
class Menataur():
    def __init__(self):
        # Format Strings
        self._placeholder = ""
        self._header = "{ascii_art_title}\n{title_bar}\n{program_version_color}{small_title} v{program_version_num}\n{os_support_message}{reset}"
        self._body = "{accent_color}{menu_option_number}) {menu_option_color}{menu_option}{reset}"
        self._paragraph = "{text_color}{text}{reset}"
        self._footer = "{text_color}{text}{reset}"
    # Formally adds an element to the menu interface
    def _include(self, element):
        self._placeholder = self._placeholder + f"{element}\n"
    # Adds a header element (title, os support info, etc.) to the menu interface
    def add_header(self, ascii_art_title: str, small_title: str, title_colors: list, title_bar: str, program_version_color: str, program_version_num: str, os_support_message_color: str, os_support_highlight_color: str, os_support_color: str, os_support_info: list) -> None:
        # Validates the colors in the title colors list and gets the real color if they are valid
        validated_title_colors = [validate_color(color) for color in title_colors]
        # Creates a colorful title using the provided ascii_art_title and title colors
        colorful_title = ''.join(validated_title_colors[char % len(validated_title_colors)] + ascii_art_title[char] for char in range(len(ascii_art_title)))
        # Validates the os_support_color
        os_support_color = validate_color(os_support_color)
        # Validates the os_support_highlight_color and sets its value
        os_support_highlight_color = validate_highlight_color(os_support_highlight_color)
        # Creates the os support message using the os support info list, os support highlight color, and os_support_color
        os_support_message = f"{os_support_color}This Program Supports:"
        
        for os in os_support_info:
            if os != os_support_info[-1]:
                os_support_message = os_support_message + f" {os_support_highlight_color}{os}{highlight_reset},"
            else:
                os_support_message = os_support_message + f" {os_support_highlight_color}{os}{highlight_reset}"
        
        self._include(self._header.format(
            ascii_art_title=colorful_title,
            small_title=small_title,
            title_bar=title_bar,
            program_version_color=validate_color(program_version_color),
            program_version_num=program_version_num,
            os_support_message=os_support_message,
            reset=reset
        ))
    # Adds a body element (menu option) to the menu interface
    def add_body(self, accent_color: str, menu_option_number: int, menu_option_color: str, menu_option: str) -> None:
        self._include(self._body.format(
            accent_color=validate_color(accent_color),
            menu_option_number=menu_option_number,
            menu_option_color=validate_color(menu_option_color),
            menu_option=menu_option,
            reset=reset
        ))
    # Adds a paragraph (description) to the menu interface
    def add_paragraph(self, text_color: str, text: str, title_width=5) -> None:
        self._include(self._paragraph.format(
            text_color=validate_color(text_color),
            text=text,
            reset=reset
        ))
    # Adds a footer element (thank you or warning message) to the menu interface
    def add_footer(self, text_color: str, text: str, title_width=5) -> None:
        if not isinstance(title_width, int):
            print(f"{red}[!] Minotaur Error: {yellow}title_width {light_red}must be type: {yellow}int{reset}")
            raise ValueError("title_width must be an integer.")
        
        text = f"{' ' * (title_width // 2)}{text}{' ' * (title_width // 2)}"
        self._include(self._paragraph.format(
            text_color=validate_color(text_color),
            text=text,
            reset=reset
        ))
    # Finishes the UX menu, displays it, and returns the users choice
    def execute(self) -> None:
        # Prints the main portion of the menu
        print(self._placeholder)