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
hs_menu_titles = importlib.import_module('hs_menu_titles')

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

# Clears the terminal - NOTE: 'cls' must be added for Windows along with a check for the running OS in v2
def clear_terminal():
    os.system("clear")

# :: UX Menu Interface Functions :: #

# Builds the tool/main UX menu and asks the user for their tool choice
def main_UX_menu() -> vars:
    try:
        hs_menus.call_main_menu()
        chosen_tool = hs_prompts.toolbox()
        if chosen_tool == 0:
            terminate_program()
        elif chosen_tool == 7:
            clear_terminal()
            floppy_heaven_easter_egg = hs_menu_titles.floppy_drive_heaven_easter_egg()
            print(floppy_heaven_easter_egg)
        else:
            return chosen_tool
    except KeyboardInterrupt:
        terminate_program()
# TODO: Fix single port prompt
def port_scanner_UX_menus():
    # all the tool settings to be returned are in this list...
    settings = []
    # Used to store the scan type
    scan_type = ""
    try:
        target = hs_prompts.target()
        # Prints the first setup menu
        hs_menus.call_port_scanner_setup_1()
        # Asks for the first setup option - 1 is the port_scanner tool id
        setup_option_1 = hs_prompts.setup(1)
        # Prompts for the first tool option setup choice/setting configuration
        if setup_option_1 == 0:
            terminate_program()
        elif setup_option_1 == 1:
            # type: str
            port = hs_prompts.port()
            settings.append(port)
        elif setup_option_1 == 2:
            # type: str
            port_range = hs_prompts.port_range()
            settings.append(port_range)
        # Prints the second setup menu
        hs_menus.call_port_scanner_setup_2()
        # Asks for the second setup option - 1 is the port_scanner tool id
        setup_option_2 = hs_prompts.setup(1)
        # Prompts for the second tool option setup choice/setting configuration
        if setup_option_2 == 0:
            terminate_program()
        elif setup_option_2 == 1:
            scan_type = "basic"
            settings.append(scan_type)
        elif setup_option_2 == 2:
            scan_type = "advanced"
            settings.append(scan_type)
        elif setup_option_2 == 3:
            scan_type = "stealth"
            settings.append(scan_type)
        # If the scan_type != advanced the settings will be returned. otherwise the -->
        # settings menu will be called
        if scan_type == "basic":
            return settings
        elif scan_type == "advanced":
            hs_menus.call_port_scanner_settings()
            setting_choice = hs_prompts.setup(1)
            if setting_choice == 0:
                terminate_program()
            elif setting_choice == 1:
                try:
                    thread_amount = hs_prompts.thread_amount()
                    # just for consistency
                    setting_choices = [thread_amount]
                    settings.append(setting_choices)
                except KeyboardInterrupt:
                    terminate_program()
            elif setting_choice == 2:
                try:
                    timeout_amount = hs_prompts.timeout_amount()
                    # just for consistency
                    setting_choices = [timeout_amount]
                    settings.append(setting_choices)
                except KeyboardInterrupt:
                    terminate_program()
            elif setting_choice == 3:
                try:
                    # returns [timeout, thread_amount]
                    setting_choices = hs_prompts.timeout_and_thread_amount()
                    settings.append(setting_choices)
                except KeyboardInterrupt:
                    terminate_program()
            elif setting_choice == 4:
                try:
                    special_scan_type = "advanced_stealth"
                    thread_amount = hs_prompts.thread_amount()
                    setting_choices = [special_scan_type, thread_amount]
                    settings.append(setting_choices)
                except KeyboardInterrupt:
                    terminate_program()
            elif setting_choice == 5:
                try:
                    special_scan_type = "advanced_stealth"
                    timeout_amount = hs_prompts.timeout_amount()
                    setting_choices = [special_scan_type, timeout_amount]
                    settings.append(setting_choices)
                except KeyboardInterrupt:
                    terminate_program()
            elif setting_choice == 6:
                try:
                    special_scan_type = "advanced_stealth"
                    setting_choices = hs_prompts.timeout_and_thread_amount()
                    setting_choices.insert(0, special_scan_type)
                    settings.append(setting_choices)
                except KeyboardInterrupt:
                    terminate_program()
            elif setting_choice == 7:
                pass
                # Need to add while loop that checks in the program is finished in order to create infinate menu loop for prev options
        elif scan_type == "stealth":
            return settings
    except KeyboardInterrupt:
        terminate_program()
port_scanner_UX_menus()
# port_scanner_UX_menus()
# Handles the entire UX menu and returns a list of all the user input
def UX_menu_interface() -> list:
    pass