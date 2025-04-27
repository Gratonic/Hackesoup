# :: Program Information :: #

"""
Program Name: PatchPirate
Description: A brief description of what your program does.
Authors: Br0k3nPix3l (https://github.com/FailurePoint) and Gratonic (https://github.com/Gratonic)
License: MIT
Date: 4/19/2025
Version: 1.1.0
"""

# :: Imports :: #

from colorama import Fore, init # Copywrite (c) 2013-2025, Jonathan Hartley (https://github.com/tartley)
from halo import Halo # Copywrite (c) 2016-2025, Singh
import piratescanner # Copywrite (c) 2025, Gratonic (https://github.com/Gratonic)
import json
import os

# :: Global Variables :: #

username = ""

# :: Functionality :: #

# Initialize colorama with auto reset
init(autoreset=True)

# Initialize loading indicator
working_indicator = Halo(text=f'Searching user commits...', spinner='pong')

# program banner
banner = r"""
 ______                  _     ______ _                         
(_____ \        _       | |   (_____ (_)              _         
 _____) )____ _| |_ ____| |__  _____) )  ____ _____ _| |_ _____ 
|  ____(____ (_   _) ___)  _ \|  ____/ |/ ___|____ (_   _) ___ |
| |    / ___ | | |( (___| | | | |    | | |   / ___ | | |_| ____|
|_|    \_____|  \__)____)_| |_|_|    |_|_|   \_____|  \__)_____)

   BY: ┳┓  ┏┓┓ ┏┓  ┏┓•  ┏┓┓     ┏┓         • 
       ┣┫┏┓┃┫┃┏ ┫┏┓┃┃┓┓┏ ┫┃     ┃┓┏┓┏┓╋┏┓┏┓┓┏
       ┻┛┛ ┗┛┛┗┗┛┛┗┣┛┗┛┗┗┛┗ and ┗┛┛ ┗┻┗┗┛┛┗┗┗  Version: 1.1.0   
-----------------------------------------------------------------
"""

# display program banner at top of the terminal
print(f"{Fore.RED}{banner}")

def clear_data_dir():
    os.remove("./data/input_file.json")
    os.remove("./data/output_file.json")
    os.remove("./data/repo_count.txt")

def collect_user_input():
    # loads the username variable into the function because it is modified and will be used later
    global username

    # prompts the user for their target GitHub user and gives them the option to use an API token
    username = input(f"{Fore.GREEN}Enter GitHub username: ").strip()
    GITHUB_TOKEN = input(f"{Fore.YELLOW}Enter GitHub Personal Access Token (or press Enter to skip): ").strip()
    # stores the input as a dictionary so it converts nicely to JSON, GITHUB_TOKEN is null (or None in python) if one was not given
    user_input = {
        "username": username, 
        "github_token": GITHUB_TOKEN if GITHUB_TOKEN else None
    }
    # dumps the input data as JSON into a JSON input_file stored under ./data
    with open("./data/input_file.json", "w") as input_file:
        json.dump(user_input, input_file, indent=4)

def get_user_commits():
    # prints a message letting the user know that the program has began scanning
    print(f"{Fore.GREEN}Starting the scanner")

    # starts the working indicator
    working_indicator.start()
    
    # scans the targeted users github and stores the output has JSON and Text files stored under ./data
    # NOTE: This function was written in rust
    piratescanner.get_user_commits_sync()

    # stops the working indicator and makes it disappear
    working_indicator.stop()

def analyse_and_display_output():
    # opens the text repo_count file and collects the information related to the toal repository amount
    with open("./data/repo_count.txt", "r") as repo_count_file:
        repo_count = repo_count_file.readlines()[0].strip("\n")
    
    # displays the total amount of repos found
    print(f"{Fore.BLUE}Found {repo_count} repositories for user {Fore.RED}{username}{Fore.BLUE}.")

    # opens the JSON output file and collects the discovered information/data
    with open("./data/output_file.json", "r") as output_file:
        user_commits = json.load(output_file)

    # displays the total amount of commits found
    print(f"{Fore.BLUE}Total commits found: {Fore.RED}{len(user_commits)}")
    # prints a line so things look a little cleaner
    print("---------------------------------------------------------------------")

    # used to store the non-duplicate email address(es)
    email_addresses = set()
    # used to store the obfuscated (AKA no-reply) email address
    obfuscated = ""

    # attempts to display the collected information/data
    try:
        for commit in user_commits:
            email = commit["email"]
            if email:
                if email.endswith("noreply.github.com"):
                    obfuscated = email
                else:
                    email_addresses.add(email)
        
        print(f"\nObfucated noreply address: {Fore.GREEN}{obfuscated}")
        print("Email address(es) found:")
        for email in email_addresses:
            print(f"{Fore.GREEN}{email}")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")


if __name__ == "__main__":
    # clears the data directory if it has data, ignores this step if it doesn't
    try:
        clear_data_dir()
    except:
        pass
    # collects the user input and stores it as JSON under ./data
    collect_user_input()
    # runs the scanner and stores the output as JSON under ./data
    get_user_commits()
    # analyzes and displays the collected sensitive information/data
    analyse_and_display_output()