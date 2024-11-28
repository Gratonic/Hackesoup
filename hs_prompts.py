import colorama
import socket

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

# Status Codes, Returned And Used For Input Validation
good_status = 0
error_status = 1
invalid_value_status = 2
invalid_tool_option_status = 3

# Tool Selection Prompt
def tool_choice() -> int:
    chosen_tool = input(f"{magenta}Please Select A Tool From The Toolbox [EX: 3]: {reset}")
    try:
        chosen_tool = int(chosen_tool)
    except:
        print(f"{red} [!] Invalid Tool Choice!{reset}")
        chosen_tool = input(f"{magenta}Please Choose A{reset} {green}Valid{reset} {magenta}Tool From The Toolbox [EX: 3]{reset}: ")
    # Will be changed to 8 in version 2
    if chosen_tool > 7:
        print(f"{red} [!] Invalid Tool Choice!{reset}")
        chosen_tool = input(f"{magenta}Please Choose A{reset} {green}Valid{reset} {magenta}Tool From The Toolbox [EX: 3]{reset}: ")
    else:
        return chosen_tool


# Target Prompt
def target(tool_opt: str) -> list:
    if tool_opt == "1":
        t = input(f"{magenta}Please Specify The Target [Ex: 192.168.10.1 Or www.example.com]{reset}: ")
        try:
            t = float(target)
            t = str(target)
        except ValueError:
            try:
                target_ip = socket.gethostbyname(t.lower())
                return (good_status, target_ip)
            except:
                try:
                    socket.gethostbyaddr(t)
                    return (good_status, t)
                except:
                    return (error_status)
        except:
            return (error_status)
    elif tool_opt == "2" or tool_opt == "3" or tool_opt == "4" or tool_opt == "5":
        t = input(f"{magenta}Please Specify The Target [Ex: www.example.com]{reset}: ")
        try:
            target_ip = socket.gethostbyname(t.lower())
            return (good_status, target_ip)
        except:
            try:
                socket.gethostbyaddr(t)
                return (good_status, t)
            except:
                return (error_status)
    elif tool_opt == "6":
        t = input(f"{magenta}Please Specify A Target [Ex: 192.168.10.1]{reset}: ")
        try:
            t = int(t)
            t = str(t)
            return (good_status, t)
        except:
            return (error_status)
    else:
        print(f"{red}[!] Error: Invalid Tool Option{reset}")
        return (invalid_tool_option_status)

# Port And Port Range Prompts
def port() -> list:
    p = input(f"{magenta}Please Specify A Port [Ex: 53]{reset}: ")
    try:
        p = int(p)
        if p > 65535:
            return (invalid_value_status)
        elif p <= 0:
            return (invalid_value_status)
        else:
            return (good_status, p)
    except ValueError:
        return (invalid_value_status)
    except:
        return (error_status)

def port_range() -> list:
    pr = input(f"{magenta}Please Specify A Port Range Seperated By A '-' [Ex: 1-53]{reset}: ")
    try:
        ports = pr.split("-")
        for port in ports:
            port = int(port.split())
        start_port = ports[0]
        end_port = ports[1]
        return (good_status, start_port, end_port)
    except ValueError:
        return (invalid_value_status)
    except:
        return (error_status)

# Tool Option Prompt
def tool_option_prompt(contains_letters: str) -> tuple:
    # Lower Case Roman Alphabet
    lowercase_letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    ]
    # Upper Case Roman Alphabet
    uppercase_letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    # Main Part Of Function
    menu_option = input(f"{magenta}Please Select An Option/Setting From The Menu [Ex: 2]{reset}: ")
    if contains_letters == "f" or "F":
        try:
            menu_option = int(menu_option)
            return (good_status, menu_option)
        except ValueError:
            return (invalid_value_status)
        except:
            return (error_status)
    elif contains_letters == "t" or "T":
        if menu_option in lowercase_letters or uppercase_letters:
            return (good_status, menu_option)
        elif menu_option not in lowercase_letters or uppercase_letters:
            try:
                menu_option = int(menu_option)
                return (good_status, menu_option)
            except:
                return (invalid_value_status)
        else:
            return (error_status)
    else:
        return (error_status)