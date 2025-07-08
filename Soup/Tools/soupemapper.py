# [=== Program Metadata ===] #

"""
# :: Author Information and Program Details :: #

File Name: saifandor.py
Author(s): ibrahim-sisar (https://github.com/ibrahim-sisar) and Gratonic (https://github.com/Gratonic)
Written In: Python 3.13.5
Dependencie(s): colorama, halo, json, os
Last Modified: 7/6/2025

# :: Description :: #

This is the code for the soupemapper tool.

"""

# [=== Imports ===] #

from colorama import Fore, Back # Copyright (c) 2013-2025, Anthony Sottile, All Rights Reserved
from halo import Halo
import json
import os

# [=== Tool Plan ===] #

# [=== Settings Example ===] #

"""
NOTE: Only the target and save_file information is needed, the other settings are not used by the tool

{
'target': 'https://www.google.com',
'tool': 'subdomain_finder', 
'tool_class': 'WEB', 
'API_token': None, 
'port': None, 'port_range': None, 
'scan_type': None, 
'save_file': None
}
"""

# [=== Final Output Example ===]

"""
<ascii title>
___________________/

Target: 192.168.1.1
---------------------------------
* OS: Linux 5.4.0
* Uptime: 12 days, 4 hours

[ === Discovered Nodes ===]

    Node/Device        IP Address        Hostname
------------------------------------------------------------------------------
[+] Web Server       192.168.1.10      web.example.com
[+] Database Server  192.168.1.20      db.example.com
[+] Mail Server      192.168.1.30      mail.example.com
------------------------------------------------------------------------------

[=== Open Ports with Services ===]

    Service          Port
------------------------------------------------------------------------------
[+] SSH             22
[+] HTTP            80
[+] HTTPS           443
[+] FTP             21
[+] MySQL           3306
[+] PostgreSQL      5432
------------------------------------------------------------------------------

[=== Report Summary ===]

    - Total Discovered Nodes: 3
    - Scan Duration: 5 minutes
    - Scan Date: July 8, 2025

------------------------------------------------------------------------------

[=== End of Report ===]

"""