### Tools ###

1) Port Scanner - Version 1
2) Sub Domain Finder - Version 1
3) XSS Vulnerability Scanner - Version 1
4) Directory Traversal Vulnerability Scanner - Version 1
5) SQLI vulnerability Scanner - Version 1
6) File Destoryer - Version 1

### Tool Required Arguments ###

## Port Scanner:
    * Target
    * Port or Port Range
    * Types of Scan
## Sub Domain Finder:
    * Target
    * Type of Search
## XSS Vulnerability Scanner:
    * Target
## Directory Traversal Vulnerability Scanner:
    * Target
## SQLI Vulnerability Scanner:
    * Target
## File Destroyer:
    * File Path/File

### Tool Menu Options:

## Port Scanner
    Menu 1 - Setup 1:
        * Exit
        * Single Port
        * Port Range
        * Re-open Toolbox
    Menu 2 - Setup 2:
        * Exit
        * Basic Scan
        * Stealth Scan
        * Advanced Settings
        * Previous Menu
    Menu 3 - Advanced Settings:
        * Exit
        * Adjust Thread Count
        * Adjust Timeout
        * Adjust Thread Count and Timeout
        * Adjust Thead Count and Do A Stealth Scan
        * Adjust Timeout and Do A Stealth Scan
        * Adjust Thread Count, Adjust Timeout, and Do A Stealth Scan
        * Previous Menu
## Sub Domain Finder
    Menu 1 - Setup 1:
        * Exit
        * Basic Search
        * Stealth Search
        * Advanced Search
        * Re-open Toolbox
    Menu 2 - Advanced Settings:
        * Exit
        * Adjust Thread Amount
        * Adjust Timeout
        * Adjust Thread Amount and Timeout
        * Use Stealth Features and Adjust Thread Amount
        * Use Steatlh Features and Adjust Timeout
        * Use Stealth Features, Adjust Thread Amount, and Adjust Timeout
        * Use Custom Payload File
        * Use Custom Payload File and Stealth Features
        * Use Custom Payload File and Adjust Thread Amount
        * Use Custom Payload File and Adjust Timeout
        * Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features
        * Previous Menu
## XSS Vulnerability Scanner
    Menu 1 - Setup 1:
        * Exit
        * Basic Search
        * Stealth Search
        * Advanced Search
        * Re-open Toolbox
    Menu 2 - Advanced Settings:
        * Exit
        * Adjust Thread Amount
        * Adjust Timeout
        * Adjust Thread Amount and Timeout
        * Use Stealth Features and Adjust Thread Amount
        * Use Steatlh Features and Adjust Timeout
        * Use Stealth Features, Adjust Thread Amount, and Adjust Timeout
        * Use Custom Payload File
        * Use Custom Payload File and Stealth Features
        * Use Custom Payload File and Adjust Thread Amount
        * Use Custom Payload File and Adjust Timeout
        * Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features
        * Previous Menu
## Directory Traversal Vulnerability Scanner
    Menu 1 - Setup 1:
        * Exit
        * Basic Search
        * Stealth Search
        * Advanced Search
        * Re-open Toolbox
    Menu 2 - Advanced Settings:
        * Exit
        * Adjust Thread Amount
        * Adjust Timeout
        * Adjust Thread Amount and Timeout
        * Use Stealth Features and Adjust Thread Amount
        * Use Steatlh Features and Adjust Timeout
        * Use Stealth Features, Adjust Thread Amount, and Adjust Timeout
        * Use Custom Payload File
        * Use Custom Payload File and Stealth Features
        * Use Custom Payload File and Adjust Thread Amount
        * Use Custom Payload File and Adjust Timeout
        * Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features
        * Previous Menu
## SQLI Vulnerability Scanner
    Menu 1 - Setup 1:
        * Exit
        * Basic Search
        * Stealth Search
        * Advanced Search
        * Re-open Toolbox
    Menu 2 - Advanced Settings:
        * Exit
        * Adjust Thread Amount
        * Adjust Timeout
        * Adjust Thread Amount and Timeout
        * Use Stealth Features and Adjust Thread Amount
        * Use Steatlh Features and Adjust Timeout
        * Use Stealth Features, Adjust Thread Amount, and Adjust Timeout
        * Use Custom Payload File
        * Use Custom Payload File and Stealth Features
        * Use Custom Payload File and Adjust Thread Amount
        * Use Custom Payload File and Adjust Timeout
        * Use Custom Payload File, Adjust Thread Amount, and Adjust Timeout, and Use Stealth Features
        * Previous Menu
## File Destroyer
    Menu 1 - Setup 1:
        * Exit
        * Basic Destruction
        * Advanced Destruction
        * Re-open Toolbox
    Menu 2 - Advanced Settings:
        * Exit
        * Permanently Encrypt File with a Modern AES Cipher
        * Overwrite The File with Random Data X Amount of Times
        * Permanently Encrypt File with a Modern AES Cipher and Overwrite The File with Random Data X Amount Of Times
        * Delete The File
        * Permanently Encrypt File with a Modern AES Cipher, Overwrite The File X Amount Of Times, and Delete The File
        * Previous Menu

### Prompts ###
1) Tool Choice Prompt
2) Target
3) Port
4) Port and Port Range
5) Settings Prompt
6) Custom Payload File Prompt
7) Timeout Amount Prompt
8) Thread Amount Prompt
9) Timeout + Thread Amount Prompt 
10) Custom Payload File Prompt + Timeout and Thread Amount Prompt

### Planned Interfaces ###

1) Menu Interface - Version 1
2) Menu and Command-Line Interface - Version 2
3) Menu, Command-Line, and Graphical User Interface - Version 3
4) Console Menu [metasploit-like], Command-Line, and Graphical User Interface - Version 4
5) Improved Console, Command-Line, and Graphical User Interface - Version 5

### Update Plans ###

## Version 2:
    * Add a Command-Line Interface
    * Improve the menu interface
    * Add an OSINT Tool
    * Add a Backdoor Tool/Program
    * Add support for Windows and MacOS
## Version 3:
    * Add a Graphical User Interface
    * Improve other tnterfaces
    * Improve overall speed of the program
## Version 4:
    * Replace the Simple Menu Interface with a Console Menu Interface
    * Improve other interfaces
    * Add more features to some of the tools, if possible
## Version 5:
    * Make some improvements to the speed and design, if possible
    * Possibly add a new tool
    * Improve Stealth Features of the tools with a stealth setting

### Ideas ###

Payload Based Scanners:
    * Add a deep scan features that uses a payload file with all known payloads for that type of hack - search the web to see if such a payload file exists
    * Have the basic scan use only the payloads found on gitub for that type of hack
    * For the CLI in version 2, -t = single target and -T = multiple targets