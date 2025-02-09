# :: Imports :: #
import colorama
import hs_validator

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

def menu_prompt(first: int, last: int):
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

def target_IPv4():
    pass

def target_website():
    pass

def target_combo():
    pass

def port():
    pass

def port_range():
    pass

def thread_amount():
    pass

def file_path():
    pass
