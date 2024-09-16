import tomllib, shutil, os, subprocess, platform
#import os, subprocess
import multiprocessing as mp
from globals import  PY_WIN_LOGO,  TOTAL_CPUS, SYSTEM_ARCH #, DEFAULT_TINY_PATH_WIN11, DEFAULT_TINY_PATH_WIM_MOUNT
from globals import __RAW_BANNER__, DEFAULT_TINY_PATH  #srcPath, TOTAL_CPUS, WImfillPath, ESDfillPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath, defaultTinyPathWin11, appxPackagesToRemove
from globals import BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN
from globals import BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE, RESET #, DEFAULT_TINY_PATH_WIN11_WIM, DEFAULT_TINY_PATH_WIN11_ESD
import win32com.client

def colored_print(color: str, message: str) -> None:
    print(f"{color}{message}{RESET}")


def getDocsDrive():
    return DEFAULT_TINY_PATH[:2] if DEFAULT_TINY_PATH else False

#        print("Time to create some folders.")

def calcDriveSpace(drive: str) -> list:
    total, used, free = shutil.disk_usage(drive)
    # Convert free space to gigabytes
    free_gb: int = round(free / (1024 ** 3), 2)

    # Convert free space to terabytes if needed
    free_tb: int = round(free / (1024 ** 4), 2)

    # Check if free space is greater than or equal to 1 TB
    # TODO: re-test the TBs free thing - completed
    if free_gb >= 1024:
        # Calculate TB and remaining GB
        terabytes: int = int(free_tb)
        gigabytes: int = round((free_tb - terabytes) * 1024, 2)
        return terabytes, gigabytes
#        print(f"{terabytes} TB {gigabytes} GBs free")
    else:
        # Display in GB if less than 1 TB
        gb_space: list = [free_gb]
        #gb_space:
        #return free_gb # this actually returns value I want (tested on think pad with 744.57 GBs free)
        return gb_space
#        print(f"{free_gb} GBs free")

# the need for this if exist function was eliminated by the variable definition in globals.py
#def confirmDocumentsPaths() -> str:
#    if os.path.exists(DEFAULT_TINY_PATH):
#        return True
#    else:
#        return False
#        #if os.path.exists(DEFAULT_TINY_PATH_WIN11_WIM) or os.path.exists(DEFAULT_TINY_PATH_WIN11_ESD):





######### left over notes from confirmDcoumentsPath() function
    # upon further reflection I should just use this special folders approach to finding the 
    # documents folder and create tiny11 folder from there. Instead of user the 
    # %profile% environment variable and comparing to what it really is. 
    # that seems like an unecessary step

# these two lines and definition of defaulttinypath moved to globals
#    shell = win32com.client.Dispatch("WScript.Shell")
#    documents_path = shell.SpecialFolders("MyDocuments") + """\\tiny11"""

#    print(f"documents path is {documents_path}, while defaultTinyPath is {defaultTinyPath}")

# these lines no longer needed
#    if defaultTinyPath.lstrip().rstrip().lower() == documents_path.lstrip().rstrip().lower():
#        print(f"first two characters are {documents_path[:2]}")
#        return defaultTinyPath[:2]
#    else:
#        print(f"documents path is {documents_path}, while defaultTinyPath is {defaultTinyPath}")
#        return documents_path[:2]



#    if defaultTinyPath == documents_path:
#        #return documents_path
#    #else:
#        rootDrive = documents_path[1]
#        #return documents_path
#        return documents_path
    
    #return documents_path

# def confirmDocPath() -> bool:
#     if defaultTinyPath == confirmDocumentsPath():
#         return True
#     else:
#         return False
#     
# def defineDocPath() -> str:
#     if confirmDocPath:
#         return defaultTinyPath
#     else:
#         return confirmDocumentsPath