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
    ascii_tool_title_art = r"""
     _____                                                              
    /  ___|                                                             
    \ `--.  ___  _   _ _ __   ___ _ __ ___   __ _ _ __  _ __   ___ _ __ 
     `--. \/ _ \| | | | '_ \ / _ \ '_ ` _ \ / _` | '_ \| '_ \ / _ \ '__|
    /\__/ / (_) | |_| | |_) |  __/ | | | | | (_| | |_) | |_) |  __/ |   
    \____/ \___/ \__,_| .__/ \___|_| |_| |_|\__,_| .__/| .__/ \___|_|   
                      | |                        | |   | |              
                      |_|                        |_|   |_|              """
    tool_name = f"soupemapper"
    menu_title_bar = f"_________________________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_name]

def serikandor():
    ascii_tool_title_art = r"""
    
    
     _____           _ _                   _            
    /  ___|         (_) |                 | |           
    \ `--.  ___ _ __ _| | ____ _ _ __   __| | ___  _ __ 
     `--. \/ _ \ '__| | |/ / _` | '_ \ / _` |/ _ \| '__|
    /\__/ /  __/ |  | |   < (_| | | | | (_| | (_) | |   
    \____/ \___|_|  |_|_|\_\__,_|_| |_|\__,_|\___/|_|   """
    tool_title = f"serikandor"
    menu_title_bar = f"______________________________________________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_title]

def mudelatie():
    ascii_tool_title_art = r"""
    ___  ___          _      _       _   _      
    |  \/  |         | |    | |     | | (_)     
    | .  . |_   _  __| | ___| | __ _| |_ _  ___ 
    | |\/| | | | |/ _` |/ _ \ |/ _` | __| |/ _ \
    | |  | | |_| | (_| |  __/ | (_| | |_| |  __/
    \_|  |_/\__,_|\__,_|\___|_|\__,_|\__|_|\___|"""
    tool_title = f"mudelatie"
    menu_title_bar = f"_______________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_title]

def baumspinne():
    ascii_tool_title_art = r"""
    ______                                 _                  
    | ___ \                               (_)                 
    | |_/ / __ _ _   _ _ __ ___  ___ _ __  _ _ __  _ __   ___ 
    | ___ \/ _` | | | | '_ ` _ \/ __| '_ \| | '_ \| '_ \ / _ \
    | |_/ / (_| | |_| | | | | | \__ \ |_) | | | | | | | |  __/
    \____/ \__,_|\__,_|_| |_| |_|___/ .__/|_|_| |_|_| |_|\___|
                                    | |                       
                                    |_|                       """
    tool_title = f"baumspinne"
    menu_title_bar = f"________________________________________________________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_title]

def dabijar():
    ascii_tool_title_art = r"""
    ______      _     _ _            
    |  _  \    | |   (_|_)           
    | | | |__ _| |__  _ _  __ _ _ __ 
    | | | / _` | '_ \| | |/ _` | '__|
    | |/ / (_| | |_) | | | (_| | |   
    |___/ \__,_|_.__/|_| |\__,_|_|   
                      _/ |           
                     |__/            """
    tool_title = f"dabijar"
    menu_title_bar = f"____________________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_title]

def patchpirate():
    ascii_tool_title_art = r"""
    ______     _       _    ______ _           _       
    | ___ \   | |     | |   | ___ (_)         | |      
    | |_/ /_ _| |_ ___| |__ | |_/ /_ _ __ __ _| |_ ___ 
    |  __/ _` | __/ __| '_ \|  __/| | '__/ _` | __/ _ \
    | | | (_| | || (__| | | | |   | | | | (_| | ||  __/
    \_|  \__,_|\__\___|_| |_\_|   |_|_|  \__,_|\__\___|"""
    tool_title = f"patchpirate hackesoup edition"
    menu_title_bar = f"___________________________________________________________/"
    return [ascii_tool_title_art, menu_title_bar, tool_title]

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