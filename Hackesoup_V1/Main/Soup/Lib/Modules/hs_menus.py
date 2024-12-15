import colorama
# Imports Custom Modules
import frankenstien
import hs_menu_titles


# Colour objects, used for nicer output
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

# checks the menu_num to make sure its an integer or can be converted to one
def check_menu_num(mn):
    try:
        return int(mn)
    except:
        raise ValueError(f"{red}Menu_num must be an integer or an integer in string form!{reset} {blue}[EX: 1 or '1']{reset}")

# builds the UX menu and returns it
def menu_builder(mops: dict, meds: dict, special_mops={}, special_mops_check=False) -> object:
    # Grabs the needed menu options, menu descriptions, and special menu options info
    _menu_opt_nums = list(mops.keys())
    _menu_opt_names = list(mops.values())
    _descriptions = list(meds.values())
    _special_opt_nums = list(special_mops.keys())
    _special_opt_names = list(special_mops.values())
    # Creates the menu object (frankenstien monster)
    frank = frankenstien.Frank()
    # Adds the exit option to the menu
    frank.add_limb("body", text="Exit", text_colour=gray, menu_item_num=0, accent_colour=gray)
    # Adds the general menu options and their descriptions to the menu
    for item in range(len(_menu_opt_nums)):
        frank.add_limb("guts", text=_descriptions[item], text_colour=blue)
        frank.add_limb("body", text=_menu_opt_names[item], text_colour=magenta, menu_item_num=_menu_opt_nums[item], accent_colour=yellow)
    # Adds the special menu options to the menu if there is any
    # NOTE: displayed in gray
    if special_mops_check == True:
        for item in range(len(_special_opt_nums)):
            frank.add_limb("body", text=_special_opt_names[item], text_colour=gray, menu_item_num=_special_opt_nums[item], accent_colour=gray)
        # Adds the previous menu option to the menu
        frank.add_limb("body", text="Previous Menu", text_colour=gray, menu_item_num=int(f"{_special_opt_nums[-1] + 1}"), accent_colour=gray)
        # Returns the menu object
        return frank
    else:
        pass
    # Adds the previous menu option to the menu
    frank.add_limb("body", text="Previous Menu", text_colour=gray, menu_item_num=int(f"{_menu_opt_nums[-1] + 1}"), accent_colour=gray)
    # Returns the menu object
    return frank

# Menus - TODO: Fix error preventing the menu titles from being printed (error unknown)

def main_menu(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menu
    # NOTE: if a new option needs to be added to to the menu, simply add its name and description to the proper dict.
    options = {
        1: " Port Scanner", 2: " Subdomain Finder", 3: " XSS Vulnerability Scanner",
        4: " Directory Traversal Vulnerability Scanner", 5: " SQLI Vulnerability Scanners", 6: " Destroyer"
    }
    descriptions = {
        1: "scans port to see if they are open, closed, or filtered", 2: "finds the subdomains of a websites",
        3: "scans a website for XSS vulnerabilities", 4: "scans a website for directory traversal vulnerabilities",
        5: "scans a website for SQLI vulnerabilities", 6: "adds a junk data to a file, encrypts it with aes, then overwrites it and deletes it"
    }
    special_options = {7: "Previous Menu"}

def port_scanner_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to to one of the menu, simply add it the right list of menu options
    if menu_num == 1:
        menu_1_options = {
            1: "Single Port", 2: "Port Range"
        }
        menu_1_descriptions = {
            1: "scan a single port", 2: "scan a range of ports"
        }
        # Creates the menu object
        menu = menu_builder(menu_1_options, menu_1_descriptions)
    elif menu_num == 2:
        menu_2_options = {
            1: "Basic Scan", 2: "Advanced Scan", 3: "Stealth Scan"
        }
        menu_2_descriptions = {
            1: "scan without any stealth and/or firewall evasion features",
            2: "configure the scanner settings for this scan",
            3: "use stealth and firewall evasion features - NSFW"
        }
        # Creates the menu object
        menu = menu_builder(menu_2_options, menu_2_descriptions)
    elif menu_num == 3:
        menu_3_options = {
            1: "Adjust Thread Count", 2: "Adjust Timeout", 
            3: "Adjust Thread Count and Timeout", 4: "Adjust Thread Count and Preform A Stealth Scan", 
            5: "Adjust Timeout and Preform A Stealth Scan", 6: "Adjust Thread Count, Adjust Timeout, and Preform A Stealth Scan"
        }
        menu_3_descriptions = {
            1: "adjust the amount of threads", 2: "adjust the timeout", 
            3: "adjust both the thread amount and timeout", 4: "adjust the thread amount and use stealth/firewall evasion features - NSFW", 
            5: "adjust the timeout and use stealth/firewall evasion features - NSFW", 6: "adjust both the thread count and timeout and use stealth/firewall evasion features - NSFW"
        }
        # Creates the menu object
        menu = menu_builder(menu_3_options, menu_3_descriptions)

def sub_domain_finder_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to to one of the menu, simply add it the right list of menu options
    menu_1_options = [""]

def xss_vuln_scanner_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to to one of the menu, simply add it the right list of menu options
    menu_1_options = [""]

def dir_trav_vuln_scanner_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to to one of the menu, simply add it the right list of menu options
    menu_1_options = [""]

def sqli_vuln_scanner_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to to one of the menu, simply add it the right list of menu options
    menu_1_options = [""]

def destroyer_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to to one of the menu, simply add it the right list of menu options
    menu_1_options = [""]