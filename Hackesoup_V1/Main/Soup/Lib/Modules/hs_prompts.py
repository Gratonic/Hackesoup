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

# Says "Goodbye!" to the user in German and exits the program
def exit_program() -> None:
    print(f"{magenta}\n\nTschüss!{reset}")
    exit()

def menu_prompt(first: int, last: int) -> int:
    while True:
        try:
            user_choice = int(input(f"{magenta}Please Choose An Option From The Menu {green}[Ex: 3]{magenta}:{reset} "))
            status_code = hs_validator.check_user_choice(user_choice, first=first, last=last)
            if status_code == 0:
                return user_choice
        except ValueError:
            print(f"{red}[!] Error: Invalid Option{reset}")
        except KeyboardInterrupt:
            exit_program()
        except:
            print(f"{red}[!] Error: Unknown{reset}")
            exit_program()

def target_IPv4() -> str:
    while True:
        try:
            ipv4_address = str(input(f"{magenta}Please Enter An IPv4 Address {green}[Ex: 192.168.1.1 or 75.124.90.102]: {reset}"))
            status_code = hs_validator.check_IPv4_target(ipv4_address)
            if status_code == 0:
                return ipv4_address
        except KeyboardInterrupt:
            exit_program()
        except:
            print(f"{red}[!] Error: Invalid IPv4 Address{reset}")


def target_website() -> str:
    while True:
        try:
            url = str(input(f"{magenta}Please Enter A URL With The Protocal Included{green}[Ex: https://example.com or https://sub.example.com]: {reset}"))
            status_code = hs_validator.check_web_target(url)
            if status_code == 0:
                return url
        except KeyboardInterrupt:
            exit_program()
        except:
            print(f"{red}[!] Error: Invalid URL{reset}")

def target_combo() -> str:
    while True:
        try:
            target_type = int(input(f"{magenta}Is You Target A Website or IPv4 Address {green}[Enter 1 for a Website and Enter 2 for an IPv4 Address]{magenta}? {reset}"))
            status_code = hs_validator.check_user_choice(target_type, first=1, last=2)
            if status_code == 0:
                if target_type == 1:
                    target = target_website()
                    return target
                elif target_type == 2:
                    target = target_IPv4()
                    return target
        except KeyboardInterrupt:
            exit_program()
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

def port() -> int:
    while True:
        try:
            port = str(input(f"{magenta}Please Enter A Port Number {green}[Ex: 53]{magenta}: {reset}"))
            status_code = hs_validator.check_port(port)
            if status_code == 0:
                return int(port)
        except KeyboardInterrupt:
            exit_program()
        except:
            pass

def port_range() -> list:
    while True:
        try:
            port_range = str(input(f"{magenta}Please Enter A Port Range Seperated By A '-' {green}[Ex: 1-49151]{magenta}: {reset}"))
            status_code = hs_validator.check_port_range(port_range)
            if status_code == 0:
                ports = port_range.split("-")
                return ports
        except KeyboardInterrupt:
            exit_program()
        except:
            print(f"{red}[!] Error: Unknown{reset}")
            exit_program()

def timeout() -> int:
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
            exit_program()
        except ValueError:
            print(f"{red}[!] Error: Invalid Input{reset}")
        except:
            print(f"{red}[!] Error: Unknown{reset}")
            exit_program()

def thread_amount() -> int:
    while True:
        try:
            thread_amount = int(input(f"{magenta}Please Enter A Thread Amount {green}[Ex: 2]{magenta}: {reset}"))
            # NOTE: Result of this validator function is very simular to the validator function used in the 'timeout' function
            validator_result = hs_validator.check_thread_amount(thread_amount)
            thread_amount = validator_result[1]
            return thread_amount
        except KeyboardInterrupt:
            exit_program()
        except ValueError:
            print(f"{red}[!] Error: Invalid Input{reset}")
        except:
            print(f"{red}[!] Error: Unknown{reset}")
            exit_program()

# NOTE: This function does not work at the moment and the payload file options are currently unavailable
def payload_file_path() -> str:
    try:
        print(f"{red}[!] Notice: The {yellow}Payload File Selection {red} Is Currently Unavailable. Sorry For The Inconvenience.{reset}")
        time.sleep(3)
        file_path = "NA"
        return file_path
    except KeyboardInterrupt:
        exit_program()
    except:
        print(f"{red}[!] Error: Unknown{reset}")
        exit_program()
    # while True:
    #     try:
    #         payload_file_path = str(input(f"{magenta}Please Enter Your Payload File Path {green}[Ex: ~/../../etc/passwd]{magenta}: {reset}"))
    #         # NOTE: Result of this validator function is very simular to the validator function used in the 'timeout' function
    #         validator_result = hs_validator.check_file_path(payload_file_path)
    #         payload_file = validator_result[1]
    #         return payload_file_path
    #     except KeyboardInterrupt:
    #         exit_program()
    #     except:
    #         print(f"{red}[!] Error: Unknown{reset}")
    #         exit_program()