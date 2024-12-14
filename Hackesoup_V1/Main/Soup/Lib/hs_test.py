# TODO: Use scrapy to modify the packet headers of the sent data in order to implement a stealth scanning feature
import socket
# Imports the concurrent futures module for thread pool
import concurrent.futures
import argparse
import textwrap
import colorama
import time

# Creates the colour objects to use for nicer output
reset = colorama.Fore.RESET
blue = colorama.Fore.LIGHTBLUE_EX
cyan = colorama.Fore.LIGHTCYAN_EX
red = colorama.Fore.RED
green = colorama.Fore.GREEN
yellow = colorama.Fore.LIGHTYELLOW_EX
magenta = colorama.Fore.MAGENTA

print(f"""{green}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{reset}
       {cyan}____  ____  ____  ______   _____ _________    _   ___   ____________ 
      / __ \/ __ \/ __ \/_  __/  / ___// ____/   |  / | / / | / / ____/ __ \ 
     / /_/ / / / / /_/ / / /     \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
    / ____/ /_/ / _, _/ / /     ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/ 
   /_/    \____/_/ |_| /_/     /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|{reset}
                                                                         
{green}::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{reset}
""")

# Insures the command-line arguments only work if the program is being run directly
if __name__ == "__main__":
    # Command-Line arguments and help information
    parser = argparse.ArgumentParser(prog="Port Scanner",
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    epilog=textwrap.dedent(f'''
                                    {magenta}Quick, Beautiful, and Helpful Information:{reset}
                                    
                                    {blue}1) port_scanner.py{reset} {cyan}-t{reset} {blue}192.168.1.1{reset} {yellow}# target{reset}
                                    {blue}*) port_scanner.py{reset} {cyan}--target{reset} {blue}192.168.1.1{reset} {yellow}# target{reset}
                                    {blue}2) port_scanner.py{reset} {cyan}-p{reset} {blue}1{reset} {yellow}# single port{reset}
                                    {blue}*) port_scanner.py{reset} {cyan}--port{reset} {blue}1{reset} {yellow}# single port{reset}
                                    {blue}3) port_scanner.py{reset} {cyan}-r{reset} {blue}1-50000{reset} {yellow}# port range{reset}
                                    {blue}*) port_scanner.py{reset} {cyan}--range{reset} {blue}1-50000{reset} {yellow}# port range{reset}
                                    {blue}4) port_scanner.py{reset} {cyan}-w{reset} {blue}1{reset} {yellow}# timeout{reset}
                                    {blue}*) port_scanner.py{reset} {cyan}--wait{reset} {blue}1{reset} {yellow}#timeout{reset}
                                    {blue}5) port_scanner.py{reset} {cyan}-d{reset} {blue}5{reset} {yellow}# amount of threads to use{reset}
                                    {blue}*) port_scanner.py{reset} {cyan}--threads{reset} {blue}5{reset} {yellow}# amount of threads to use{reset}
                                    {blue}6) port_scanner.py{reset} {cyan}-s{reset} {yellow}# stealth scan{reset}
                                    {blue}*) port_scanner.py{reset} {cyan}--stealth{reset} {yellow}# stealth scan{reset}
                                    '''))
    parser.add_argument("-p", "--port", type=str, help="Specify a single port | Example: -p 80")
    parser.add_argument("-r", "--range", type=str, help="Specify a port-range, separated by a dash | Example: -r 1-50000")
    parser.add_argument("-t", "--target", type=str, help="Specify target ip address, needs a port argument | Example: -t 192.168.1.1 -r 1-443 | Default is 192.168.1.1")
    parser.add_argument("-w", "--wait", type=int, help="Determines how long to wait for each connection to each port before timing out, interpreted as seconds | Example: -c 1 | Default 1")
    parser.add_argument("-d", "--threads", type=int, help="Specify the amount of threads to use, although more threads can mean a faster port-scan...make sure not to use too many threads, enter an integer | Example: -d 5 | Default for a Normal Scan is 5, Default for a Stealth Scan is 3")
    parser.add_argument("-s", "--stealth", help="Perform a stealth scan, warning takes longer if you use threads default settings because less threads are used for a stealth scan to optimize system performance")
    args = parser.parse_args()

# User input validation
if not args.target:
    print(f"{red}[!] Error:{reset} {yellow}You must specify a target ip address.{reset}")
elif not args.port and not args.range:
    print(f"{red}[!] Error:{reset} {yellow}You must specify a port or port-range.{reset}")
elif args.port and args.range:
    print(f"{red}[!] Error:{reset} {yellow}You must specify a port or port-range but not both.{reset}")

# Port scanner functionality
class port_scan():
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
    # Calculates the estimated port-scan time remaining
    def time_remaining_calculater(self):
        # Values to use for calculating the time remaining
        if self.args.wait and self.args.threads and self.args.range:
            start_port, end_port = map(int, self.args.range.split("-"))
            thread_amount = self.args.threads
            wait_time = self.args.wait
            start_time = round(end_port / thread_amount * wait_time)
        elif self.args.wait and self.args.range and self.args.stealth and not self.args.threads:
            start_port, end_port = map(int, self.args.range.split("-"))
            thread_amount = 3
            wait_time = self.args.wait
            start_time = round(end_port / thread_amount * wait_time)
        elif self.args.wait and self.args.range and not self.args.threads and not self.args.stealth:
            start_port, end_port = map(int, self.args.range.split("-"))
            thread_amount = 5
            wait_time = self.args.wait
            start_time = round(end_port / thread_amount * wait_time)
        elif self.args.threads and self.args.range and not self.args.wait:
            start_port, end_port = map(int, self.args.range.split("-"))
            thread_amount = self.args.threads
            wait_time = 1
            start_time = round(end_port / thread_amount * wait_time)
        elif self.args.stealth and self.args.range and not self.args.wait and not self.args.threads:
            start_port, end_port = map(int, self.args.range.split("-"))
            thread_amount = 3
            wait_time = 1
            start_time = round(end_port / thread_amount * wait_time)
        else:
            start_port, end_port = map(int, self.args.range.split("-"))
            thread_amount = 5
            wait_time = 1
            start_time = round(end_port / thread_amount * wait_time)
        # Time remaining counter functionality
        for sec in range(start_time, 0, -1):
            # Calculate seconds
            seconds = int(sec % 60)
            # Calculate minutes
            minutes = int(sec / 60)
            # Calculate hours, NOTE: there are 3600 seconds in an hour
            hours = int(sec / 3600)
            # Prints the estimated time remaining to the console
            # NOTE: "\r" makes sure the message is not printed on a new line each time and "flush=True" -->
            # clears the previous message printed on the line and the :02 formats the values, a zero -->
            # fills in any empty space (the 2 represents the amount of spaces)
            print(f"{blue}Estimated Time Remaining:{reset} {cyan}{hours:02}:{minutes:02}:{seconds:02}{reset}", end="\r", flush=True)
            time.sleep(1)
    def scan_single_port(self):
        if self.args.target and self.args.port:
            self.args.port = int(self.args.port)
            print(f"{magenta}[-] Scanning {self.args.target}:{self.args.port}{reset}\n")
            self.scan(self.args.target, self.args.port)
    def scan_port_range(self):
        # Determines the amount of threads (workers) to be used
        if self.args.threads:
            max_worker_amount = self.args.threads
        elif self.args.stealth and not self.args.threads:
            max_worker_amount = 3
        else:
            max_worker_amount = 5
        # Using ThreadPoolExecutor to manage a pool of threads
        if self.args.target and self.args.range:
            start_port, end_port = map(int, self.args.range.split("-"))
            end_port += 1
            print(f"{magenta}[-] Scanning {self.args.target}:{start_port}-{end_port - 1}{reset}\n")
            self.time_remaining_calculater()
            # Creates a thread pool with the specified number of threads
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_worker_amount) as executor:
                # Submit tasks to the thread pool
                futures = {executor.submit(self.scan, self.args.target, port): port for port in range(start_port, end_port)}
                # Wait for each future to complete and handle results
                for future in concurrent.futures.as_completed(futures):
                    port = futures[future]  # Get the port associated with the future
                    try:
                        future.result()  # Get the result of the scan (this will raise an exception if the scan failed)
                    except Exception as e:
                        print(f"{red}[!] Error:{reset} {yellow}An error occurred while scanning port {port}: {e}{reset}")
            # Exits the program, preventing the Time Remaining Calc function from restarting and -->
            # running again for a second or two before the program ends
            exit()
    def scan(self, target, port):
        try:
            if self.args.wait:
                timeout = self.args.wait
            else:
                timeout = 1
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"{yellow}__________________________________{reset}")
                    print(f"\n{blue}Port{reset} {cyan}{port}{reset} {blue}is{reset} {green}OPEN{reset}")
                    print(f"{yellow}__________________________________\n{reset}")
                else:
                    pass
        except KeyboardInterrupt:
            s.close()
        except Exception as e:
            print(f"{red}[!] Error:{reset} {yellow}An error has occurred while scanning port {port}.")
            print(f"{magenta}-------------------------------------------------------------------------------{reset}")
            print(f"{red}{e}{reset}")

# Creates a port_scanner object
ps = port_scan(args)

# Runs the right port_scanner function based on the command-line arguments given
if args.port:
    ps.scan_single_port()
elif args.range:
    try:
        ps.scan_port_range()
        ps.time_remaining_calculater()
    except KeyboardInterrupt:
        print("\n")
        exit()
    except Exception as e:
        print(f"{red}{e}{reset}")