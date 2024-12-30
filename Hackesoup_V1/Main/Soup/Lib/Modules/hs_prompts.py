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

# Toolbox Prompt - Used for Main/Tool Menu only!
def toolbox() -> int:
    while True:
        tool = input(f"{magenta}Please Choose An Option From The Toolbox{reset} {green}[Ex: 3]{reset}: ")
        try:
            tool = int(tool)
            # 7 because of easter egg, number will be changed to a higher number in future versions
            if tool >= 0 and tool <= 7:
                return tool
            else:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Tool.{reset}")
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Tool.{reset}")

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

# Target Prompt - IP Address Only!
def target() -> str:
    while True:
        try:
            targ = input(f"{magenta}Please Specify a Target{reset} {green}[Ex: 74.203.143.35]{reset}: ")
            octets = targ.split(".")
            try:
                good_octets = []
                for octet in octets:
                    octet = int(octet)
                    if octet >= 1 and octet <= 255:
                        good_octets.append(octet)
                    else:
                        print(f"{red}[!] Error{reset}: One Or More Octets Are Invalid.{reset}")
                        break
            except:
                print(f"{red}[!] Error{reset}: One Or More Octets Are Invalid.{reset}")
            # Returns the target if there are enough good octets
            if len(good_octets) == 4:
                return targ
            else:
                continue
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Target.{reset}")

# Special Target Prompt - IP Address and Website Domains Accepted!
def special_target() -> str:
    while True:
        try:
            targ = input(f"{magenta}Please Specify a Target{reset} {green}[Ex: 74.203.143.35 or www.example.com]{reset}: ")
            target_pieces = targ.split(".")
            if len(target_pieces) == 4:
                try:
                    # just to make things more readable
                    octets = target_pieces
                    # container for the good octets
                    good_octets = []
                    for octet in octets:
                        octet = int(octet)
                        if octet >= 1 and octet <= 255:
                            good_octets.append(octet)
                        else:
                            print(f"{red}[!] Error{reset}: One Or More Octets Are Invalid.{reset}")
                            break
                    # if everything goes well...
                    if len(good_octets) == 4:
                        return targ
                except socket.gaierror:
                    print(f"{red}[!] Error{reset}: One Or More Octets Are Invalid.{reset}")
            elif len(target_pieces) > 4 or len(target_pieces) < 4:
                try:
                    # NOTE: The website ip address is not actually used, it just means the website must exist -->
                    # since it has an ip address
                    website_ip = socket.gethostbyname(targ)
                    # if the website ip address was obtained....
                    return targ
                except socket.gaierror:
                    print(f"{red}[!] Erorr:{reset} Invalid Domain Name or IP Address.{light_red}")
                except Exception as e:
                    print(f"{red}[!] Erorr:{reset} {light_red}Unknown.{reset}")
        except KeyboardInterrupt:
            terminate_program()
        except Exception as e:
            print(e)

# Port Prompt
def port() -> int:
    while True:
        prt = input(f"{magenta}Please Specify A Port {green}[Ex: 21]{reset}: ")
        try:
            prt = int(port)
            # 65535 is the last port number
            if prt > 65535:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Port.{reset}")
            elif prt < 1:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Port.{reset}")
            else:
                return prt
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Port.{reset}")

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
                print(f"{red}[!] Error{reset}: {light_red}Invalid Port Range.{reset}")
            elif start_prt < 1 or end_prt < 1:
                print(f"{red}[!] Error{reset}: {light_red}Invalid Port Range.{reset}")
            else:
                return prt_range
        except KeyboardInterrupt:
            terminate_program()
        except:
            print(f"{red}[!] Error{reset}: {light_red}Invalid Port Range.{reset}")

# Custom Payload File Prompt
def custom_payload_file() -> str:
    while True:
        pay_file_path = input(f"{magenta}Please Specify The Path To Your Payload File{reset} {green}[Ex: ./Payloads/your_payloads.txt]{reset}: ")
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