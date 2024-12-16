# Imports PIP modules
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

# TODO: Finish the destroyer_menus
# checks the menu_num to make sure its an integer or can be converted to one
def check_menu_num(mn):
    try:
        return int(mn)
    except:
        raise ValueError(f"{red}Menu_num must be an integer or an integer in string form!{reset} {blue}[EX: 1 or '1']{reset}")

# builds the UX menu along with its title and returns it
def menu_builder(tool_num: int, smn: str, mops: dict, meds: dict, special_mops={}, special_mops_check=False) -> object:
    # Grabs the needed menu options, menu descriptions, and special menu options info
    _menu_opt_nums = list(mops.keys())
    _menu_opt_names = list(mops.values())
    _descriptions = list(meds.values())
    _special_opt_nums = list(special_mops.keys())
    _special_opt_names = list(special_mops.values())
    # Creates the menu object (frankenstien monster)
    frank = frankenstien.Frank()
    # Grabs the title and title bar for the menu
    title_frags = hs_menu_titles.grab_menu(tool_num)
    # Grabs the title from title_frags
    t = title_frags[0]
    # Grabs the title_bar from title_frags
    tb = title_frags[1]
    # Adds the title to the menu based on the name of the tool
    frank.add_limb("head", text=t, title_bar=tb, small_menu_name=smn)
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

def main_menu():
    # Used to build the menus
    # NOTE: if a new option needs to be added to the menu, simply add it the right dictionary
    options = {
        1: " Port Scanner", 2: " Subdomain Finder", 3: " XSS Vulnerability Scanner",
        4: " Directory Traversal Vulnerability Scanner", 5: " SQLI Vulnerability Scanners", 6: " Destroyer"
    }
    descriptions = {
        1: "scans port to see if they are open, closed, or filtered", 2: "finds the subdomains of a websites",
        3: "scans a website for XSS vulnerabilities", 4: "scans a website for directory traversal vulnerabilities",
        5: "scans a website for SQLI vulnerabilities", 6: "adds a junk data to a file, encrypts it with aes, then overwrites it and deletes it"
    }
    # Creates the menu object
    menu = menu_builder(tool_num=0, mops=options, meds=descriptions, smn="Hackesoup")
    # Prints the complete menu to the output console
    menu.shock()

def port_scanner_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to the menu, simply add it the right dictionary
    if menu_num == 1:
        # Menu 1 options and descriptions
        menu_1_options = {
            1: "Single Port", 2: "Port Range"
        }
        menu_1_descriptions = {
            1: "scan a single port", 2: "scan a range of ports"
        }
        # Creates the menu object
        menu = menu_builder(tool_num=1, mops=menu_1_options, meds=menu_1_descriptions, smn="Port Scanner")
    elif menu_num == 2:
        # Menu 2 options and descriptions
        menu_2_options = {
            1: "Basic Scan", 2: "Advanced Scan", 3: "Stealth Scan"
        }
        menu_2_descriptions = {
            1: "scan without any stealth and/or firewall evasion features",
            2: "configure the scanner settings for this scan",
            3: "use stealth and firewall evasion features - NSFW"
        }
        # Creates the menu object
        menu = menu_builder(tool_num=1, mops=menu_2_options, meds=menu_2_descriptions, smn="Port Scanner")
    elif menu_num == 3:
        # Menu 3 options and descriptions
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
        menu = menu_builder(tool_num=1, mops=menu_3_options, meds=menu_3_descriptions, smn="Port Scanner")
    # Prints the complete menu to the output console
    menu.shock()

def sub_domain_finder_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to the menu, simply add it the right dictionary
    if menu_num == 1:
        # Menu 1 options and descriptions
        menu_1_options = {
            1: "Basic Search",
            2: "Advanced Search",
            3: "Stealth Search"
        }
        menu_1_descriptions = {
            1: "preform a search without stealth/firewall evasion features",
            2: "configure the subdomain finder settings for this search",
            3: "preform a search with stealth/firewall evasion features - NSFW"
        }
        menu = menu_builder(tool_num=2, mops=menu_1_options, meds=menu_1_descriptions, smn="Subdomain Finder")
    elif menu_num == 2:
        # Menu 2 options and descriptions
        menu_2_options = {
            1: "Adjust Thread Amount", 2: "Adjust Timeout",
            3: "Use stealth/firewall evasion features", 4: "Adjust Thread Amount and Timeout", 
            5: "Use Stealth Features and Adjust Thread Amount", 6: "Use Steatlh Features and Adjust Timeout", 
            7: "Use Stealth Features, Adjust Thread Amount, and Adjust Timeout", 8: "Use Custom Payload File", 
            9: "Use Custom Payload File and Stealth Features", 10: "Use Custom Payload File and Adjust Thread Amount", 
            11: "Use Custom Payload File and Adjust Timeout", 12: "Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features"
        }
        menu_2_descriptions = {
            1: "adjust the thread count", 2: "adjust the timeout",
            3: "use stealth/firewall evasion features", 4: "adjust both the thread count and timeout", 
            5: "use stealth/firewall evasion features and adjust the thread count - NSFW", 6: "use stealth/firewall evasion features and adjust the timeout - NSFW", 
            7: "use stealth/firewall evasion features and adjust both the thread count and timeout - NSFW", 8: "use a custom payload file", 
            9: "use a custom payload file and stealth/firewall evasion features - NSFW", 10: "use a custom payload file and adjust the thread count",
            11: "use a custom payload file and adjust the timeout", 12: "use a custom payload file, adjust both the thread count and timeout, and use stealth/firewall evasion features - NSFW"
        }
        menu = menu_builder(tool_num=2, mops=menu_2_options, meds=menu_2_descriptions, smn="Subdomain Finder")
    # Prints the complete menu to the output console
    menu.shock()

def xss_vuln_scanner_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to the menu, simply add it the right dictionary
    if menu_num == 1:
        # Menu 1 options and descriptions
        menu_1_options = {
            1: "Basic Search",
            2: "Advanced Search",
            3: "Stealth Search"
        }
        menu_1_descriptions = {
            1: "preform a scan without stealth/firewall evasion features",
            2: "configure the xss vulnerability scanner settings for this scan",
            3: "preform a scan with stealth/firewall evasion features - NSFW"
        }
        menu = menu_builder(tool_num=3, mops=menu_1_options, meds=menu_1_descriptions, smn="XSS Vulnerability Scanner")
    elif menu_num == 2:
        # Menu 2 options and descriptions
        menu_2_options = {
            1: "Adjust Thread Amount", 2: "Adjust Timeout",
            3: "Use stealth/firewall evasion features", 4: "Adjust Thread Amount and Timeout", 
            5: "Use Stealth Features and Adjust Thread Amount", 6: "Use Steatlh Features and Adjust Timeout", 
            7: "Use Stealth Features, Adjust Thread Amount, and Adjust Timeout", 8: "Use Custom Payload File", 
            9: "Use Custom Payload File and Stealth Features", 10: "Use Custom Payload File and Adjust Thread Amount", 
            11: "Use Custom Payload File and Adjust Timeout", 12: "Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features"
        }
        menu_2_descriptions = {
            1: "adjust the thread count", 2: "adjust the timeout",
            3: "use stealth/firewall evasion features", 4: "adjust both the thread count and timeout", 
            5: "use stealth/firewall evasion features and adjust the thread count - NSFW", 6: "use stealth/firewall evasion features and adjust the timeout - NSFW", 
            7: "use stealth/firewall evasion features and adjust both the thread count and timeout - NSFW", 8: "use a custom payload file", 
            9: "use a custom payload file and stealth/firewall evasion features - NSFW", 10: "use a custom payload file and adjust the thread count",
            11: "use a custom payload file and adjust the timeout", 12: "use a custom payload file, adjust both the thread count and timeout, and use stealth/firewall evasion features - NSFW"
        }
        menu = menu_builder(tool_num=3, mops=menu_2_options, meds=menu_2_descriptions, smn="XSS Vulnerability Scanner")
    # Prints the complete menu to the output console
    menu.shock()

def dir_trav_vuln_scanner_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to the menu, simply add it the right dictionary
    if menu_num == 1:
        # Menu 1 options and descriptions
        menu_1_options = {
            1: "Basic Search",
            2: "Advanced Search",
            3: "Stealth Search"
        }
        menu_1_descriptions = {
            1: "preform a scan without stealth/firewall evasion features",
            2: "configure the directory traversal vulnerability scanner settings for this scan",
            3: "preform a scan with stealth/firewall evasion features - NSFW"
        }
        menu = menu_builder(tool_num=4, mops=menu_1_options, meds=menu_1_descriptions, smn="Directory Traversal Vulnerability Scanner")
    elif menu_num == 2:
        # Menu 2 options and descriptions
        menu_2_options = {
            1: "Adjust Thread Amount", 2: "Adjust Timeout",
            3: "Use stealth/firewall evasion features", 4: "Adjust Thread Amount and Timeout", 
            5: "Use Stealth Features and Adjust Thread Amount", 6: "Use Steatlh Features and Adjust Timeout", 
            7: "Use Stealth Features, Adjust Thread Amount, and Adjust Timeout", 8: "Use Custom Payload File", 
            9: "Use Custom Payload File and Stealth Features", 10: "Use Custom Payload File and Adjust Thread Amount", 
            11: "Use Custom Payload File and Adjust Timeout", 12: "Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features"
        }
        menu_2_descriptions = {
            1: "adjust the thread count", 2: "adjust the timeout",
            3: "use stealth/firewall evasion features", 4: "adjust both the thread count and timeout", 
            5: "use stealth/firewall evasion features and adjust the thread count - NSFW", 6: "use stealth/firewall evasion features and adjust the timeout - NSFW", 
            7: "use stealth/firewall evasion features and adjust both the thread count and timeout - NSFW", 8: "use a custom payload file", 
            9: "use a custom payload file and stealth/firewall evasion features - NSFW", 10: "use a custom payload file and adjust the thread count",
            11: "use a custom payload file and adjust the timeout", 12: "use a custom payload file, adjust both the thread count and timeout, and use stealth/firewall evasion features - NSFW"
        }
        menu_builder(tool_num=4, mops=menu_2_options, meds=menu_2_descriptions, smn="Directory Traversal Vulnerability Scanner")
    # Prints the complete menu to the output console
    menu.shock()

def sqli_vuln_scanner_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to the menu, simply add it the right dictionary
    if menu_num == 1:
        # Menu 1 options and descriptions
        menu_1_options = {
            1: "Basic Search",
            2: "Advanced Search",
            3: "Stealth Search"
        }
        menu_1_descriptions = {
            1: "preform a scan without stealth/firewall evasion features",
            2: "configure the sqli vulnerability scanner settings for this scan",
            3: "preform a scan with stealth/firewall evasion features - NSFW"
        }
        menu = menu_builder(tool_num=5, mops=menu_1_options, meds=menu_1_descriptions, smn="SQLI Vulnerability Scanner")
    elif menu_num == 2:
        # Menu 2 options and descriptions
        menu_2_options = {
            1: "Adjust Thread Amount", 2: "Adjust Timeout",
            3: "Use stealth/firewall evasion features", 4: "Adjust Thread Amount and Timeout", 
            5: "Use Stealth Features and Adjust Thread Amount", 6: "Use Steatlh Features and Adjust Timeout", 
            7: "Use Stealth Features, Adjust Thread Amount, and Adjust Timeout", 8: "Use Custom Payload File", 
            9: "Use Custom Payload File and Stealth Features", 10: "Use Custom Payload File and Adjust Thread Amount", 
            11: "Use Custom Payload File and Adjust Timeout", 12: "Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features"
        }
        menu_2_descriptions = {
            1: "adjust the thread count", 2: "adjust the timeout",
            3: "use stealth/firewall evasion features", 4: "adjust both the thread count and timeout", 
            5: "use stealth/firewall evasion features and adjust the thread count - NSFW", 6: "use stealth/firewall evasion features and adjust the timeout - NSFW", 
            7: "use stealth/firewall evasion features and adjust both the thread count and timeout - NSFW", 8: "use a custom payload file", 
            9: "use a custom payload file and stealth/firewall evasion features - NSFW", 10: "use a custom payload file and adjust the thread count",
            11: "use a custom payload file and adjust the timeout", 12: "use a custom payload file, adjust both the thread count and timeout, and use stealth/firewall evasion features - NSFW"
        }
        menu = menu_builder(tool_num=5, mops=menu_2_options, meds=menu_2_descriptions, smn="SQLI Vulnerability Scanner")
    # Prints the complete menu to the output console
    menu.shock()

def destroyer_menus(menu_num):
    # Preforms some quick validation
    menu_num = check_menu_num(menu_num)
    # Used to build the menus
    # NOTE: if a new option needs to be added to the menu, simply add it the right dictionary
    if menu_num == 1:
        # Menu 1 options and descriptions
        menu_1_options = {
            1: "Basic Destruction", 2: "Advanced Destruction"
        }
        menu_1_descriptions = {
            1: "add random data to the file, encrypt it with a modern AES based cipher (256-bit key), overwrite it 10 times, and delete it",
            2: "choose what the destroyer does to the file"
        }
        menu = menu_builder(tool_num=6, mops=menu_1_options, meds=menu_1_descriptions, smn="Destroyer")
    elif menu_num == 2:
        # Menu 2 options and descriptions
        menu_2_options = {
            1: "Permanently Encrypt File with a Modern AES Cipher",
            2: "Overwrite The File with Random Data X Amount of Times",
            3: "Permanently Encrypt File with a Modern AES Cipher and Overwrite The File with Random Data X Amount Of Times",
            4: "Delete The File",
            5: "Permanently Encrypt File with a Modern AES Cipher, Overwrite The File X Amount Of Times, and Delete The File"
        }
        menu_2_descriptions = {
            1: "encrypt the file using a 256-bit key with a modern AES cipher",
            2: "overwrite the file with random data X amount of times (default: 10)",
            3: "encrypt the file using a 256-bit key with a modern AES cipher and overwrite it X amount of times (default: 10)",
            4: "simply delete the file",
            5: "encrypt the file using a 256-bit key with a modern AES cipher, overwrite it X amount of times (default: 10), and delete it"
        }
        menu = menu_builder(tool_num=6, mops=menu_2_options, meds=menu_2_descriptions, smn="Destroyer")
    menu.shock()

# Calls the main menu
def call_main_menu():
    main_menu()

# Calls the Port Scanner Menus
def call_port_scanner_setup_1():
    port_scanner_menus(1)

def call_port_scanner_setup_2():
    port_scanner_menus(2)

def call_port_scanner_settings():
    port_scanner_menus(3)

# Calls the Subdomain Finder menus
def call_subdomain_finder_setup():
    sub_domain_finder_menus(1)

def call_subdomain_finder_settings():
    sub_domain_finder_menus(2)

# Calls the XSS Vulnerability Scanner menus
def call_xss_vuln_scanner_setup():
    xss_vuln_scanner_menus(1)

def call_xss_vuln_scanner_settings():
    xss_vuln_scanner_menus(2)

# Calls the Directory Traversal Vulnerability Scanner menus
def call_dir_trav_vuln_scanner_setup():
    dir_trav_vuln_scanner_menus(1)

def call_dir_trav_vuln_scanner_settings():
    dir_trav_vuln_scanner_menus(2)

# Calls the SQLI Vulnerability Scanner menus
def call_sqli_vuln_scanner_setup():
    sqli_vuln_scanner_menus(1)

def call_sqli_vuln_scanner_settings():
    sqli_vuln_scanner_menus(2)

# Calls the Destroyer menus
def call_destroyer_setup():
    destroyer_menus(1)

def call_destroyer_settings():
    destroyer_menus(2)