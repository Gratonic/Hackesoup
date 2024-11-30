
# imports
import json
import colorama
import inspect
import hs_menus



banner = """
 ▄ .▄ ▄▄▄·  ▄▄· ▄ •▄ ▄▄▄ ..▄▄ ·       ▄• ▄▌ ▄▄▄·
██▪▐█▐█ ▀█ ▐█ ▌▪█▌▄▌▪▀▄.▀·▐█ ▀. ▪     █▪██▌▐█ ▄█
██▀▐█▄█▀▀█ ██ ▄▄▐▀▀▄·▐▀▀▪▄▄▀▀▀█▄ ▄█▀▄ █▌▐█▌ ██▀·
██▌▐▀▐█ ▪▐▌▐███▌▐█.█▌▐█▄▄▌▐█▄▪▐█▐█▌.▐▌▐█▄█▌▐█▪·•
▀▀▀ · ▀  ▀ ·▀▀▀ ·▀  ▀ ▀▀▀  ▀▀▀▀  ▀█▄▀▪ ▀▀▀ .▀   """

# define vesion and project info for reference during development.
# TODO: move to a global variables location in .lib
_hackesoup_info_ = json.loads('''{
    "version": "v1.0.0-dev",
    "codename": "Unknown",
    "release-date": "NA",
    "author": "<up to you if you want to include me.>"                              
}''')

# tool for sylizing only a few words out of a fstring
# TODO: move to a global module in .lib
def style(text, color):
    text_color = color.upper()
    return f"{getattr(colorama.Fore, text_color)}{text}{colorama.Fore.RESET}"

# print out acsii banner in colorfully distracting splendor (it's to cute to be dangerous...)
colorama.init()
rainbow_colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN, colorama.Fore.CYAN, colorama.Fore.BLUE, colorama.Fore.MAGENTA]
rainbow_text = ''.join(rainbow_colors[i % len(rainbow_colors)] + banner[i] for i in range(len(banner)))
print(rainbow_text + colorama.Fore.RESET)

# print out version info and dev warning
print(f"{colorama.Style.BRIGHT}{colorama.Fore.LIGHTBLACK_EX}Hackesoup {_hackesoup_info_['version']}({_hackesoup_info_['codename']})\nWelcome!" + colorama.Fore.RESET)
print(f"{colorama.Style.BRIGHT}Please note that this cli is {style("only", "red")} for testing and {colorama.Fore.BLACK + colorama.Back.RED} is far from fully functional!{colorama.Back.RESET}")
print(f"{colorama.Style.BRIGHT}{colorama.Fore.LIGHTBLACK_EX}Current Utils list:")

# Get a list of functions present in hs_menus
functions = inspect.getmembers(hs_menus, inspect.isfunction)

# Build a list if avalible tools from functions in hs_menus (skipping internal functions starting with "_")
for i, (func_name, _) in enumerate(functions, start=1):
        if not str(func_name).startswith("_"):
            print(f"{colorama.Fore.YELLOW}({i}) {colorama.Fore.LIGHTBLACK_EX}{func_name}")

# Handle triggering hs_menus function from user input.
# TODO: replace index system with something more reliable. Internal "_" functions may skew menu triggers?
x = input(f"{colorama.Fore.LIGHTBLACK_EX}Enter the {style("number", "yellow")} {colorama.Fore.LIGHTBLACK_EX}for your tool:")
function_name, function = functions[int(x) - 1]
function()