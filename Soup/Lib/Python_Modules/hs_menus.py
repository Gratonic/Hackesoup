"""
# :: Author Information and Program Details :: #

File Name: hs_menus.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.10.12
Dependencie(s): menataur, hs_menu_titles, /Lib/Data/Menu_Information/*
Last Modified: April 13th, 2025

# :: Description :: #

This Python file contains the menu functions used to build the UX Menu Interface. The most critical function is the menu_builder()
function, which is responsible for building the menu portion of every menu and printing it to the output console. The other
functions simply use the menu_builder() function to build the menus for each tool or in the case of the main menu, the tool menu.
This code is imported and used in the hs_UX_menus.py file.
"""

# :: Imports :: #

import menataur
import hs_menu_titles
import json

# :: Functions :: #

# Creates and prints the menu portion of the UX menu
def construct_menu(menu_title_func_name: str, mops: dict | None, meds: dict | None, tool_version: str, title_colors: list) -> vars:
    # Title Content
    _title_func = getattr(hs_menu_titles, menu_title_func_name)
    _title_contents = _title_func()
    _ascii_title = _title_contents[0]
    _title_bar = _title_contents[1]
    _title_colors = title_colors
    _small_title = _title_contents[2]

    # Initalizes the menu
    menu = menataur.Menataur()

    if mops["1"] != None and meds["1"] != None:
        # Menu Options, Menu Option Numbers, and Menu Option Descriptions
        _menu_opt_nums = list(mops.keys())
        _menu_opts = list(mops.values())
        _menu_descriptions = list(meds.values())

        # Constructs the menu header (title, program support info, etc.)
        menu.add_header(
            ascii_art_title=_ascii_title,
            title_bar=_title_bar,
            title_colors = _title_colors,
            small_title=_small_title,
            program_version_color = "green",
            program_version_num = tool_version,
            os_support_message_color = "black",
            os_support_highlight_color = "yellow",
            os_support_color = "magenta",
            os_support_info = ["Linux"]
        )

        # Adds the Exit Option to the menu
        menu.add_body(
        accent_color="grey", 
        menu_option_number=0, 
        menu_option_color="grey", 
        menu_option="Exit"
        )
        _pos = 0
        _opt_num = 1
        _last_option = 1

        # Constructs the main portion of the menu (options with their descriptions)
        for element in range(len(_menu_opts)):
            menu.add_paragraph(
                text_color="blue", 
                text=_menu_descriptions[_pos]
            )
            menu.add_body(
                accent_color="yellow", 
                menu_option_number=_opt_num, 
                menu_option_color="magenta", 
                menu_option=_menu_opts[_pos]
            )
            _pos += 1
            _opt_num += 1
            _last_option += 1

        # Adds the Previous Menu Option to the menu
        menu.add_body(
        accent_color="grey", 
        menu_option_number=_last_option, 
        menu_option_color="grey", 
        menu_option="Previous Menu"
        )
    else:
        # Constructs the menu header (title, program support info, etc.)
        menu.add_header(
            ascii_art_title=_ascii_title,
            title_bar=_title_bar,
            title_colors = _title_colors,
            small_title=_small_title,
            program_version_color = "green",
            program_version_num = tool_version,
            os_support_message_color = "black",
            os_support_highlight_color = "yellow",
            os_support_color = "magenta",
            os_support_info = ["Linux"]
        )

    # Prints the menu portion of the UX menu
    menu.execute()

# Grabs the menu information and builds the menu using the construct_menu() function
def menu_builder(menu_directory_name: str, menu_number: int) -> None:
    # Grabs the respective JSON data
    file_path = f"../Soup/Lib/Data/Menu_Information/{menu_directory_name}/menu_{menu_number}.json"
    with open(file_path, "r") as menu_JSON_file:
        menu_info = json.load(menu_JSON_file)
    # Extracts the menu header information
    header = menu_info["header_info"]
    # Organises the menu header information for the construct_menu() function
    menu_title_func_name = header["menu_title_func_name"]
    tool_version = header["tool_version"]
    title_colors = header["title_colors"]
    # Extracts the options and descriptions
    options = menu_info["options"]
    descriptions = menu_info["descriptions"]
    # Builds the menu with the contruct_menu() function using the menu information
    construct_menu(
        menu_title_func_name=menu_title_func_name,
        mops=options,
        meds=descriptions,
        tool_version=tool_version,
        title_colors=title_colors
    )

# Main Menu and Tool Choice Menus

def main_menu() -> None:
    menu_builder(menu_directory_name="main_menu", menu_number=1)

def OSINT_tool_menu():
    menu_builder(menu_directory_name="OSINT_tool_menu", menu_number=1)

def web_tool_menu():
    menu_builder(menu_directory_name="web_tool_menu", menu_number=1)

def LAN_tool_menu():
    menu_builder(menu_directory_name="LAN_tool_menu", menu_number=1)

# OSINT/Recon Tool Menus

def patchpirate_menu():
    menu_builder(menu_directory_name="patchpirate", menu_number=1)

# Web Tool Menus

def saifandor_menu():
    menu_builder(menu_directory_name="saifandor", menu_number=1)

def dabijar_menu():
    menu_builder(menu_directory_name="dabijar", menu_number=1)

def mudelatie_menu():
    menu_builder(menu_directory_name="mudelatie", menu_number=1)

def baumspinne_menu():
    menu_builder(menu_directory_name="baumspinne", menu_number=1)

# Network Tool Menus

def soupemapper_menu_1():
    menu_builder(menu_directory_name="soupemapper", menu_number=1)

def soupemapper_menu_2():
    menu_builder(menu_directory_name="soupemapper", menu_number=2)
