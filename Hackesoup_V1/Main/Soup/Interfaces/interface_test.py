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

# Used to recall the previous UX menu if the user chooses the previous menu option
def call_previous_UX_menu(parent_menu_num: int, child_menu_num: int) -> int:
    # -- Menu Function Names -- #
    #
    # main menu function names
    main_menu_func_names = ["call_main_menu"]
    # port scanner menu function names
    port_scanner_menu_func_names = ["call_port_scanner_setup_1", "call_port_scanner_setup_2", "call_port_scanner_settings"]
    # subdomain finder menu function names
    subdomain_finder_menu_func_names = ["call_subdomain_finder_setup", "call_subdomain_finder_settings"]
    # XSS vulnerabiity scanner menu function names
    xss_vuln_scanner_menu_func_names = ["call_xss_vuln_scanner_setup", "call_xss_vuln_scanner_settings"]
    # directory traversal scanner menu function names
    dir_trav_scanner_menu_func_names = ["call_dir_trav_vuln_scanner_setup", "call_dir_trav_vuln_scanner_settings"]
    # SQLI vulnerability scanner menu function names
    sqli_vuln_scanner_menu_func_names = ["call_sqli_vuln_scanner_setup", "call_sqli_vuln_scanner_settings"]
    # destroyer menu function names
    destroyer_menu_func_names = "call_destroyer_setup", "call_destroyer_settings"
    # -- Prompt Function Names -- #
    #
    prompt_func_names = [
        "main_menu_prompt", "setup",
        "target", "special_target",
        "port", "port_range",
        "custom_payload_file"
        "timeout_amount", "thread_amount",
        "timeout_and_thread_amount", "custom_payload_file_plus_timeout_and_thread_amount"
    ]
    # prompt_func_name = hs_prompts_funcs[1]
    # a = getattr(hs_prompts, prompt_func_name)
    if parent_menu_num == 0:
        menu_func = getattr(hs_menus, main_menu_func_names[child_menu_num])
        setup_func = getattr(hs_prompts, prompt_func_names[1])
        menu_func()
        menu_choice = setup_func(0)
        return menu_choice
    elif parent_menu_num == 1:
        if child_menu_num == 1:
            pass
        elif child_menu_num == 2:
            pass
        else:
            print(f"{red}[!] Error: {light_red}Child Menu Number Is Out Of Scope.{reset}")
        menu_func = getattr(hs_menus, port_scanner_menu_func_names[child_menu_num])
        setup_func = setup_func = getattr(hs_prompts, prompt_func_names[1])
        menu_func()
        menu_choice = setup_func(1)
        return menu_choice
    elif parent_menu_num == 2:
        menu_func = getattr(hs_menus, subdomain_finder_menu_func_names[child_menu_num])
        setup_func = setup_func = getattr(hs_prompts, prompt_func_names[1])
        menu_func()
        menu_choice = setup_func(2)
        return menu_choice
    elif parent_menu_num == 3:
        menu_func = getattr(hs_menus, xss_vuln_scanner_menu_func_names[child_menu_num])
        setup_func = setup_func = getattr(hs_prompts, prompt_func_names[1])
        menu_func()
        menu_choice = setup_func(3)
        return menu_choice
    elif parent_menu_num == 4:
        menu_func = getattr(hs_menus, dir_trav_scanner_menu_func_names[1])
        setup_func = setup_func = getattr(hs_prompts, prompt_func_names[1])
        menu_func()
        menu_choice = setup_func(4)
        return menu_choice
    elif parent_menu_num == 5:
        menu_func = getattr(hs_menus, sqli_vuln_scanner_menu_func_names[1])
        setup_func = setup_func = getattr(hs_prompts, prompt_func_names[1])
        menu_func()
        menu_choice = setup_func(5)
        return menu_choice
    elif parent_menu_num == 6:
        menu_func = getattr(hs_menus, destroyer_menu_func_names[1])
        setup_func = setup_func = getattr(hs_prompts, prompt_func_names[1])
        menu_func()
        menu_choice = setup_func(6)
        return menu_choice

# call_previous_UX_menu(1, 1)

# Builds the Main UX Menu (used in the Menu Interface function)
def main_UX_menu():
    hs_menus.call_main_menu()
    hs_prompts.setup(0)

# Builds the Port Scanner UX Menu (used in the Menu Interface function)
def port_scanner_UX_menu():
    hs_menus.call_port_scanner_setup_1()
    hs_prompts.setup(1)

# Builds the Subdomain Finder UX Menu (used in the Menu Interface function)
def subdomain_finder_UX_menu():
    hs_menus.call_subdomain_finder_setup()
    hs_prompts.setup(2)

# Builds the XSS Vulnerability Scanner UX Menu (used in the Menu Interface function)
def xss_vuln_scanner_UX_menu():
    pass

# Builds the Directory Traversal Vulnerability Scanner UX Menu (used in the Menu Interface function)
def dir_traversal_vuln_scanner_UX_menu():
    pass

# Builds the SQLI Vulnerability UX Menu (used in the Menu Interface function)
def sqli_vuln_scanner_UX_menu():
    pass

# Builds the File Destroyer UX Menu (used in the Menu Interface function)
def destroyer_UX_menu():
    pass

# Builds the complete menu interface using the UX menu functions defined above
# NOTE: This function will be called within Main function (the one function that handles the whole program)
# TODO: Figure out a way to get the previous menu option to work somewhat like this
# Maybe use an ENV file if a global var does not retain the previously chosen options still after further testing
# Otherwise just finish the previous_UX_menu function
def menu_interface(sn=0):
    pass