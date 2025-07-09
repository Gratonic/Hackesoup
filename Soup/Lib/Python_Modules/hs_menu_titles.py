"""
# :: Author Information and Program Details :: #

File Name: hs_validator.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.10.12
Dependencie(s): colorama
Last Modified: February 8th, 2025

# :: Description :: #

This python file contains the title information used in the hs_menus.py file to build the portion of the header for the menu
portion of the UX menus.
"""

# :: Imports :: #
import colorama # Copyright (c) 2013-2023, Anthony Sottile, All Rights Reserved

# color objects, used for nicer output
reset = colorama.Fore.RESET
green = colorama.Fore.GREEN

# :: Functionality :: #

# ASCII art and text

# Main Menu Title Stuff
def hackesoup():
    ascii_menu_title_art = """
        //    / /                                                                       
       //___ / / ____     ____     //___      ____    _____     ______            ______    
      / ___   / //   ) ) //   ) ) //\\ \\     //___))  ( (  ) )  //   ) ) //   / / //   ) ) 
     //    / / //   / / //       //  \\ \\   //         \\ \\     //   / / //   / / //___/ /  
    //    / / ((___( ( ((____   //    \\ \\ ((____   //__) )   ((___/ / ((___( ( //"""
    menu_name = f"Hackesoup"
    menu_title_bar = f"__________________________________________________________________________________________/"
    return [ascii_menu_title_art, menu_title_bar, menu_name]

# Other Title Stuff

def soupemapper():
    ascii_tool_title_art = """
     _____                                                              
    /  ___|                                                             
    \\ `--.  ___  _   _ _ __   ___ _ __ ___   __ _ _ __  _ __   ___ _ __ 
     `--. \\/ _ \\| | | | '_ \\ / _ \\ '_ ` _ \\ / _` | '_ \\| '_ \\ / _ \\ '__|
    /\\__/ / (_) | |_| | |_) |  __/ | | | | | (_| | |_) | |_) |  __/ |   
    \\____/ \\___/ \\__,_| .__/ \\___|_| |_| |_|\\__,_| .__/| .__/ \\___|_|   
                      | |                        | |   | |              
                      |_|                        |_|   |_|              """
    tool_name = f"Port Scanner"
    menu_title_bar = f"_________________________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_name]

def sub_domain_finder():
    ascii_tool_title_art = """
     _____       _  __                _            
    /  ___|     (_)/ _|              | |           
    \\ `--.  __ _ _| |_ __ _ _ __   __| | ___  _ __ 
     `--. \\/ _` | |  _/ _` | '_ \\ / _` |/ _ \\| '__|
    /\\__/ / (_| | | || (_| | | | | (_| | (_) | |   
    \\____/ \\__,_|_|_| \\__,_|_| |_|\\__,_|\\___/|_|   """
    tool_title = f"Sub Domain Finder"
    menu_title_bar = f"______________________________________________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_title]

def xss_scanner():
    ascii_tool_title_art = """
    __   _______ _____                                       
    \\ \\ / /  ___/  ___|                                      
     \\ V /\\ `--.\\ `--.   ___  ___ __ _ _ __   _ __    ___ _ __ 
     /   \\ `--. \\`--. \\ / __|/ __/ _`| '_   \\| '_  \\ / _ | '__|
    / /^\\ /\\__/ /\\__/ / \\__ |  (_| (_| | | | | | | ||  __| |   
    \/   \\\\____/\\____/  |___/\\___\\__,|_|_| |_|_| |_| \\___|_|"""
    tool_title = f"XSS Scanner"
    menu_title_bar = f"_______________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_title]

def dir_trav_scanner():
    ascii_tool_title_art = """
    ______ _        _____                                  _   _____                                 
    |  _  (_)      |_   _|                                | | /  ___|                                
    | | | |_ _ __    | |_ __ __ ___   _____ _ __ ___  __ _| | \\ `--.  ___ __ _ _ __  _ __   ___ _ __ 
    | | | | | '__|   | | '__/ _` \\ \\ / / _ | '__/ __|/ _` | |  `--. \\/ __/ _` | '_ \\| '_ \\ / _ | '__|
    | |/ /| | |_     | | | | (_| |\ V |  __| |  \__ | (_| | | /\__/ | (_| (_| | | | | | | |  __| |   
    |___/ |_|_(_)    \\_|_|  \\__,_| \\_/ \\___|_|  |___/\\__,_|_| \\____/ \\___\\__,_|_| |_|_| |_|\\___|_|"""
    tool_title = f"Directory Traversal Scanner"
    menu_title_bar = f"________________________________________________________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_title]


def sqli_scanner():
    ascii_tool_title_art = """
     _____ _____ _    _____                                       
    /  ___|  _  | |  |_   _|                                      
    \\ `--.| | | | |    | |    ___  ___ __ _ _ __  _ __   ___ _ __ 
     `--. | | | | |    | |   / __|/ __/ _` | '_ \\| '_ \\ / _ | '__|
    /\\__/ \\ \\/' | |____| |_  \\__ | (_| (_| | | | | | | |  __| |   
    \\____/ \\_/\\_\\_____\\___/  |___/\\___\\__,_|_| |_|_| |_|\\___|_|"""
    tool_title = f"SQLI Scanner"
    menu_title_bar = f"____________________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_title]

def patch_pirate():
    ascii_tool_title_art = """
    ______     _       _      ______ _           _       
    | ___ \\   | |     | |     | ___ (_)         | |      
    | |_/ /_ _| |_ ___| |__   | |_/ /_ _ __ __ _| |_ ___ 
    |  __/ _` | __/ __| '_ \\  |  __/| | '__/ _` | __/ _ \\
    | | | (_| | || (__| | | | | |   | | | | (_| | ||  __/
    \\_|  \\__,_|\\__\\___|_| |_| \\_|   |_|_|  \\__,_|\\__\\___|"""
    tool_title = f"patch_pirate hackesoup edition"
    menu_title_bar = f"___________________________________________________________/"
    return [ascii_tool_title_art,  menu_title_bar, tool_title]

# Easter Egg(s)

# Credit: Kirilllive (https://github.com/Kirilllive)
def floppy_drive_heaven_easter_egg():
    return """
                                                              .                    
                        .                    .                :                    
                        ;                 .               .   !   '                
                    - --+- -                +                ,|.'                  
                        !                          -  -- ---(-O-`--- --  -         
                _--__   .  _________________________________,`|'`.                 
               /  /  \\    |  |                           |  | !    .               
              |    ,-.)   |[]|                           |[]| :                    
      /\\_     (  () =(    |  |                           |  | . . :  ___           
      \\ /      \)\  _/    |  |                           |  | .     /_  ",         
       \\\\    .-'   '--.   |  |                           |  |      (((/   \\        
        \\\\_.' ,  \\  \\  \\  |  |                           |  |       )- )  )        
         \\_.-'\\,_/ _/'\\ \\/|  |                           |  |       \\_/   /        
               \\   (   '_/|  |                           |  |       _-(   (        
               |  . '.    |  |                           |  |      / ) )  )___     
               |      \\   |  |                           |  |_\\\\__/ / (  (% #/     
               \\  _|   \\  |  |                           |  | "----')__\\,)__/      
                \\  |   |  |  \               @Kirilllive /  |      /  '(           
                 '.|   |  |   '-------------------------'   |     /     \\          
                    \\  '\_|       ,-----------------.----.  |     (   / /          
                     `-._ |       |  ,---,          |    |  |     )     (          
                        \\`|       |  |   |          |    |  |     "-___-"          
                         \\| //||| |  |   |          |    |  |     |  | |           
                          | ((|-| |  |   |          |    ||||     | /| |           
                          | \\\\||| |  |   |          |    |\\/|     | )\\ |           
                          \\       |  |___|          |____|  |     | / \\ \\          
                           ',____/-------------------_______/     |-(  \\^(         
                                                                  )^/   \\_\\        
                                                                 /_/            """