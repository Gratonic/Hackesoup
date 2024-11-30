import colorama
import socket
import psutil
import re

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

# Set to 1 and breaks out of loop if all requested user input is valid
valid_choice = 0

# Used for some functions to determine the amount of threads the user can safely use for the program
def find_safe_thread_amount() -> int:
    thread_count = psutil.cpu_count(logical=True)
    thread_amount_allowed_for_program = round(int(thread_count / 2))
    return thread_amount_allowed_for_program

# Toolbox Prompt
def toolbox() -> int:
    global valid_choice
    while valid_choice == 0:
        tool = input(f"{magenta}Please Choose An Option From The Toolbox{reset} {green}[Ex: 3]{reset}: ")
        try:
            tool = int(tool)
            # 7 because of easter egg, number will be changed to a higher number in future versions
            if tool <= 7:
                valid_choice = 1
                return tool
            else:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Tool.{reset}")
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Tool.{reset}")

# Tool Setup Prompt
def setup() -> int:
    global valid_choice
    while valid_choice == 0:
        setup_opt = input(f"{magenta}Please Choose A Setup Option{reset} {green}[Ex: 2]{reset}: ") 
        try:
            setup_opt = int(setup_opt)
            # 5 is the last setup option for the largest setup menus, may change in future versions
            if setup_opt <= 13:
                valid_choice = 1
                return setup_opt
            else:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Setup Option.{reset}")
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Setup Option.{reset}")

# Target Prompt - IP Address Only
def target() -> int:
    global valid_choice
    while valid_choice == 0:
        print(f"{magenta}======================{reset}")
        targ = input(f"{magenta}Please Specify a Target{reset} {green}[Ex: 74.203.143.35]{reset}: ")
        print("Validating Target...")
        try:
            socket.gethostbyaddr(target)
            valid_choice = 1
            return targ
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Target.{reset}")

# Special Target Prompt - IP Address or Website
def special_target() -> int:
    global valid_choice
    while valid_choice == 0:
        print(f"{yellow}[*] Warning{reset}: {light_yellow}If Your Target Is A Website Use The Domain Name and Not The IP Address, Otherwise The Proxy Domain Will Be The Target!{reset}")
        print(f"{magenta}======================{reset}")
        targ = input(f"{magenta}Please Specify a Target{reset} {green}[Ex: 74.203.143.35 or www.example.com]{reset}: ")
        print("Validating Target...")
        # User provided target is more likely to be a website (domain name) than an IP address
        try:
            socket.gethostbyname(target)
            valid_choice = 1
            return targ
        except:
            try:
                socket.gethostbyaddr(target)
                valid_choice = 1
                return targ
            except:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Target.{reset}")

# Port Prompt
def port() -> int:
    global valid_choice
    while valid_choice == 0:
        prt = input(f"{magenta}Please Specify A Port {green}[Ex: 21]{reset}: ")
        try:
            prt = int(port)
            # 65535 is the last port number
            if prt > 65535:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Port.{reset}")
            elif prt < 1:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Port.{reset}")
            else:
                valid_choice = 1
                return prt
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Port.{reset}")

# Port Range Prompt
def port_range() -> str:
    global valid_choice
    while valid_choice == 0:
        prt_range = input(f"{magenta}Please Specify A Port Range Seperated By Spaces{reset} {green}[Ex: 1-53]{reset}: ")
        try:
            prts = prt_range.split("-")
            start_prt = int(prts[0])
            end_prt = int(prts[1])
            # 65535 is the last port number
            if start_prt > 65535 or end_prt > 65535:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Port Range.{reset}")
            elif start_prt < 1 or end_prt < 1:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Port Range.{reset}")
            else:
                valid_choice = 1
                return prt_range
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Port Range.{reset}")

# Settings Prompt
def settings() -> int:
    global valid_choice
    while valid_choice == 0:
        setting = input(f"Please Choose A Setting: ")
        try:
            int(setting)
            # 13 is the last possible menu option for the largest setting menus, may change in future versions
            if setting > 13:
                valid_choice = 1
                return setting
            else:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Setting.{reset}")
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Setting.{reset}")

# Custom Payload File Prompt
def custom_payload_file() -> str:
    global valid_choice
    while valid_choice == 0:
        pay_file_path = input(f"{magenta}Please Specify The Path To Your Payload File{reset} {green}[Ex: ./Payloads/your_payloads.txt]{reset}: ")
        try:
            # Splits the file path up for basic validation
            pay_path_contents = re.split("[\\/]", pay_file_path)
            # Grabbing the payload file for basic validation
            pay_file_contents = pay_path_contents[-1]
            pay_file_contents = pay_file_contents.split(".")
            pay_file = pay_file_contents[-1]
            if pay_file == "txt":
                valid_choice = 1
                return pay_file_path
            elif pay_file == "text":
                valid_choice = 1
                return pay_file_path
            else:
                print(f"{red}[!] Error{reset}: {light_red}Invalid File Path or File Type (file type must be {reset}{green}.txt or .text{reset}{light_red}).{reset}")
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid File Path or File Type (file type must be {reset}{green}.txt or .text{reset}{light_red}).{reset}")

# Timeout Amount Prompt
def timeout_amount() -> int:
    global valid_choice
    while valid_choice == 0:
        timeout = input(f"{magenta}Please Specify The Timeout Amount{reset} {green}[Ex: '3' is 3 seconds]{reset}: ")
        try:
            timeout = int(timeout)
            valid_choice = 1
            return timeout
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Input. Numbers Only!{reset}")

# Thread Amount Prompt
def thread_amount() -> int:
    global valid_choice
    safe_thread_amount = find_safe_thread_amount()
    while valid_choice == 0:
        thread_amount = input(f"{magenta}Please Specify The Thread Amount{reset} {green}[Ex: 4]{reset}: ")
        try:
            thread_amount = int(thread_amount)
            if thread_amount > safe_thread_amount:
                print(f"{red}[!] Error{reset}: {light_red}Too Many Threads. You May Use Up To {reset}{green}{safe_thread_amount}{reset}{light_red} Threads For This Computer, Using More Could Overload Your CPU.{reset}")
            valid_choice = 1
            return thread_amount
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Input. Numbers Only!{reset}")

# Timeout and Thread Amount Prompt
def timeout_and_thread_amount() -> list:
    global valid_choice
    safe_thread_amount = find_safe_thread_amount()
    while valid_choice == 0:
        timeout = input(f"{magenta}Please Specify The Timeout Amount{reset} {green}[Ex: '3' is 3 seconds]{reset}: ")
        thread_amount = input(f"{magenta}Please Specify The Thread Amount{reset} {green}[Ex: 4]{reset}: ")
        try:
            timeout = int(timeout)
            thread_amount = int(thread_amount)
            if thread_amount > safe_thread_amount:
                print(f"{red}[!] Error{reset}: {light_red}Too Many Threads. You May Use Up To {reset}{green}{safe_thread_amount}{reset}{light_red} Threads For This Computer, Using More Could Overload Your CPU.{reset}")
            else:
                valid_choice = 1
                return [timeout, thread_amount]
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Input. Numbers Only!{reset}")

# Custom Payload File Prompt + Timeout and Thread Amount Prompt
def custom_payload_file_plus_timeout_and_thread_amount() -> list:
    global valid_choice
    safe_thread_amount = find_safe_thread_amount()
    while valid_choice == 0:
        pay_file_path = input(f"{magenta}Please Specify The Path To Your Payload File{reset} {green}[Ex: ./Payloads/your_payloads.txt]{reset}: ")
        timeout = input(f"{magenta}Please Specify The Timeout Amount{reset} {green}[Ex: '3' is 3 seconds]{reset}: ")
        thread_amount = input(f"{magenta}Please Specify The Thread Amount{reset} {green}[Ex: 4]{reset}: ")
        try:
            pay_path_contents = re.split("[\\/]", pay_file_path)
            pay_file_contents = pay_path_contents[-1]
            pay_file_contents = pay_file_contents.split(".")
            pay_file_type = pay_file_contents[-1]
            if pay_file_type == "txt":
                pass
            elif pay_file_type == "text":
                pass
            else:
                print(f"{red}[!] Error{reset}: {light_red}Invalid File Path or File Type (file type must be {reset}{green}.txt or .text{reset}{light_red}).{reset}")
        except:
            print(f"{red}[!] Error{reset}: {light_red}Something Went Wrong During The File Validation Process.{reset}")
        try:
            timeout = int(timeout)
            thread_amount = int(thread_amount)
            if thread_amount > safe_thread_amount():
                print(f"{red}[!] Error{reset}: {light_red}Too Many Threads. You May Use Up To {reset}{green}{safe_thread_amount}{reset}{light_red} Threads For This Computer, Using More Could Overload Your CPU.{reset}")
            else:
                # Safe to break the loop here because everything must go well to reach this point
                valid_choice = 1
                return [pay_file_path, timeout, thread_amount]
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Input! Numbers Only!{reset}")