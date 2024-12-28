# Imports

# PIP Modules
import sys
import os
# Used to import the custom modules
import importlib

# Custom Modules
# NOTE: The custom modules must be imported this way because of the way the Python import system works

# Used to locate the custom modules
current_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(current_dir, '..', 'Lib', 'Modules')
sys.path.append(modules_dir)
# Imports the custom modules
hs_menus = importlib.import_module('hs_menus')
hs_prompts = importlib.import_module('hs_prompts')
