# Inside hs_mi.py

import sys
import os
import importlib

module_path = os.path.join(os.path.dirname(__file__), '..', 'Soup', 'Lib', 'Python_Modules')

sys.path.append(module_path)

hs_UX_menus = importlib.import_module('hs_UX_menus')

settings = hs_UX_menus.menu_interface()
print(settings)
