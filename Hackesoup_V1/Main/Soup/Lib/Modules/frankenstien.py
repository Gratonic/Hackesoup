# External imports
import os
import colorama

# Colour objects, used for nicer output
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

# TODO: Fix errors

# Main class
class Monster():
    """Hackesoup core [Soup] module for generating cli based UX menus: \n
    Args: None
    Public Functions:

        <add_limb>:
            Takes type and values as args, generates a UX element and adds it to
            the page (Monster) constructor process.

            args:
                <type> (String) Char or symbol used to construct element
                <values> (String, Tuple) Takes a tuple of settings for the
                        element or a string with the element text and auto 
                        sets the other settings using defaults

        <come_to_life>:
            Draws the constructed page to the output.
            Args: None    
        """
    
    # Init main class
    def __init__(self):
        # Define internal globals
        # Compiled page = _live_monster
        self._live_monster = ""
        self._limb_default_accent_color = green
        self._limb_default_text_color = green
        # Define element templates
        # Type Header
        self._head = "{a}{b}\n{c}{d}\n{a}{b} {reset}"
        # Type Footer
        self._feet = "{a}{b}\n{c}{d} {reset}"
        # Type Text
        self. _guts = "{a}{b} {reset}"
        # Type Body
        self._body = "{a}{b}{c} {d} {reset}"
    

    # Internal function for appending new elements to the page variable to be drawn.
    # _page_add
    def _attach(self, element):
        self._live_monster = self._live_monster + f"{element}\n"
    
    # Function responsable for creating UX elements
    # Add element
    def add_limb(self, type, values=None):
        """Function to generate a UX element and add it to\n
            the page constructor process.\n
            Avalible UX elements:\n
            [header] arg: [title text, border symbol (default "="), accent color (default green), text color (default gray)]\n
            [foot] arg: [length, symbol (default "="), message(default: Blank), accent color (default green), text color (default gray)]\n
            [menu_item] arg: [text, bullet symbol (or string), accent color (default green), text color (default gray)]\n
            [decoration] arg: [Unfinished]\n
            [text] arg: [text, color(default grey)]\n"""
        
        # Header element
        if type == "head":
            if isinstance(values, str):
                values = [values, "=",self._limb_default_accent_color, self._limb_default_text_color]
            if len(values) < 4:
                raise ValueError("Header requires at least 4 values: [title text, border symbol, accent color, text color]")
            self._attach(self._head.format(
                a=values[2], 
                b=values[1] * (len(values[0]) + 4), 
                c=values[3], 
                d=values[0], 
                reset=reset))

        # Footer element
        elif type == "feet":
            if isinstance(values, str):
                values = [values, "=", "", self._limb_default_accent_color, self._limb_default_text_color]
            if len(values) < 5:
                raise ValueError("Footer requires at least 5 values: [length, symbol, message, accent color, text color]")
            # lenghth, Type, message, color, message_color
            if int((values[0]//2)-(len(values[2])/2)-1) > -1:
                self._attach(self._feet.format(
                    a=values[3], 
                    b=values[1] * values[0], 
                    c=values[4], 
                    d=((" " * int((values[0]/2)-(len(values[2])/2)-1)) + values[2]), 
                    reset=reset))
            else:
                self._attach("UX element error: message length is greater then footer length. element was not rendered.")

        # Menu item element (Bullet list)
        elif type == "body":
            # text, bullet_type, text_color, bullet_color
            if isinstance(values, str):
                values = [values, "-", self._limb_default_text_color, self._limb_default_accent_color]
            if len(values) < 4:
                raise ValueError("Body requires at least 4 values: [text, bullet symbol, accent color, text color]")
            self._attach(self._body.format(
                    a=values[3], 
                    b=values[1], 
                    c=values[2], 
                    d=values[0], 
                    reset=reset))

        # TODO: Decoration element (i.e. ACSII art banner or other such UX elements)
        # No need to have python evaulate these lines at the moment
        # elif type == "decoration":
        #     pass

        # Text element
        elif type == "guts":
            if isinstance(values, str):
                values = [values, self._limb_default_text_color]
            if len(values) < 2:
                raise ValueError("Text requires at least 2 values: [text, color]")
            self._attach(self._guts.format(
                a=values[1], 
                b=values[0], 
                reset=reset))

    # Function to draw the current UX to the output console
    def shock(self, suppress_output=False):
        """Draws the current state of the UX build to the output console."""
        # "cls" if os == windows and "clear" if os == "mac" or "linux"
        os.system("cls" if os.name == "nt" else "clear")
        if not suppress_output:
            print(self._live_monster)
        return self._live_monster

"""
Example Usage:

# Prepares the lab for assembly (creates the monster object)
monster = Monster()

# Adding head (header element)
monster.add_limb("head", "Welcome to the Monster CLI")
# Adding to the body (body element)
monster.add_limb("body", "0) Exit")
# Adding to the body (body element)
monster.add_limb("body", "1): XSS Scanner")
# Adding to the body (body element)
monster.add_limb("body", "2): Previous Menu")
# Adding feet (footer element)
monster.add_limb("feet", [30, "=", "Thank you for playing!", green, gray])

# Shock the monster, brining it to life (Draw the UX to the output console)
monster.shock()
"""