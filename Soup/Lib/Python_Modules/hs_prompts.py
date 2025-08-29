# :: Imports :: #

from datetime import datetime
import colorama
import hs_validator
import time
import os

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

# -- Terminal Clear -- #

def clear_terminal():
    # Check the operating system and clear the terminal
    if os.name == 'posix':
        # For Unix-like systems (Linux, macOS)
        os.system('clear')
    else:
        # For Windows
        os.system('cls')

# -- Exit Functions -- #

# Says a simple "Goodbye!" to the user in German and exits the program
def exit_program_main() -> None:
    print(f"{magenta}\n\nTschüss!{reset}")
    exit()

# Says "Goodbye!" to the user and exits the program
def exit_program_soupemapper() -> None:
    print(f"{magenta}\n\nGood luck and goodbye!{reset}")
    exit()

# Says "Goodbye!" to the user in Arabic and exits the program
def exit_program_serikandor() -> None:
    print(f"{magenta}\n\nשיהיה לך יום שקט ולהתראות לעת עתה!{reset}")
    exit()

# Says "Goodbye!" to the user in Spanish and exits the program
def exit_program_mudelatie() -> None:
    print(f"{magenta}\n\nRecuerda, cada final es un nuevo comienzo. ¡Adios por ahora!{reset}")
    exit()

# Says "Goodbye!" to the user in German and exits the program
def exit_program_baumspinne() -> None:
    print(f"{magenta}\n\nVielen Dank für Ihre Unterstützung und die Zusammenarbeit. Wünschend Ihnen alles Gute für die Zukunft. Auf Wiedersehen!{reset}")
    exit()

def exit_program_dabijar() -> None:
    print(f"{magenta}\n\nFino alla prossima volta! Arrivederci!{reset}")
    exit()

# Says "Goodbye!" and best of luck in Croation
def exit_program_patchpirate() -> None:
    print(f"{magenta}\n\nSvako dobro i doviđenja!{reset}")
    exit()

# Checks the users chosen configuration option to see if they want to exit the program
def exit_program(tool_name: str) -> None:
    if tool_name == "NA":
        exit_program_main()
    elif tool_name == "patchpirate":
        exit_program_patchpirate()
    elif tool_name == "serikandor":
        exit_program_serikandor()
    elif tool_name == "dabijar":
        exit_program_dabijar()
    elif tool_name == "mudelatie":
        exit_program_mudelatie()
    elif tool_name == "baumspinne":
        exit_program_baumspinne()
    elif tool_name == "soupemapper":
        exit_program_soupemapper()
    else:
        print(f"{red}Error: Unknown{reset}")
        exit_program_main()

# -- Main Functions -- #

# Menu Option Prompt

def menu_prompt(first: int, last: int, tool_name: str) -> int:
    while True:
        try:
            user_choice = int(input(f"{magenta}Please Choose An Option From The Menu {green}[Ex: 1]{magenta}:{reset} "))
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

# Target Prompts

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
            url = str(input(f"{magenta}Please Enter A Target URL {green}[Ex: https://example.com or sub.example.com]{magenta}: {reset}"))
            # [0] is 0 or 1, [1] is the domain name
            domain_name = hs_validator.check_web_target(url)
            if domain_name[0] == 0:
                return domain_name
            else:
                print(f"{red}[!] Error: Invalid URL{reset}")
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except:
            print(f"{red}[!] Error: Invalid URL{reset}")

def target_username(tool_name: str) -> str:
    while True:
        try:
            target = str(input(f"{magenta}Please Enter A Username To Target {green}[Ex: CrashOverride or AcidBurn]: {reset}"))
            return target
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except Exception as e:
            print(f"{red}[!] Error: Invalid Username{reset}")

# API Token Prompt

def api_token(tool_name: str) -> str:
    while True:
        try:
            api_token = str(input(f"{magenta}Please Enter An API Token {green}[Ex: AbCDEfGHi...]{magenta}: {reset}"))
            return api_token
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except:
            print(f"{red}[!] Error: Unknown{reset}")

# Port and Port Range Prompts

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

# RPM (Requests Per Minute) and Timeout Prompts

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

def requests_per_minute(tool_name: str) -> int:
    while True:
        try:
            rpm = int(input(f"{magenta}Please Enter A Number For The Request Per Minute Amount {green}[Ex: 300]{magenta}: {reset}"))
            if rpm > 1 and rpm < 7500:
                return rpm
            elif rpm > 7500:
                print(f"{red}[!] Error: Too High, Please Choose A Smaller Number{reset}")
                continue
            elif rpm < 1:
                print(f"{red}[!] Error: Too Low, Please Choose A Bigger Number{reset}")
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except:
            print(f"{red}[!] Error: Unknown{reset}")
            exit_program(tool_name=tool_name)

# Save To File and Payload File Prompts

def save_to_file(tool_name: str) -> list:
    while True:
        try:
            save = input(f"{magenta}Would You Like To Save The Tools Output To A JSON File? {green}[y/n]{magenta}: {reset}")
            if save == "y" or save == "Y" or save == "yes" or save == "YES":
                current_time = str(datetime.now())
                current_time = current_time.split(" ")
                date = current_time[0]
                time_now =  current_time[1].split(".")[0]
                
                # this path is used by the tool files, so the current location will be Interfaces (location of the interface files [aka the ones used to run the program])
                save_file_path = f"../Saves/{tool_name}_{date}_{time_now}.json"

                print(f"{magenta}[*] The tool output will be saved at {cyan}{save_file_path}{reset}")
                time.sleep(3)
                return [True, save_file_path]
            elif save == "n" or save == "N" or save == "no" or save == "NO":
                return [False, "NA"]
            else:
                print(f"{red}[!] Error: Invalid Input{reset}")
        except KeyboardInterrupt:
            exit_program(tool_name=tool_name)
        except Exception as e:
            print(f"{red}[!] Error: An unknown error has occured while asking the user if they want to save the tool output.{reset}")
            print("\n")
            print(e)
            exit_program(tool_name=tool_name)