# :: Imports :: #
import colorama
import hs_validator
import time

# :: Global Variables :: #

# Colors
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

# :: Functionality :: #

# Says "Goodbye!" to the user and exits the program
def exit_program_port_scanner():
    print(f"{magenta}\n\nGood luck and goodbye!{reset}")
    exit()

# Says "Goodbye!" to the user in Arabic and exits the program
def exit_program_subdomain_finder():
    print(f"{magenta}\n\nغزة تنهي هذا اللقاء، لكنها لا تنتهي!{reset}")
    exit()

# Says "Goodbye!" to the user in Spanish and exits the program
def exit_program_XSS_scanner():
    print(f"{magenta}\n\nRecuerda, cada final es un nuevo comienzo. ¡Adios por ahora!{reset}")
    exit()

# Says "Goodbye!" to the user in German and exits the program
def exit_program_dir_trav_scanner():
    print(f"{magenta}\n\nVielen Dank für Ihre Unterstützung und die Zusammenarbeit. Wünschend Ihnen alles Gute für die Zukunft. Auf Wiedersehen!{reset}")
    exit()

def exit_program_SQLI_scanner():
    print(f"{magenta}\n\nFino alla prossima volta! Arrivederci!{reset}")
    exit()

def exit_program_destroyer():
    print(f"{magenta}\n\nज्ञान को अपने जीवन का हिस्सा बनाइए क्योंकि यह आपकी सबसे बड़ी शक्ति है, लेकिन इसका इस्तेमाल दुनिया को बेहतर बनाने के लिए करें, न कि उसे नष्ट करने के लिए। अभी के लिए अलविदा!{reset}")
    exit()

def exit_program(tool_name: str):
    if tool_name == "port_scanner":
        exit_program_port_scanner()
    elif tool_name == "subdomain_finder":
        exit_program_subdomain_finder()
    elif tool_name == "XSS_scanner":
        exit_program_XSS_scanner()
    elif tool_name == "dir_trav_scanner":
        exit_program_dir_trav_scanner()
    elif tool_name == "SQLI_scanner":
        exit_program_SQLI_scanner()
    elif tool_name == "destroyer":
        exit_program_destroyer()
    else:
        print(f"{magenta}\n\nTschüss{reset}")
        exit()

def menu_prompt(first: int, last: int, tool_name: str) -> int:
    while True:
        try:
            user_choice = int(input(f"{magenta}Please Choose An Option From The Menu {green}[Ex: 3]{magenta}:{reset} "))
            status_code = hs_validator.check_user_choice(user_choice, first=first, last=last)
            if status_code == 0:
                return user_choice
        except ValueError:
            print(f"{red}[!] Error: Invalid Option{reset}")
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except:
            print(f"{red}[!] Error: Unknown{reset}")
            exit_program(tool_name=tool_name)

def target_IPv4(tool_name: str) -> str:
    while True:
        try:
            ipv4_address = str(input(f"{magenta}Please Enter A Target IPv4 Address {green}[Ex: 192.168.1.1 or 75.124.90.102]: {reset}"))
            status_code = hs_validator.check_IPv4_target(ipv4_address)
            if status_code == 0:
                return ipv4_address
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except:
            print(f"{red}[!] Error: Invalid IPv4 Address{reset}")


def target_website(tool_name: str) -> str:
    while True:
        try:
            url = str(input(f"{magenta}Please Enter A Target URL With The Protocal Included {green}[Ex: https://example.com or https://sub.example.com]: {reset}"))
            status_code = hs_validator.check_web_target(url)
            if status_code == 0:
                return url
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except:
            print(f"{red}[!] Error: Invalid URL{reset}")

def target_combo(tool_name: str) -> str:
    while True:
        try:
            target_type = int(input(f"{magenta}Is Your Target A Website or IPv4 Address {green}[Enter 1 for a Website and Enter 2 for an IPv4 Address]{magenta}? {reset}"))
            status_code = hs_validator.check_user_choice(target_type, first=1, last=2)
            if status_code == 0:
                if target_type == 1:
                    target = target_website()
                    return target
                elif target_type == 2:
                    target = target_IPv4()
                    return target
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except ValueError:
            # NOTE: A Base10 integer error can occur sometimes when an invalid website is entered, it's hard to trigger -->
            # and I don't know why it does. This will handle those rare cases.
            if target_type == 2:
                print(f"{red}[!] Error: Invalid Website{reset}")
                print(f"[!] This Is A Critical Error, Restarting Target Prompt...{reset}")
                target_combo()
        except:
            # If exit program is called in this function, the goodbye message will be printed twice during a keyboard interupt
            exit()

def port(tool_name: str) -> int:
    while True:
        try:
            port = str(input(f"{magenta}Please Enter A Port Number {green}[Ex: 53]{magenta}: {reset}"))
            status_code = hs_validator.check_port(port)
            if status_code == 0:
                return int(port)
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except:
            pass

def port_range(tool_name: str) -> list:
    while True:
        try:
            port_range = str(input(f"{magenta}Please Enter A Port Range Seperated By A '-' {green}[Ex: 1-49151]{magenta}: {reset}"))
            status_code = hs_validator.check_port_range(port_range)
            if status_code == 0:
                ports = port_range.split("-")
                start_port = int(ports[0])
                end_port = int(ports[1])
                return [start_port, end_port]
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except:
            print(f"{red}[!] Error: Unknown{reset}")
            exit_program(tool_name=tool_name)

def timeout(tool_name: str) -> int:
    while True:
        try:
            timeout_amount = int(input(f"{magenta}Please Enter An Amount Of Seconds For The Timeout Amount {green}[Ex: 100]{magenta}: {reset}"))
            # NOTE: The result is not important because this validation function will set a default timeout and give the user -->
            # a warning message in the case of an error. 
            # It will return a list containing the status code (not important) at 0 and the timeout amount at 1 (both type: int)
            validator_result = hs_validator.check_timeout(timeout_amount)
            timeout = validator_result[1]
            return timeout
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except ValueError:
            print(f"{red}[!] Error: Invalid Input{reset}")
        except:
            print(f"{red}[!] Error: Unknown{reset}")
            exit_program(tool_name=tool_name)

def thread_amount(tool_name: str) -> int:
    while True:
        try:
            thread_amount = int(input(f"{magenta}Please Enter A Thread Amount {green}[Ex: 2]{magenta}: {reset}"))
            # NOTE: Result of this validator function is very simular to the validator function used in the 'timeout' function
            validator_result = hs_validator.check_thread_amount(thread_amount)
            thread_amount = validator_result[1]
            return thread_amount
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except ValueError:
            print(f"{red}[!] Error: Invalid Input{reset}")
        except:
            print(f"{red}[!] Error: Unknown{reset}")
            exit_program(tool_name=tool_name)

def payload_file_path(tool_name: str) -> str:
    try:
        path = str(input(f"{magenta}Please Enter A Payload File Path or File {green}[Ex: ./payload_file_example.txt]{magenta}: {reset}"))
        validator = hs_validator.check_file_path(path)
        return validator[1]
    # if the user hit [ctrl + c] will exit the program
    except KeyboardInterrupt:
        exit_program(tool_name=tool_name)
    except:
        print(f"{red}[!] Error: Unknown{reset}")
        exit_program(tool_name=tool_name)

def destroyer_file_prompt(tool_name: str) -> str:
    try:
        path = str(input(f"{magenta}Please Enter A File Path or File To Destroy {green}[Ex: ./destroy_me.txt]{magenta}: {reset}"))
        validator = hs_validator.check_file_path(path)
        return validator[1]
    # if the user hit [ctrl + c] will exit the program
    except KeyboardInterrupt:
        exit_program(tool_name=tool_name)
    except:
        print(f"{red}[!] Error: Unknown{reset}")
        exit_program(tool_name=tool_name)

def destroyer_file_overwrite_amount():
    while True:
        try:
            overwrite_amount = int(input(f"{magenta}Please Specify The Amount Of Times You Would Like To Overwrite The File {green}[Ex: 15]{magenta}: {reset}"))
            if overwrite_amount < 0 and overwrite_amount >= 5000:
                return overwrite_amount
            else:
                print(f"{red}[!] Warning: The Requested File Overwrite Amount Is To High, Reducing It To {yellow}5000{reset}")
                try:
                    time.sleep(3)
                    overwrite_amount = 5000
                    return overwrite_amount
                except KeyboardInterrupt:
                    exit_program(tool_name="destroyer")
        except ValueError:
            print(f"{red}[!] Error: You Must Enter A Number")
        except KeyboardInterrupt:
            exit_program(tool_name="destroyer")
        except:
            print(f"{red}[!] Error: Unknown")