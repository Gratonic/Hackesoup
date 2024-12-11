# External imports
import colorama
import os

# Colour objects, used for nicer output
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

# :: Overview :: #
"""
Generates a UX menu in a block like manner, where each block represent a piece of a page of text (the Monster).
The page is referred to as the Monster.

Elements [private objects]:

<head>
    Header portion of the page. [EX: title]
<body>
    Body portion of the page. [EX: menu_item]
<guts>
    Simple text aligned to the left of the page. [EX: setting description]
<feet>
    Footer portion of the page. [EX: warning message]

Example Usage:
    menu = Frank()
    menu.add_limb("head", text="Toolbox", title_length=10)
    menu.add_limb("body", text="XSS Vuln Scanner", menu_item_num=1)
    menu.add_limb("guts", text="XSS Vuln Scanner Description.", text_color=light_cyan)
    menu.add_limb("body", text="SQLI Vuln Scanner", menu_item_num=2)
    menu.add_limb("guts", text="SQLI Vuln Scanner Description.", text_color=light_cyan)
    menu.add_limb("feet", text="[!] Warning: This is a test UX menu!", title_length=10)
    menu.shock()
"""

# Class for creating the Monster (page of text)
class Frank():
    def __init__(self):
        # Placeholder string for the text
        self._monster = ""
        # Placeholder for the format strings
        self._head = "{border_color}{border_line}\n{text_color}{menu_title}\n{border_color}{border_line}{reset}"
        self._body = "{accent_color}{menu_item_num}) {text_color}{menu_item}{reset}"
        self._guts = "{text_color}{text}{reset}"
        self._feet = "{text_color}{space}{text}{space}\n{border_color}{border_line}{reset}"
    
    def _attach(self, element):
        self._monster = self._monster + f"{element}\n"
    
    def add_limb(self, element_type, text="Python Rocks!", menu_item_num=0, accent_color=yellow, text_color=blue, border_color=magenta, border_symbol="=", title_length=30):
        # Basic Element Type Validation
        if isinstance(element_type, str):
            pass
        else:
            raise ValueError("'element_type' must be type: str!")
        # Basic Text Value Validation
        if isinstance(text, str):
            pass
        else:
            raise ValueError("'text' must be type: str!")
        # Basic Menu Num Value Validation
        if isinstance(menu_item_num, int):
            pass
        else:
            raise ValueError("'menu_item_num' must be type: int!")
        # Basic Border Symbol Validation
        if isinstance(border_symbol, str):
            pass
        else:
            raise ValueError("'border_symbol' must be type: str!")
        # Basic Title Length Validation
        if isinstance(title_length, int):
            pass
        else:
            raise ValueError("'title_length' must be type: int!")
        
        # Creates the values list to use for the formatting
        vals = [text, menu_item_num, accent_color, text_color, border_color, border_symbol, title_length]
        # Header Element
        if element_type == "head":
            self._attach(self._head.format(
                border_color=vals[4],
                border_line=vals[5] * (vals[6] + 4),
                text_color=vals[3],
                menu_title=vals[0],
                reset=reset
            ))
        # Body Element
        elif element_type == "body":
            self._attach(self._body.format(
                accent_color=vals[2],
                menu_item_num=vals[1],
                text_color=vals[3],
                menu_item=vals[0],
                reset=reset
            ))
        # Basic Text Element
        elif element_type == "guts":
            self._attach(self._guts.format(
                text_color=vals[3],
                text=vals[0],
                reset=reset
            ))
        # Footer Element
        elif element_type == "feet":
            self._attach(self._feet.format(
                text_color=vals[3],
                space=vals[6] // 2,
                text=vals[0],
                border_color=vals[4],
                border_line=vals[5] * (vals[6] + 4),
                reset=reset
            ))
    
    # Function to draw current UX build to the output console
    def shock(self, suppress_output=False):
        # "cls" if os == windows and "clear" if os == "mac" or "linux"
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        # Draws the current state of the UX build to the output console
        if not suppress_output:
            print(self._monster)
        return self._monster

menu = Frank()
menu.add_limb("head", text="Toolbox", title_length=10)
menu.add_limb("body", text="XSS Vuln Scanner", menu_item_num=1)
menu.add_limb("guts", text="XSS Vuln Scanner Description.", text_color=light_cyan)
menu.add_limb("body", text="SQLI Vuln Scanner", menu_item_num=2)
menu.add_limb("guts", text="SQLI Vuln Scanner Description.", text_color=light_cyan)
menu.add_limb("feet", text="[!] Warning: This is a test UX menu!", title_length=10)
menu.shock()