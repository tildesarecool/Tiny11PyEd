import tomllib, shutil, os, subprocess, platform
#import os, subprocess
import multiprocessing as mp
from globals import DEFAULT_TINY_PATH_WIN11, DEFAULT_TINY_PATH_WIM_MOUNT, PY_WIN_LOGO,  TOTAL_CPUS, SYSTEM_ARCH
from globals import __RAW_BANNER__, DEFAULT_TINY_PATH  #srcPath, TOTAL_CPUS, WImfillPath, ESDfillPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath, defaultTinyPathWin11, appxPackagesToRemove
from globals import BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN
from globals import BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE, RESET
import win32com.client


def colored_print(color: str, message: str) -> None:
    print(f"{color}{message}{RESET}")
    

def confirmDocumentsPath() -> str:
    pass




def calcDriveSpace(drive: str) -> list:
    total, used, free = shutil.disk_usage(drive)
    # Convert free space to gigabytes
    free_gb: int = round(free / (1024 ** 3), 2)

    # Convert free space to terabytes if needed
    free_tb: int = round(free / (1024 ** 4), 2)

    # Check if free space is greater than or equal to 1 TB
    if free_gb >= 1024:
        # Calculate TB and remaining GB
        terabytes: int = int(free_tb)
        gigabytes: int = round((free_tb - terabytes) * 1024, 2)
        return terabytes, gigabytes
#        print(f"{terabytes} TB {gigabytes} GBs free")
    else:
        # Display in GB if less than 1 TB
        gb_space: list = [free_gb]
        return gb_space
#        print(f"{free_gb} GBs free")







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