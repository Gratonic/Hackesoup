"""
# :: Author Information and Program Details :: #

File Name: patch_pirate.py
Author(s): Br0k3nPix3l (https://github.com/FailurePoint) and Gratonic (https://github.com/Gratonic)
Written In: Python 3.10.12
Dependencie(s): halo, piratescanner, colorama, json, os
Last Modified: April 26th, 2025

# :: Description :: #

This python file is the run file for patch_pirate. All functions that are used to run patch_pirate are
stored in this python file.

"""

# [=== Imports ===] #

from datetime import datetime
from colorama import Fore, init
from halo import Halo
import requests
import hashlib
import os

# [=== Global Variables ===] #

# Settings placeholder
settings = None

# Tool ouput placeholder
user_commits = None

# Repo count placeholder
repo_count = None

# Initializes the loading indicator
working_indicator = Halo(text=f'Searching for user commits...', spinner='pong')

# banner componets
ascii_art_title = """
______     _       _     ______ _           _       
| ___ \   | |     | |    | ___ (_)         | |      
| |_/ /_ _| |_ ___| |__  | |_/ /_ _ __ __ _| |_ ___ 
|  __/ _` | __/ __| '_ \ |  __/| | '__/ _` | __/ _ \\
| | | (_| | || (__| | | || |   | | | | (_| | ||  __/
\_|  \__,_|\__\___|_| |_|\_|   |_|_|  \__,_|\__\___|"""
banner_bar = f"{Fore.YELLOW}___________________________________________________________/{Fore.RESET}"
version = f"{Fore.GREEN}PatchPirate Hackesoup Edition v1.0{Fore.RESET}"

# makes the banner title colorful
banner_colors = [Fore.RED, Fore.WHITE, Fore.BLUE, Fore.YELLOW]
colorful_ascii_art_title = ''.join(banner_colors[char % len(banner_colors)] + ascii_art_title[char] for char in range(len(ascii_art_title)))

# creates the complete banner
banner = f"{colorful_ascii_art_title}\n{banner_bar}\n{version}"

# initialize loading indicator
working_indicator = Halo(text=f'Searching user commits...', spinner='pong')

# [=== Special Functions ===] #

def exit_program() -> None:
    print("\n")
    print(f"{Fore.MAGENTA}\n\nSvako dobro i doviđenja!{Fore.RESET}")
    exit()
# Clears the users terminal
def clear_terminal() -> None:
    if os.name == "posix": # For Linux or MacOS
        os.system("clear")
    else:
        os.system("cls") # For Windows

# [=== Functionality ===] #

# turns on auto reset for the colorama colors
init(autoreset=True)

def handle_rate_limit(response) -> None:
    reset_timestamp = int(response.headers.get('X-RateLimit-Reset', 0))
    reset_time = datetime.fromtimestamp(reset_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    remaining = response.headers.get('X-RateLimit-Remaining', '0')
    print(f"\n{Fore.RED}GitHub API rate limit exceeded.")
    print(f"{Fore.YELLOW}Remaining requests: {remaining}")
    print(f"{Fore.YELLOW}Rate limit resets at: {Fore.CYAN}{reset_time}")
    raise Exception("Rate limit hit. Please wait for cooldown or use a personal access token.")

def get_user_commits(settings: dict) -> list:
    username = settings["target"]
    github_token = settings["API_token"]

    headers = {"Authorization": f"token {github_token}"} if github_token else {}

    commits = []
    repos = []

    working_indicator.start()

    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 403:
                handle_rate_limit(response)
            elif response.status_code != 200:
                raise Exception(f"Error fetching repos: {response.status_code}")
        except requests.Timeout:
            print(f"{Fore.RED}[!] Error: The GitHub API request timed out.")
        except requests.ConnectionError:
            print(f"{Fore.RED}[!] Error: Failed to connect to GitHub.")
        except KeyboardInterrupt:
            exit_program()

        data = response.json()
        if not data:
            break

        repos.extend(data)
        page += 1

    working_indicator.stop()

    print(f"{Fore.BLUE}Found {len(repos)} repositories for user {Fore.RED}{username}{Fore.BLUE}.")

    working_indicator.start()

    for repo in repos:
        repo_name = repo['name']
        owner = repo['owner']['login']

        page = 1
        while True:
            url = f"https://api.github.com/repos/{owner}/{repo_name}/commits?author={username}&page={page}&per_page=100"
            
            try:
                response = requests.get(url, headers=headers, timeout=30)
                if response.status_code == 403:
                    working_indicator.stop()
                    handle_rate_limit(response)
                elif response.status_code != 200:
                    break
            except requests.Timeout:
                print(f"{Fore.RED}[!] Error: The GitHub API request timed out.")
            except requests.ConnectionError:
                print(f"{Fore.RED}[!] Error: Failed to connect to GitHub.")
            except KeyboardInterrupt:
                exit_program()
            except Exception as e:
                print(f"{Fore.RED}[!] Error: Unknown.\n{Fore.RESET}{e}")
                exit_program()
            
            data = response.json()

            if not data:
                break
            
            for commit in data:
                commits.append({
                    'repo': repo_name,
                    'message': commit['commit']['message'],
                    'url': commit['html_url'],
                    'date': commit['commit']['author']['date'],
                    'sha': commit['sha'][:7],
                    'email': commit['commit']['author']['email']
                })
            
            page += 1

    working_indicator.stop()
    
    return commits

def generate_gravatar_url(email: str):
    # Normalize the email address
    email = email.strip().lower()
    # Calculate MD5 hash
    email_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
    # Return the Gravatar URL
    return f"https://www.gravatar.com/{email_hash} {Fore.BLUE}({Fore.LIGHTBLACK_EX}{email}{Fore.BLUE})"

# runs PatchPirate
def run(settings: dict) -> list:
    print(f"{banner}")
    
    user_commits = get_user_commits(settings=settings)

    email_addresses = set()

    print(f"\n{Fore.RED}[*] WARNING: These results may not be entirely accurate, it is up to you verify them. This is simply a tool.\n")

    for commit in user_commits:
        email = commit['email']
        if email:
            if email.endswith("noreply.github.com"):
                obfuscated = email
            else:
                email_addresses.add(email)
    
    print(f"{Fore.BLUE}Total commits found{Fore.WHITE}: {Fore.RED}{len(user_commits)}")
    print("-----------------------------------------------------------------------------------------")
    print(f"{Fore.YELLOW}Obfucated noreply address{Fore.WHITE}: {Fore.GREEN}{obfuscated}")
    print("-----------------------------------------------------------------------------------------")
    print(f"{Fore.RED}[=== Discovered Emails ===]\n")
    for email in email_addresses:
        print(f"{Fore.GREEN}{email}")
    
    print("-----------------------------------------------------------------------------------------")
    print(f"{Fore.RED}[=== Gravitars ===]\n")
    for email in email_addresses:
        print(f"{Fore.GREEN}{generate_gravatar_url(email)}")
    print("-----------------------------------------------------------------------------------------")

    return user_commits