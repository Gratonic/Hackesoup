import colorama
import socket
import psutil # Written and Licensed by Giampaolo Rodola, https://github.com/giampaolo/psutil
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

# Used for some functions to determine the amount of threads the user can safely use for the program
def find_safe_thread_amount() -> int:
    thread_count = psutil.cpu_count(logical=True)
    thread_amount_allowed_for_program = round(int(thread_count / 2))
    return thread_amount_allowed_for_program

# Says "Goodbye!" to the user in German and exits the program
def terminate_program() -> None:
    print(f"{magenta}\n\nTschüss!{reset}")
    exit()

# Checks an IP Address - Used in the target prompt functions - ocs == list of octets
def check_ip(ocs: list) -> int:
    # NOTE: 0 == all-good status, 1 == stanard error status (invalid ip), -->
    # 2 == missing octets status, 3 == too many octets status
    #
    # Stores the valid octets
    good_octets = []
    # If there are 4 octets keep going, if there are less than 4 return the too many octets status, -->
    #  if there are less than 4 ocets return the missing octets status, else return the stanard error status
    if len(ocs) == 4:
        pass
    elif len(ocs) < 4:
        return 2
    elif len(ocs) > 4:
        return 3
    else:
        return 1
    # Checks every octet in the octets list
    for octet in ocs:
        try:
            octet = int(octet)
            # 255 is for the broadcast address only in all cases 254 is last usable
            if octet > 0 and octet < 254:
                good_octets.append(octet)
            else:
                return 1
        except:
            return 1
    # All ip address contain 4 octets, no less and no more
    if len(good_octets) == 4:
        return 0
    else:
        return 1

# Main/Tool Menu Prompt
def toolbox() -> int:
    while True:
        try:
            # Asks the user to choose a tool, integer expected
            tool_choice = int(input(f"{magenta}Please Choose A Tool Number {green}[EX: 3]{magenta}:{reset} "))
            # 0 == exit, 7 == previous menu (7 will trigger an easter egg in this case)
            if tool_choice >= 0 and tool_choice <= 7:
                return tool_choice
            else:
                print(f"{red}[!] Error: {light_red}Tool Choice Out Of Scope{reset}")
        except ValueError:
            print(f"{red}[!] Error: {light_red}Please Choose A Number.{reset}")
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error: {light_red}Invalid Tool Choice.{reset}")

# Target Prompt - IP Address Only!
def target() -> str:
    while True:
        try:
            # Asks the user to specify their target, ip address expected
            target = str(input(f"{magenta}Please Specify A Target {green}[EX: 1.1.1.1]{magenta}:{reset} "))
            # If there are no dots in the string, the user must have not entered an IP Address
            if "." in target:
                # Used to store the octets that have not been validated
                octets = target.split(".")
                # Checks the ip address, 0 == all-good status, 1 == stanard error status (invalid ip), -->
                # 2 == missing octets status, 3 == too many octets status
                ip_check_status = check_ip(octets)
                # Determines what to do based on the status returned
                if ip_check_status == 0:
                    return target
                elif ip_check_status == 1:
                    print(f"{red}[!] Error: {light_red}Invalid IP Address.{reset}")
                elif ip_check_status == 2:
                    print(f"{red}[!] Error: {light_red}One Or More Octets Are Missing.{reset}")
                elif ip_check_status == 3:
                    print(f"{red}[!] Error: {light_red}Too Many Octets.")
                else:
                    print(f"{red}[!] Error: {light_red}Unknown, Please Try Again.{reset}")
            else:
                print(f"{red}[!] Error: {light_red}You Must Specify An IP Address.{reset}")
        except KeyboardInterrupt:
            terminate_program()
        except Exception as e:
            # Prints the error because the user will likely never cause this error, -->
            # since all the input validation is done above in another try-except block
            print(e)

# Special Target Prompt - Website or IP Address
def special_target() -> str:
    # Gets the target type
    while True:
        try:
            target_type = int(input(f"{magenta}Is Your Target Address A Website or IP Address? {green}[Enter 1: For A Website, Enter 2: For An IP Address]: {reset}"))
            if target_type == 1 or target_type == 2:
                break
            else:
                print(f"{red}[!] Error: {light_red}Invalid Target Type.{reset}")
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error: {light_red}Target Type Must Be A Number.{reset}")
    # Gets the target based on the target_type and preforms the proper validation
    while True:
        try:
            # Asks the user to specify their target, ip address expected
            target = str(input(f"{magenta}Please Specify A Target {green}[EX: 1.1.1.1]{magenta}:{reset} "))
            # If target is a web address (website)
            if target_type == 1:
                try:
                    socket.gethostbyname(target)
                    return target
                except KeyboardInterrupt:
                    terminate_program()
                except:
                    print(f"{red}[!] Error: {light_red}Invalid Website.{reset}")
            elif target_type == 2:
                # If there are no dots in the string, the user must have not entered an IP Address
                if "." in target:
                    # Used to store the octets that have not been validated
                    octets = target.split(".")
                    # Checks the ip address, 0 == all-good status, 1 == stanard error status (invalid ip), -->
                    # 2 == missing octets status, 3 == too many octets status
                    ip_check_status = check_ip(octets)
                    # Determines what to do based on the status returned
                    if ip_check_status == 0:
                        return target
                    elif ip_check_status == 1:
                        print(f"{red}[!] Error: {light_red}Invalid IP Address.{reset}")
                    elif ip_check_status == 2:
                        print(f"{red}[!] Error: {light_red}One Or More Octets Are Missing.{reset}")
                    elif ip_check_status == 3:
                        print(f"{red}[!] Error: {light_red}Too Many Octets.")
                    else:
                        print(f"{red}[!] Error: {light_red}Unknown, Please Try Again.{reset}")
                else:
                    print(f"{red}[!] Error: {light_red}You Must Specify An IP Address.{reset}")
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error: Invalid Target.{reset}")

# Setup Prompt - Used for tool setting/setup menus
def setup(tool_number: int) -> int:
    def option_out_of_scope():
        print(f"{red}Erorr: {reset}{light_red}Invalid setup option. The number you have chosen is out of scope.{reset}")
    try:
        while True:
            try:
                setup_option = int(input(f"{magenta}Please Choose A Setup Option{reset} {green}[Ex: 2]{reset}: "))
                # Returns an integer if one of the conditions below are met -->
                # otherwise the user will recieve a custom erorr message
                if tool_number == 1:
                    if setup_option >= 0 and setup_option <= 7:
                        return setup_option
                    else:
                        option_out_of_scope()
                elif tool_number == 2:
                    if setup_option >= 0 and setup_option <= 13:
                        return setup_option
                    else:
                        option_out_of_scope()
                elif tool_number == 3:
                    if setup_option >= 0 and setup_option <= 13:
                        return setup_option
                    else:
                        option_out_of_scope()
                    return setup_option
                elif tool_number == 4:
                    if setup_option >= 0 and setup_option <= 13:
                        return setup_option
                    else:
                        option_out_of_scope()
                elif tool_number == 5:
                    if setup_option >= 0 and setup_option <= 13:
                        return setup_option
                    else:
                        option_out_of_scope()
                elif tool_number == 6:
                    if setup_option >= 0 and setup_option <= 6:
                        return setup_option
                    else:
                        option_out_of_scope()
                else:
                    raise ValueError(f"{red}'tool_number [{tool_number}]' is out of scope{reset}")
            except ValueError:
                print(f"{red}[!] Error{reset}: {light_red}Invalid setup option. Please enter a number.{reset}")
            except:
                print(f"{red}[!] Error{reset}: {light_red}Invalid setup option.{reset}")
    except KeyboardInterrupt:
        terminate_program()
    except ValueError:
        raise ValueError(f"{red}'tool_number [{tool_number}]' must be an integer")
    except Exception as error:
        print(error)

# Port Prompt
def port() -> int:
    while True:
        try:
            port = int(input(f"{magenta}Please Specify A Port Number {green}[EX: 53]: {reset}"))
            if port < 1:
                print(f"{red}[!] Error: {light_red}Port Number Is Too Low.{reset}")
            elif port > 65535:
                print(f"{red}[!] Error: {light_red}Port Number Is Too High.{reset}")
            else:
                return port
        except KeyboardInterrupt:
            terminate_program()
        except ValueError:
            print(f"{red}[!] Error: {light_red}You Must Enter A Number.{reset}")
        except:
            print(f"{red}[!] Error: {light_red}Invalid Port.{reset}")

# Port Range Prompt
def port_range() -> str:
    while True:
        prt_range = input(f"{magenta}Please Specify A Port Range Seperated By Spaces{reset} {green}[Ex: 1-53]{reset}: ")
        try:
            prts = prt_range.split("-")
            start_prt = int(prts[0])
            end_prt = int(prts[1])
            # 65535 is the last port number
            if start_prt > 65535 or end_prt > 65535:
                print(f"{red}[!] Error{reset}: {light_red}One Or More Port Number(s) Are/Is Too High.{reset}")
            elif start_prt < 1 or end_prt < 1:
                print(f"{red}[!] Error{reset}: {light_red}One Or More Port Number(s) Are/Is Too Low.{reset}")
            else:
                return prt_range
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Port Range.{reset}")

# Custom Payload File Prompt
def custom_payload_file() -> str:
    while True:
        pay_file_path = input(f"{magenta}Please Specify The Path To Your Payload File{reset} {green}[Ex: ../Payloads/your_payloads.txt]{reset}: ")
        try:
            # Splits the file path up for basic validation
            pay_path_contents = re.split("[\\/]", pay_file_path)
            # Grabbing the payload file for basic validation
            pay_file_contents = pay_path_contents[-1]
            pay_file_contents = pay_file_contents.split(".")
            pay_file = pay_file_contents[-1]
            if pay_file == "txt":
                return pay_file_path
            elif pay_file == "text":
                return pay_file_path
            else:
                print(f"{red}[!] Error{reset}: {light_red}Invalid File Path or File Type (file type must be {reset}{green}.txt or .text{reset}{light_red}).{reset}")
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid File Path or File Type (file type must be {reset}{green}.txt or .text{reset}{light_red}).{reset}")

# Timeout Amount Prompt
def timeout_amount() -> int:
    while True:
        timeout = input(f"{magenta}Please Specify The Timeout Amount{reset} {green}[Ex: '3' is 3 seconds]{reset}: ")
        try:
            timeout = int(timeout)
            return timeout
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Input. Numbers Only!{reset}")

# Thread Amount Prompt
def thread_amount() -> int:
    safe_thread_amount = find_safe_thread_amount()
    while True:
        thread_amount = input(f"{magenta}Please Specify The Thread Amount{reset} {green}[Ex: 4]{reset}: ")
        try:
            thread_amount = int(thread_amount)
            if thread_amount > safe_thread_amount:
                print(f"{red}[!] Error{reset}: {light_red}Too Many Threads. You May Use Up To {reset}{green}{safe_thread_amount}{reset}{light_red} Threads For This Computer, Using More Could Overload Your CPU.{reset}")
            else:
                return thread_amount
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Input. Numbers Only!{reset}")

# Timeout and Thread Amount Prompt
def timeout_and_thread_amount() -> list:
    safe_thread_amount = find_safe_thread_amount()
    while True:
        timeout = input(f"{magenta}Please Specify The Timeout Amount{reset} {green}[Ex: '3' is 3 seconds]{reset}: ")
        thread_amount = input(f"{magenta}Please Specify The Thread Amount{reset} {green}[Ex: 4]{reset}: ")
        try:
            timeout = int(timeout)
            thread_amount = int(thread_amount)
            if thread_amount > safe_thread_amount:
                print(f"{red}[!] Error{reset}: {light_red}Too Many Threads. You May Use Up To {reset}{green}{safe_thread_amount}{reset}{light_red} Threads For This Computer, Using More Could Overload Your CPU.{reset}")
            else:
                return [timeout, thread_amount]
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Input. Numbers Only!{reset}")

# Custom Payload File Prompt + Timeout and Thread Amount Prompt
def custom_payload_file_plus_timeout_and_thread_amount() -> list:
    safe_thread_amount = find_safe_thread_amount()
    while True:
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
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Something Went Wrong During The File Validation Process.{reset}")
        try:
            timeout = int(timeout)
            thread_amount = int(thread_amount)
            if thread_amount > safe_thread_amount():
                print(f"{red}[!] Error{reset}: {light_red}Too Many Threads. You May Use Up To {reset}{green}{safe_thread_amount}{reset}{light_red} Threads For This Computer, Using More Could Overload Your CPU.{reset}")
            else:
                # Safe to break the loop here because everything must go well to reach this point
                return [pay_file_path, timeout, thread_amount]
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Input! Numbers Only!{reset}")