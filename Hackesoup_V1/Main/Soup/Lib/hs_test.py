
# imports
import json
import colorama
import inspect
import os

banner = """
                                                                            
    //    / /                                                                       
   //___ / / ____     ____     //___      ____    _____     ______            ______    
  / ___   / //   ) ) //   ) ) //\ \     //___))  ( (  ) )  //   ) ) //   / / //   ) ) 
 //    / / //   / / //       //  \ \   //         \ \     //   / / //   / / //___/ /  
//    / / ((___( ( ((____   //    \ \ ((____   //__) )   ((___/ / ((___( ( //"""

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


# Clear the terminal to make the output prettier
os.system("clear")

# Print out acsii banner in colorfully distracting splendor (it's to cute to be dangerous...)
colorama.init()
rainbow_colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN, colorama.Fore.CYAN, colorama.Fore.BLUE, colorama.Fore.MAGENTA]
rainbow_text = ''.join(rainbow_colors[i % len(rainbow_colors)] + banner[i] for i in range(len(banner)))
print(rainbow_text + colorama.Fore.RESET)

# Print out Banner scoop bar - will be integrated at a more advanced level
print(f"{colorama.Style.BRIGHT}{colorama.Fore.LIGHTGREEN_EX}____________________________________________________________________________________/")

# Print out version info and dev warning - might be needed but not at the moment
print(f"{colorama.Style.BRIGHT}{colorama.Fore.LIGHTBLACK_EX}Hackesoup {_hackesoup_info_['version']}({_hackesoup_info_['codename']})" + colorama.Fore.RESET)
print(f"{colorama.Style.BRIGHT}Please note that this cli is {style('only', 'red')} for testing and {colorama.Fore.BLACK + colorama.Back.RED} is far from fully functional!{colorama.Back.RESET}")
print(f"{colorama.Style.BRIGHT}{colorama.Fore.LIGHTBLACK_EX}Current Utils list:")

# Get a list of functions present in hs_menus - no longer needed
functions = inspect.getmembers("menu_options_here", inspect.isfunction)

# Prints a function's name beside a number for every function in a list - no longer needed
for func_num, (func_name, _) in enumerate(functions, start=1):
        if not str(func_name).startswith("_"):
            print(f"{colorama.Fore.YELLOW}({func_num}) {colorama.Fore.LIGHTBLACK_EX}{func_name}")


# Handle triggering hs_menus function from user input.
# TODO: replace index system with something more reliable. Internal "_" functions may skew menu triggers?
x = input(f"{colorama.Fore.LIGHTBLACK_EX}Enter the {style('number', 'yellow')} {colorama.Fore.LIGHTBLACK_EX}for your tool:")
function_name, function = functions[int(x) - 1]

# Clear the terminal and switch to the new menu (trigger the fuction)
os.system("clear")
function()