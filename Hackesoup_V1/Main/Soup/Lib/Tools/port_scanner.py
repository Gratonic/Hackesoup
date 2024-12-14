import socket
import colorama

# color objects, used for nicer output
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

# Creates the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

for port in range(1000):
    result = s.connect_ex(("127.0.0.1", port))
    if result == 0:
        print(f"{green}Port {port} is open{reset}")
    else:
        print(f"{red} Port {port} is closed{reset}")