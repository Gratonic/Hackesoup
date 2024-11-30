
# imports
import json
import colorama

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
print(f"{colorama.Style.BRIGHT}Please note that this cli is {style("only", "red")} for testing and {colorama.Fore.BLACK + colorama.Back.RED} is far from fully functional!")


# TODO: everything else still!