import colorama

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

def toolbox() -> None:
    print(f"""
{magenta}======================{reset}
{yellow} [-^-]{reset}{magenta} Toolbox {reset}{yellow}[-^-]{reset}
{magenta}======================{reset}
{gray}0) Exit{reset}
{blue}1) Port Scanner{reset}
{light_blue}2) Sub Domain Finder{reset}
{blue}3) XSS Vulnerability Scanner{reset}
{light_blue}4) Directory Traversal Vulnerability Scanner{reset}
{blue}5) SQLI Vulnerability Scanner{reset}
{light_blue}6) Destroyer{reset}
{gray}7) Previous Menu{reset}
{magenta}======================{reset}
    """)

# Port Scanner Menus
def port_scanner_setup_1() -> None:
    print(f"""
{magenta}==========================={reset}
{yellow} Port Scanner Setup Menu 1{reset}
{magenta}==========================={reset}
{gray}0) Exit{reset}
{blue}1) Single Port{reset}
{light_blue}2) Port Range{reset}
{gray}3) Re-Open Toolbox{reset}
{magenta}=========================={reset}
    """)

def port_scanner_setup_2() -> None:
    print(f"""
{magenta}=========================={reset}
{yellow} Port Scanner Setup Menu 2{reset}
{magenta}=========================={reset}
{gray}0) Exit{reset}
{blue}1) Basic Scan{reset}
{light_blue}2) Stealth Scan{reset}
{blue}3) Advanced Scan{reset}
{gray}4) Previous Menu{reset}
{magenta}=========================={reset}
    """)

def port_scanner_settings() -> None:
    print(f"""
{magenta}======================={reset}
{yellow} Port Scanner Settings{reset}
{magenta}======================={reset}
{gray}0) Exit{reset}
{blue}1) Adjust Thread Count{reset}
{light_blue}2) Adjust Timeout{reset}
{blue}3) Adjust Thread Count and Timeout{reset}
{light_blue}4) Adjust Thread Count and Preform A Stealth Scan{reset}
{blue}5) Adjust Timeout and Preform A Stealth Scan{reset}
{light_blue}6) Adjust Thread Count, Adjust Timeout, and Preform A Stealth Scan{reset}
{gray}7) Previous Menu{reset}
{magenta}======================={reset}
    """)

# Sub Domain Finder Menus
def sub_finder_setup() -> None:
    print(f"""
{magenta}========================={reset}
{yellow} Sub Domain Finder Setup{reset}
{magenta}========================={reset}
{gray}0) Exit{reset}
{blue}1) Basic Search{reset}
{light_blue}2) Stealth Search{reset}
{blue}3) Advanced Search{reset}
{gray}4) Re-open Toolbox{reset}
{magenta}========================{reset}
    """)

def sub_finder_settings() -> None:
    print(f"""
{magenta}============================{reset}
{yellow} Sub Domain Finder Settings{reset}
{magenta}============================{reset}
{gray}0) Exit{reset}
{blue}1) Adjust Thread Amount{reset}
{light_blue}2) Adjust Timeout{reset}
{blue}3) Adjust Thread Amount and Timeout{reset}
{light_blue}4) Use Stealth Features and Adjust Thread Amount{reset}
{blue}5) Use Steatlh Features and Adjust Timeout{reset}
{light_blue}6) Use Stealth Features, Adjust Thread Amount, and Adjust Timeout{reset}
{blue}7) Use Custom Payload File{reset}
{light_blue}8) Use Custom Payload File and Stealth Features{reset}
{blue}9) Use Custom Payload File and Adjust Thread Amount{reset}
{light_blue}10) Use Custom Payload File and Adjust Timeout{reset}
{blue}11) Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features{reset}
{gray}12) Previous Menu{reset}
{magenta}============================{reset}
    """)

# XSS Vulnerability Scanner Menus
def xss_scanner_setup() -> None:
    print(f"""
{magenta}================================={reset}
{yellow} XSS Vulnerability Scanner Setup{reset}
{magenta}================================={reset}
{gray}0) Exit{reset}
{blue}1) Basic Scan{reset}
{light_blue}2) Stealth Scan{reset}
{blue}3) Advanced Scan{reset}
{gray}4) Re-open Toolbox{reset}
{magenta}================================={reset}
    """)

def xss_scanner_settings() -> None:
    print(f"""
{magenta}===================================={reset}
{yellow} XSS Vulnerability Scanner Settings{reset}
{magenta}===================================={reset}
{gray}0) Exit{reset}
{blue}1) Adjust Thread Amount{reset}
{light_blue}2) Adjust Timeout{reset}
{blue}3) Adjust Thread Amount and Timeout{reset}
{light_blue}4) Use Stealth Features and Adjust Thread Amount{reset}
{blue}5) Use Steatlh Features and Adjust Timeout{reset}
{light_blue}6) Use Stealth Features, Adjust Thread Amount, and Adjust Timeout{reset}
{blue}7) Use Custom Payload File{reset}
{light_blue}8) Use Custom Payload File and Stealth Features{reset}
{blue}9) Use Custom Payload File and Adjust Thread Amount{reset}
{light_blue}10) Use Custom Payload File and Adjust Timeout{reset}
{blue}11) Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features{reset}
{gray}12) Previous Menu{reset}
{magenta}===================================={reset}
    """)

# Directory Traversal Vulnerability Scanner Menus
def dir_traversal_setup() -> None:
    print(f"""
{magenta}================================================={reset}
{yellow} Directory Traversal Vulnerability Scanner Setup{reset}
{magenta}================================================={reset}
{gray}0) Exit{reset}
{blue}1) Basic Scan{reset}
{light_blue}2) Stealth Scan{reset}
{blue}3) Advanced Scan{reset}
{gray}4) Re-open Toolbox{reset}
{magenta}================================================={reset}
    """)

def dir_traversal_settings() -> None:
    print(f"""
{magenta}==========================================={reset}
{yellow} Directory Traversal Vulnerability Scanner{reset}
{magenta}==========================================={reset}
{gray}0) Exit{reset}
{blue}1) Adjust Thread Amount{reset}
{light_blue}2) Adjust Timeout{reset}
{blue}3) Adjust Thread Amount and Timeout{reset}
{light_blue}4) Use Stealth Features and Adjust Thread Amount{reset}
{blue}5) Use Steatlh Features and Adjust Timeout{reset}
{light_blue}6) Use Stealth Features, Adjust Thread Amount, and Adjust Timeout{reset}
{blue}7) Use Custom Payload File{reset}
{light_blue}8) Use Custom Payload File and Stealth Features{reset}
{blue}9) Use Custom Payload File and Adjust Thread Amount{reset}
{light_blue}10) Use Custom Payload File and Adjust Timeout{reset}
{blue}11) Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features{reset}
{gray}12) Previous Menu{reset}
{magenta}==========================================={reset}
    """)

# SQLI Vulnerability Scanner Menus
def sqli_scanner_setup() -> None:
    print(f"""
{magenta}=================================={reset}
{yellow} SQLI Vulnerability Scanner Setup{reset}
{magenta}=================================={reset}
{gray}0) Exit{reset}
{blue}1) Basic Scan{reset}
{light_blue}2) Stealth Scan{reset}
{blue}3) Advanced Scan{reset}
{gray}4) Re-open Toolbox{reset}
{magenta}=================================={reset}
    """)

def sqli_scanner_settings() -> None:
    print(f"""
{magenta}====================================={reset}
{yellow} SQLI Vulnerability Scanner Settings{reset}
{magenta}====================================={reset}
{gray}0) Exit{reset}
{blue}1) Adjust Thread Amount{reset}
{light_blue}2) Adjust Timeout{reset}
{blue}3) Adjust Thread Amount and Timeout{reset}
{light_blue}4) Use Stealth Features and Adjust Thread Amount{reset}
{blue}5) Use Steatlh Features and Adjust Timeout{reset}
{light_blue}6) Use Stealth Features, Adjust Thread Amount, and Adjust Timeout{reset}
{blue}7) Use Custom Payload File{reset}
{light_blue}8) Use Custom Payload File and Stealth Features{reset}
{blue}9) Use Custom Payload File and Adjust Thread Amount{reset}
{light_blue}10) Use Custom Payload File and Adjust Timeout{reset}
{blue}11) Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features{reset}
{gray}12) Previous Menu{reset}
{magenta}====================================={reset}
    """)

# File Destroyer Menus
def file_destroyer_setup() -> None:
    print(f"""
{magenta}======================{reset}
{yellow} File Destroyer Setup{reset}
{magenta}======================{reset}
{gray}0) Exit{reset}
{blue}1) Basic Destruction{reset}
{light_blue}2) Advanced Destruction{reset}
{gray}3) Re-open Toolbox{reset}
{magenta}======================{reset}
    """)

def file_destroyer_settings() -> None:
    print(f"""
{magenta}========================={reset}
{yellow} File Destroyer Settings{reset}
{magenta}========================={reset}
{gray}Exit{reset}
{blue}Permanently Encrypt File with a Modern AES Cipher{reset}
{light_blue}Overwrite The File with Random Data X Amount of Times{reset}
{blue}Permanently Encrypt File with a Modern AES Cipher and Overwrite The File with Random Data X Amount Of Times{reset}
{light_blue}Delete The File{reset}
{blue}Permanently Encrypt File with a Modern AES Cipher, Overwrite The File X Amount Of Times, and Delete The File{reset}
{gray}Previous Menu{reset}
{magenta}========================={reset}
    """)