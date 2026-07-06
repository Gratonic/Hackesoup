"""
[=== Author Information and Program Details ===]

File Name: mudelatie.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.12.3
Dependencie(s): halo, piratescanner, colorama, json, os
Last Modified: December 17, 2025

[=== Description ===]

This is the SQLI scanner for Hackesoup.

[=== Current Plan ===]



"""

# [=== Imports ===] #

from colorama import Fore # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
from halo import Halo
import importlib
import requests
import random
import sys
import os

python_modules_path = os.path.join(os.path.dirname(__file__), "..", "Soup", "Lib", "Python_Modules")
sys.path.append(python_modules_path)

crawler = importlib.import_module("crawler")

utils = importlib.import_module("utils")

def exit_program() -> None:
    utils.exit_program(tool_name="dabijar")

# [=== Functionality ===] #

def load_payloads() -> list:
    payloads = utils.load_payloads(filename="../Soup/DB/Dabijar/payloads.txt")

    return payloads

print(load_payloads())