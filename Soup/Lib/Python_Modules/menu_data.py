"""
# :: Author Information and Program Details :: #

File Name: menu_data.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.12.3
Dependencie(s): None
Last Modified: October 3, 2025

# :: Description :: #

This file contains all of the functions used to retrieve the data needed to construct each menu with menataur in hs_menus.
"""

# [=== Main Menu ===] #

def main_menu() -> dict:
    ascii_title = r"""
        //    / /                                                                       
       //___ / / ____     ____     //___      ____    _____     ______            ______    
      / ___   / //   ) ) //   ) ) //\ \     //___))  ( (  ) )  //   ) ) //   / / //   ) ) 
     //    / / //   / / //       //  \ \   //         \ \     //   / / //   / / //___/ /  
    //    / / ((___( ( ((____   //    \ \ ((____   //__) )   ((___/ / ((___( ( //        """
    title_colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

    title_bar = "__________________________________________________________________________________________/"

    small_title = "Hackesoup"
    tool_version = "1.0"

    descriptions = {
        "1": "tools for open-source intelligence and general reconnaissance", 
        "2": "tools for scanning websites and web applications", 
        "3": "tools for local area network mapping and hacking"
    }

    options = {
        "1": "OSINT and Recon Tools", 
        "2": "Web Tools", 
        "3": "LAN Tools"
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

# [=== Tool Class Menus ===] #

def osint_tool_menu() -> dict:
    ascii_title = r"""
        //    / /                                                                       
       //___ / / ____     ____     //___      ____    _____     ______            ______    
      / ___   / //   ) ) //   ) ) //\ \     //___))  ( (  ) )  //   ) ) //   / / //   ) ) 
     //    / / //   / / //       //  \ \   //         \ \     //   / / //   / / //___/ /  
    //    / / ((___( ( ((____   //    \ \ ((____   //__) )   ((___/ / ((___( ( //        """
    title_colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

    title_bar = "__________________________________________________________________________________________/"

    small_title = "Hackesoup"
    tool_version = "1.0"

    descriptions = {
        "1": "scans github for PII and other information on a targeted github user"
    }

    options = {
        "1": "PatchPirate (Juha sa štruklima Soup - Croation)"
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

def web_tool_menu() -> dict:
    ascii_title = r"""
        //    / /                                                                       
       //___ / / ____     ____     //___      ____    _____     ______            ______    
      / ___   / //   ) ) //   ) ) //\ \     //___))  ( (  ) )  //   ) ) //   / / //   ) ) 
     //    / / //   / / //       //  \ \   //         \ \     //   / / //   / / //___/ /  
    //    / / ((___( ( ((____   //    \ \ ((____   //__) )   ((___/ / ((___( ( //        """
    title_colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

    title_bar = "__________________________________________________________________________________________/"

    small_title = "Hackesoup"
    tool_version = "1.0"

    descriptions = {
        "1": "finds the subdomains of a website", 
        "2": "scans a website for SQLI vulnerabilities",
        "3": "scans a website for XSS vulnerabilities", 
        "4": "scans a website for directory traversal vulnerabilities",
        "5": "determines the web application firewall used on a website"
    }

    options = {
        "1": "Serikandor (Lentil - Israeli)",
        "2": "Dabijar (Zuppa di Cavolo Nero - Italiano)", 
        "3": "Mudelatie (Hutspot - Dutch)", 
        "4": "Baumspinne (Kartoffelsuppe Soup - German)",
        "5": "Wafter (Sopa de Mariscos - Costa Rican)",
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

def lan_tool_menu() -> dict:
    ascii_title = r"""
        //    / /                                                                       
       //___ / / ____     ____     //___      ____    _____     ______            ______    
      / ___   / //   ) ) //   ) ) //\ \     //___))  ( (  ) )  //   ) ) //   / / //   ) ) 
     //    / / //   / / //       //  \ \   //         \ \     //   / / //   / / //___/ /  
    //    / / ((___( ( ((____   //    \ \ ((____   //__) )   ((___/ / ((___( ( //        """
    title_colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

    title_bar = "__________________________________________________________________________________________/"

    small_title = "Hackesoup"
    tool_version = "1.0"

    descriptions = {
        "1": "scans ports to see if they are open, closed, or filtered"
    }

    options = {
        "1": "Soupemapper (Clam Chowder Soup - American)"
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

# [=== PatchPirate Menu(s) ===] #

def patchpirate_menu_1() -> dict:
    ascii_title = r"""
    ______     _       _    ______ _           _       
    | ___ \   | |     | |   | ___ (_)         | |      
    | |_/ /_ _| |_ ___| |__ | |_/ /_ _ __ __ _| |_ ___ 
    |  __/ _` | __/ __| '_ \|  __/| | '__/ _` | __/ _ \
    | | | (_| | || (__| | | | |   | | | | (_| | ||  __/
    \_|  \__,_|\__\___|_| |_\_|   |_|_|  \__,_|\__\___|"""
    title_colors = ["red", "white", "blue", "yellow"]

    title_bar = "___________________________________________________________/"

    small_title = "patchpirate hackesoup edition"
    tool_version = "1.0"

    descriptions = {
        "1": "scan with a GitHub API token", 
        "2": "scan without a GitHub API token"
    }

    options = {
        "1": "Use an API Token", 
        "2": "Don't use an API Token"
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

# [=== Serikandor Menu(s) ===] #

def serikandor_menu_1() -> dict:
    ascii_title = r"""
     _____           _ _                   _            
    /  ___|         (_) |                 | |           
    \ `--.  ___ _ __ _| | ____ _ _ __   __| | ___  _ __ 
     `--. \/ _ \ '__| | |/ / _` | '_ \ / _` |/ _ \| '__|
    /\__/ /  __/ |  | |   < (_| | | | | (_| | (_) | |   
    \____/ \___|_|  |_|_|\_\__,_|_| |_|\__,_|\___/|_|   """
    title_colors = ["blue", "white"]

    title_bar = "______________________________________________________________________________________________/"
    
    small_title = "serikandor"
    tool_version = "1.0"

    descriptions = {
        "1": None
    }

    options = {
        "1": None
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

# [=== Dabijar Menu(s) ===] #

def dabijar_menu_1() -> dict:
    ascii_title = r"""
    ______      _     _ _            
    |  _  \    | |   (_|_)           
    | | | |__ _| |__  _ _  __ _ _ __ 
    | | | / _` | '_ \| | |/ _` | '__|
    | |/ / (_| | |_) | | | (_| | |   
    |___/ \__,_|_.__/|_| |\__,_|_|   
                      _/ |           
                     |__/            """
    title_colors = ["green", "white", "red"]

    title_bar = "____________________________________________________________________/"

    small_title = "dabijar"
    tool_version = "1.0"  

    descriptions = {
        "1": None
    }

    options = {
        "1": None
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

# [=== Mudelatie Menu(s) ===] #

def mudelatie_menu_1() -> dict:
    ascii_title = r"""
    ___  ___          _      _       _   _      
    |  \/  |         | |    | |     | | (_)     
    | .  . |_   _  __| | ___| | __ _| |_ _  ___ 
    | |\/| | | | |/ _` |/ _ \ |/ _` | __| |/ _ \
    | |  | | |_| | (_| |  __/ | (_| | |_| |  __/
    \_|  |_/\__,_|\__,_|\___|_|\__,_|\__|_|\___|"""
    title_colors = ["red", "white", "blue", "green"]

    title_bar = "_______________________________________________________________/"
    
    small_title = "mudelatie"
    tool_version = "1.0"

    descriptions = {
        "1": None
    }

    options = {
        "1": None
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

# [=== Baumspinne Menu(s) ===] #

def baumspinne_menu_1() -> dict:
    ascii_title = r"""
    ______                                 _                  
    | ___ \                               (_)                 
    | |_/ / __ _ _   _ _ __ ___  ___ _ __  _ _ __  _ __   ___ 
    | ___ \/ _` | | | | '_ ` _ \/ __| '_ \| | '_ \| '_ \ / _ \
    | |_/ / (_| | |_| | | | | | \__ \ |_) | | | | | | | |  __/
    \____/ \__,_|\__,_|_| |_| |_|___/ .__/|_|_| |_|_| |_|\___|
                                    | |                       
                                    |_|                       """
    title_colors = ["red", "grey", "yellow"]

    title_bar = "________________________________________________________________________________________________________/"

    small_title = "baumspinne"
    tool_version = "1.0"

    descriptions = {
        "1": None
    }

    options = {
        "1": None
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

# [=== Wafter Menu(s) ===] #

def wafter_menu_1():
    ascii_title = r"""
     _    _        __ _            
    | |  | |      / _| |           
    | |  | | __ _| |_| |_ ___ _ __ 
    | |/\| |/ _` |  _| __/ _ \ '__|
    \  /\  / (_| | | | ||  __/ |   
     \/  \/ \__,_|_|  \__\___|_|   """
    title_colors = ["blue", "red", "white", "yellow", "light_blue", "light_green"]

    title_bar = "___________________________________/"

    small_title = "wafter"
    tool_version = "1.0"

    descriptions = {
        "1": None
    }

    options = {
        "1": None
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

# [=== Soupemapper Menu(s) ===] #

def soupemapper_menu_1() -> dict:
    ascii_title = r"""
     _____                                                              
    /  ___|                                                             
    \ `--.  ___  _   _ _ __   ___ _ __ ___   __ _ _ __  _ __   ___ _ __ 
     `--. \/ _ \| | | | '_ \ / _ \ '_ ` _ \ / _` | '_ \| '_ \ / _ \ '__|
    /\__/ / (_) | |_| | |_) |  __/ | | | | | (_| | |_) | |_) |  __/ |   
    \____/ \___/ \__,_| .__/ \___|_| |_| |_|\__,_| .__/| .__/ \___|_|   
                      | |                        | |   | |              
                      |_|                        |_|   |_|              """
    title_colors = ["red", "white", "blue"]

    title_bar = "_________________________________________________________________________/"

    small_title = "soupemapper"
    tool_version = "1.0"

    descriptions = {
        "1": "scans a single port", 
        "2": "scans a range of ports"
    }

    options = {
         "1": "Single Port", 
         "2": "Port Range"
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

def soupemapper_menu_2() -> dict:
    ascii_title = r"""
     _____                                                              
    /  ___|                                                             
    \ `--.  ___  _   _ _ __   ___ _ __ ___   __ _ _ __  _ __   ___ _ __ 
     `--. \/ _ \| | | | '_ \ / _ \ '_ ` _ \ / _` | '_ \| '_ \ / _ \ '__|
    /\__/ / (_) | |_| | |_) |  __/ | | | | | (_| | |_) | |_) |  __/ |   
    \____/ \___/ \__,_| .__/ \___|_| |_| |_|\__,_| .__/| .__/ \___|_|   
                      | |                        | |   | |              
                      |_|                        |_|   |_|              """
    title_colors = ["red", "white", "blue"]

    title_bar = "_________________________________________________________________________/"

    small_title = "soupemapper"
    tool_version = "1.0"

    descriptions = {
        "1": "Establishes a full TCP connection to identify open ports.",
        "2": "Sends SYN packets to find open ports without completing the handshake.",
        "3": "Sends UDP packets to check for open ports.",
        "4": "Sends packets with FIN, URG, and PSH flags to elicit responses.",
        "5": "Identifies open ports and determines the service running on each port.",
    }

    options = {
        "1": "TCP Connect Scan",
        "2": "SYN Scan",
        "3": "UDP Scan",
        "4": "Xmas Scan",
        "5": "Service Scan",
    }

    return {
        "ascii_title": ascii_title,
        "title_colors": title_colors,
        "title_bar": title_bar,
        "small_title": small_title,
        "tool_version": tool_version,
        "options": options,
        "descriptions": descriptions
    }

# [=== Easter Egg ASCII Art ===] #

def floppy_disk_heaven_easter_egg():
    return r"""
                                                          .                    
                    .                    .                :                    
                    ;                 .               .   !   '                
                - --+- -                +                ,|.'                  
                    !                          -  -- ---(-O-`--- --  -         
            _--__   .  _________________________________,`|'`.                 
           /  /  \    |  |                           |, | !    .               
          |    ,-.)   |[]|                           |[]| :                    
  /\_     (  () =(    |  |                           |  | . . :  ___           
  \ /      \)\  _/    |  |                           |  | .     /_  ",         
   \\    .-'   '--.   |  |                           |  |      (((/   \        
    \\_.' ,  \  \  \  |  |                           |  |       )- )  )        
     \_.-'\,_/ _/'\ \/|  |                           |  | ,     \_/   /        
           \   (   '_/|  |                           |  | |     _-(   (        
           |  . '.    |  |                           |  | |    / ) )  )___     
           |      \   |  |                           |  |_\\__/ / (  (% #/     
           \  _|   \  |  |                           |  | "----')__\,)__/      
            \  |   |  |  \               @Kirilllive /  |      /  '(           
             '.|   |  |   '-------------------------'   |     /     \          
                \  '\_|       ,-----------------.----.  |     (   / /          
                 `-._ |       |  ,---,          |    |  |     )     (          
                    \`|       |  |   |          |    |  |     "-___-"          
                     \| //||| |  |   |          |    |  |     |  | |           
                      | ((|-| |  |   |          |    ||||     | /| |           
                      | \\||| |  |   |          |    |\/|     | )\ |           
                      \       |  |___|          |____|  |     | / \ \          
                       ',____/-------------------_______/     |-(  \^(         
                                                              )^/   \_\        
                                                             /_/          """