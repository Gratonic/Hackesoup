"""
[=== Author Information and Program Details ===]

File Name: utils.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.12.3
Dependencie(s): colorama
Last Modified: October 27, 2025

[=== Description ===]

This module contains commonly used functions.
"""

# [=== Imports ===] #

from colorama import Fore, Back # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
import os

# [=== Functionality ===] #

# exits x program after priting a tool specific message
def exit_program(tool_name: str) -> None:
    goodbye_messages = {
        "hackesoup": "\n\nTschüss!",
        "patchpirate": "\n\nSvako dobro i doviđenja!",
        "serikandor": "\n\nשיהיה לך יום שקט ולהתראות לעת עתה!",
        "dabijar": "\n\nFino alla prossima volta! Arrivederci!",
        "mudelatie": "\n\nWees voorzichtig!",
        "baumspinne": "\n\nVielen Dank für Ihre Unterstützung und die Zusammenarbeit. Wünschend Ihnen alles Gute für die Zukunft. Auf Wiedersehen!",
        "wafter": "\n\nCuídese!",
        "soupemapper": "\n\nGood luck and goodbye!"
    }

    exit_message = f"{Fore.MAGENTA}{goodbye_messages[tool_name]}{Fore.RESET}"
    print(exit_message)
    exit()

# Clears the users terminal
def clear_terminal():
    if os.name == "posix": # For Linux or MacOS
        os.system("clear")
    else:
        os.system("cls") # For Windows

def load_payloads(filename: str) -> list:
    with open(filename, "r") as payload_file:
        payloads = payload_file.readlines()
        
    return payloads