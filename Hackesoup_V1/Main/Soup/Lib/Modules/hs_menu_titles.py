# Imports
import colorama

# color objects, used for nicer output
reset = colorama.Fore.RESET
green = colorama.Fore.GREEN

# ASCII art and text

# Main Menu Title Stuff
def hackesoup():
    return """
        //    / /                                                                       
       //___ / / ____     ____     //___      ____    _____     ______            ______    
      / ___   / //   ) ) //   ) ) //\ \     //___))  ( (  ) )  //   ) ) //   / / //   ) ) 
     //    / / //   / / //       //  \ \   //         \ \     //   / / //   / / //___/ /  
    //    / / ((___( ( ((____   //    \ \ ((____   //__) )   ((___/ / ((___( ( //"""

def hackesoup_snowboard():
    return "__________________________________________________________________________________/"

# Other Title Stuff

def port_scanner():
    return """
    ______          _     _____                                 
    | ___ \        | |   /  ___|                                
    | |_/ /__  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
    |  __/ _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ | '__|
    | | | (_) | |  | |_  /\__/ | (_| (_| | | | | | | |  __| |   
    \_|  \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|"""

def sub_domain_finder():
    return """
     _____       _      ______                      _        ______ _           _           
    /  ___|     | |     |  _  \                    (_)       |  ___(_)         | |          
    \ `--. _   _| |__   | | | |___  _ __ ___   __ _ _ _ __   | |_   _ _ __   __| | ___ _ __ 
     `--. | | | | '_ \  | | | / _ \| '_ ` _ \ / _` | | '_ \  |  _| | | '_ \ / _` |/ _ | '__|
    /\__/ | |_| | |_) | | |/ | (_) | | | | | | (_| | | | | | | |   | | | | | (_| |  __| |   
    \____/ \__,_|_.__/  |___/ \___/|_| |_| |_|\__,_|_|_| |_| \_|   |_|_| |_|\__,_|\___|_|"""

def xss_scanner():
    return """
    __   _______ _____                                       
    \ \ / /  ___/  ___|                                      
     \ V /\ `--.\ `--.   ___  ___ __ _ _ __  _ __   ___ _ __ 
     /   \ `--. \`--. \ / __|/ __/ _` | '_ \| '_ \ / _ | '__|
    / /^\ /\__/ /\__/ / \__ | (_| (_| | | | | | | |  __| |   
    \/   \\____/\____/  |___/\___\__,_|_| |_|_| |_|\___|_|"""

def dir_trav_scanner():
    return """
    ______ _        _____                                  _   _____                                 
    |  _  (_)      |_   _|                                | | /  ___|                                
    | | | |_ _ __    | |_ __ __ ___   _____ _ __ ___  __ _| | \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
    | | | | | '__|   | | '__/ _` \ \ / / _ | '__/ __|/ _` | |  `--. \/ __/ _` | '_ \| '_ \ / _ | '__|
    | |/ /| | |_     | | | | (_| |\ V |  __| |  \__ | (_| | | /\__/ | (_| (_| | | | | | | |  __| |   
    |___/ |_|_(_)    \_|_|  \__,_| \_/ \___|_|  |___/\__,_|_| \____/ \___\__,_|_| |_|_| |_|\___|_|"""

def sqli_scanner():
    return """
     _____ _____ _    _____                                       
    /  ___|  _  | |  |_   _|                                      
    \ `--.| | | | |    | |    ___  ___ __ _ _ __  _ __   ___ _ __ 
     `--. | | | | |    | |   / __|/ __/ _` | '_ \| '_ \ / _ | '__|
    /\__/ \ \/' | |____| |_  \__ | (_| (_| | | | | | | |  __| |   
    \____/ \_/\_\_____\___/  |___/\___\__,_|_| |_|_| |_|\___|_|"""

# Fragmented because of the y
def destroyter_fragements():
    destroyer_frags = [
                        "______         _                             ", # line 0
                        "|  _  \       | |                            ", # line 1
                        "| | | |___ ___| |_ _ __ ___  _   _  ___ _ __ ", # line 2
                        "| | | / _ / __| __| '__/ _ \| | | |/ _ | '__|", # line 3
                        "| |/ |  __\__ | |_| | | (_) | |_| |  __| |   ", # line 4
                        "|___/ \___|___/\__|_|  \___/ \__, |\___|_|   ", # line 5
                        "                              __/ |          ", # line 6 - Will have a line that is broken by the 'y'
                        "                             |___/           ", # line 7
                    ]
    return destroyer_frags

# Provides an alternative way to grab a menu
def grab_menu(tool_num) -> list:
    try:
        tool_num = int(tool_num)
        if tool_num <= 0:
            raise ValueError("Invalid tool number")
        elif tool_num > 6:
            raise ValueError("Invalid tool number")
        else:
            pass
    except:
        raise ValueError("Invalid tool number")
    # Determines what menu to return based on the tool number
    if tool_num == 1:
        menu_title = port_scanner()
        menu_title_bar = f"__________________________________________________________________/"
        return [menu_title, menu_title_bar]
    elif tool_num == 2:
        menu = sub_domain_finder()
        return menu
    elif tool_num == 3:
        menu = xss_scanner()
        return menu
    elif tool_num == 4:
        menu = dir_trav_scanner()
        return menu
    elif tool_num == 5:
        menu = sqli_scanner()
        return menu
    elif tool_num == 6:
        message = "Destroyer cannot be displayed because it comes in fragements, remember?"
        return message

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
               /  /  \    |  |                           |  | !    .               
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
                                                                 /_/            """