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

# Main class
class Pages():
    """Hackesoup core module for generating cli based UX menus: \n
    Args: None
    Public Functions:

        <add_element>:
            Takes type and values as args, generates a UX element and adds it to
            the page constructor process.

            args:
                <type> (String) Char or symbol used to construct element
                <values> (String, Tuple) Takes a tuple of settings for the
                        element or a string with the element text and auto 
                        sets the other settings using defaults

        <draw>:
            Draws the constructed page to the output.
            Args: None    
        """
    
    # Init main class
    def __init__(self):

        # Define internal globals
        self._compiled_page = ""
        self._element_default_accent_color = green
        self._element_default_text_color = green

        # Define element templates
        self._header = "{a}{b}\n{c}{d}\n{a}{b} {reset}"
        self._footer = "{a}{b}\n{c}{d} {reset}"
        self. _text = "{a}{b} {reset}"
        self._menu_item = "{a}{b}{c} {d} {reset}"
        

    
    # Internal function for appending new elements to the page variable to be drawn.
    def _page_add(self, element):

        self._compiled_page = self._compiled_page + f"{element}\n"


    # Function responsable for creating UX elements
    def add_element(self, type, values=None):
        """Function to generate a UX element and add it to\n
            the page constructor process.\n
            Avalible UX elements:\n
             [header] arg: [title text, border symbol (default "="), accent color (default green), text color (default gray)]\n
             [foot] arg: [length, symbol (default "="), message(default: Blank), accent color (default green), text color (default gray)]\n
             [menu_item] arg: [text, bullet symbol (or string), accent color (default green), text color (default gray)]\n
             [decoration] arg: [Unfinished]\n
             [text] arg: [text, color(default grey)]\n"""

        # Header element
        if type == "header":
            if isinstance(values, str):
                values = [values, "=",self._element_default_accent_color, self._element_default_text_color]
            self._page_add(self._header.format(
                a=values[2], 
                b=values[1] * (len(values[0]) + 4), 
                c=values[3], 
                d=values[0], 
                reset=reset))

        # Footer element
        elif type == "foot":
            if int((values[0]/2)-(len(values[2])/2)-1) > -1:
                if isinstance(values, str):
                    values = [values, "=", "", self._element_default_accent_color, self._element_default_text_color]
            # lenghth, Type, message, color, message_color
                self._page_add(self._footer.format(
                    a=values[3], 
                    b=values[1] * values[0], 
                    c=values[4], 
                    d=((" " * int((values[0]/2)-(len(values[2])/2)-1)) + values[2]), 
                    reset=reset))
            else:
                self._page_add("UX element error: message length is greater then footer length. element was not rendered.")

        # Menu item element (Bullet list)
        elif type == "menu_item":
            # text, bullet_type, text_color, bullet_color
            if isinstance(values, str):
                values = [values, "-", self._element_default_text_color, self._element_default_accent_color]
            self._page_add(self._menu_item.format(
                    a=values[3], 
                    b=values[1], 
                    c=values[2], 
                    d=values[0], 
                    reset=reset))

        #TODO: Decoration element (i.e. ACSII art banner or other such UX elements)
        elif type == "decoration":
            pass

        # Text element
        elif type == "text":
            if isinstance(values, str):
                values = [values, self._element_default_text_color]
            self._page_add(self._text.format(
                a=values[1], 
                b=values[0],  
                reset=reset))

    # Function to draw the current UX to the output console
    def draw(self, suppress_output=False):
        """Draws the current state of the UX build to the output console."""
        os.system("clear")
        if not suppress_output:
            print(self._compiled_page)
        return self._compiled_page
