"""
# :: Author Information and Program Details :: #

File Name: patch_pirate.py
Author(s): Gratonic (https://github.com/Gratonic) and Br0k3nPix3l (https://github.com/FailurePoint)
Written In: Python 3.10.12
Dependencie(s): halo, piratescanner, colorama, json, os
Last Modified: April 26th, 2025

# :: Description :: #

This python file is the run file for patch_pirate. All functions that are used to run patch_pirate are
stored in this python file.

"""

# :: Imports :: #

from halo import Halo # Copywrite (c) 2016-2025, Singh
import hspatchpiratescanner # Copywrite (c) 2025, Gratonic (https://github.com/Gratonic)
import colorama # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
import json
import os

# :: Global Variables

# Settings placeholder
settings = None

# Tool ouput placeholder
user_commits = None

# Repo count placeholder
repo_count = None

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

# Initializes the loading indicator
working_indicator = Halo(text=f'Searching for user commits...', spinner='pong')

# banner componets
ascii_art_tool_banner_title = """
______     _       _      ______ _           _       
| ___ \   | |     | |     | ___ (_)         | |      
| |_/ /_ _| |_ ___| |__   | |_/ /_ _ __ __ _| |_ ___ 
|  __/ _` | __/ __| '_ \  |  __/| | '__/ _` | __/ _ \\
| | | (_| | || (__| | | | | |   | | | | (_| | ||  __/
\_|  \__,_|\__\___|_| |_| \_|   |_|_|  \__,_|\__\___|"""
banner_bar = f"{yellow}___________________________________________________________/{reset}"
version = f"{green}Hackesoup Edition v1.0{reset}"

# makes the banner title colorful
banner_colors = [red, white, blue, yellow]
colorful_banner_title = ''.join(banner_colors[char % len(banner_colors)] + ascii_art_tool_banner_title[char] for char in range(len(ascii_art_tool_banner_title)))

# creates the complete banner
banner = f"{colorful_banner_title}\n{banner_bar}\n{version}"

# :: Functionality :: #

# NOTE: To test this file, the program must be run from hsmi.py. This is due to the way the file has to be -->
# imported into hsmi.py (the main program file for the menu interface version of the program)

# :: Special Functions :: #

# Says "Goodbye!" and best of luck in Croation
def exit_program_patch_pirate() -> None:
    print(f"{magenta}\nSvako dobro i doviđenja!{reset}")
    exit()

# Clears the users terminal
def clear_terminal() -> None:
    if os.name == "posix": # For Linux or MacOS
        os.system("clear")
    else:
        os.system("cls") # For Windows

# -- Input and Ouput Collection Functions -- #

# loads the JSON input data into a dictionary
def read_input_file() -> None:
    # loads the settings variable into the function for writing
    global settings

    # NOTE: This tool file is imported into hsmi.py (where the program is run from) and -->
    # the current path is acutally Hackesoup/Interfaces, not Hackesoup/Soup/Tools
    with open("../Soup/Lib/Data/Input_Data/input.json") as tool_settings:
        settings = json.load(tool_settings)

# loads the JSON output data into a dictionary
def read_output_file() -> None:
    # loads the user_commits variable into the function for writing
    global user_commits

    # NOTE: This tool file is imported into hsmi.py (where the program is run from) and -->
    # the current path is acutally Hackesoup/Interfaces, not Hackesoup/Soup/Tools
    with open("../Soup/Lib/Data/Output_Data/output.json") as tool_ouput:
        user_commits = json.load(tool_ouput)

# grabs the repo count information and stored it as a string
def read_repo_count_file() -> None:
    # loads the repo_count variable into the function for writing
    global repo_count

    # NOTE: This tool file is imported into hsmi.py (where the program is run from) and -->
    # the current path is acutally Hackesoup/Interfaces, not Hackesoup/Soup/Tools
    with open("../Soup/Lib/Data/Special_Output_Data/repo_count.txt", "r") as repo_count_file:
        repo_count = repo_count_file.readlines()[0].strip("\n")

# -- Cleanup Functions -- #

# NOTE: Most cleanup is done in hsmi.py

# clears the repo_count file
def clear_repo_count_file() -> None:
    with open("../Soup/Lib/Data/Special_Output_Data/repo_count.txt", "w") as repo_count_file:
        pass

# -- Main Functions -- #

# gets user commit and repo data, along with the email(s) and other wanted information/data
def get_user_commits() -> None:
    try:
        # starts the working indicator
        working_indicator.start()

        # scans the targeted users github and stores the output has JSON and Text files stored under ./data
        # NOTE: This function was written in rust
        hspatchpiratescanner.get_user_commits_sync()

        # stops the working indicator and makes it disappear
        working_indicator.stop()
    except KeyboardInterrupt:
        exit_program_patch_pirate()
    except:
        print(f"{red}[!] Error: Unknown{reset}")

def analyse_and_display_output() -> None:
    # used to store the non-duplicate email address(es)
    email_addresses = set()
    # used to store the obfuscated (AKA no-reply) email address
    obfuscated = ""

    # clears the terminal
    clear_terminal()

    # displays the tool banner
    print(banner)

    # calls the scanner
    get_user_commits()

    # grabs the input and output data
    read_input_file()
    read_output_file()
    read_repo_count_file()

    # gets the target info from the input data (GitHub username)
    target = settings["target"]

    # displays some simple blue text along with a gray dashed line to keep things organised
    print(f"{yellow}Results:{reset}")
    print(f"{gray}------------------------------------------------------------{reset}")
    # displays the repo count
    print(f"{blue}Found {repo_count} repositories for user {red}{target}{blue}.")

    # grabs the email information from the collected data (if any emails exist)
    try:
        for commit in user_commits:
            email = commit["email"]
            if email:
                if email.endswith("noreply.github.com"):
                    obfuscated = email
                else:
                    email_addresses.add(email)
    except:
        print(f"{red}[!] Error: Unknown{reset}")

    # adds a space to keep things organised
    print("")
    # displays the obfuscated no-reply email address (if one exists)
    print(f"{blue}Obfucated No-Aeply Address: {green}\n{obfuscated}{reset}")
    # adds a space to keep things organised
    print(" ")
    # displays the normal emails found (if any)
    print(f"{blue}Email Address(es) Found:{reset}")
    # displays all the normal emails found (if any)
    for email in email_addresses:
        print(f"{green}{email}{reset}")

# runs patch pirate
def run():
    try:
        # clears the repo count file to ensure there is no leftover data from any possible previous scan
        clear_repo_count_file()
        # runs patch pirate and displays its output
        analyse_and_display_output()
    except KeyboardInterrupt:
        exit_program_patch_pirate()
    except:
        # telling the user an error occured was causing some issues, handled in other functions anyway
        pass