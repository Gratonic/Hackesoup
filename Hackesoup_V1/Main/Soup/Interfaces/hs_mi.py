# :: Imports :: #

# PIP Modules
import colorama
import sys
import os
# Used to import the custom modules
import importlib

# Custom Modules
# NOTE: The custom modules must be imported this way because of the way the Python import system works

# Used to locate the custom modules
current_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(current_dir, '..', 'Lib', 'Modules')
sys.path.append(modules_dir)
# Imports the custom modules
hs_menus = importlib.import_module('hs_menus')
hs_prompts = importlib.import_module('hs_prompts')

# :: Global Variables :: #

# Colour Objects, Used For Nicer Output
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

# ::  Special Functions :: #

# Says "Goodbye!" to the user in German and exits the program
def terminate_program():
    print(f"{magenta}\n\nTschüss!{reset}")
    exit()

# :: UX Menu Interface Functions :: #

# Builds the tool/main UX menu and asks the user for their tool choice
def main_UX_menu() -> vars:
    hs_menus.call_main_menu()
    chosen_tool = hs_prompts.toolbox()
    return chosen_tool

def port_scanner_UX_menus():
    try:
        target = hs_prompts.target()
        # TODO: Fix the issue (caused by something to do with the target and setup prompt functions) that is preventing the setup prompt from being called
        # NOTE: When target is printed, it is both the ip entered and None
        hs_menus.call_port_scanner_setup_1()
        hs_prompts.setup()
    except KeyboardInterrupt:
        terminate_program()

port_scanner_UX_menus()
# Handles the entire UX menu and returns a list of all the user input
def UX_menu_interface() -> list:
    pass