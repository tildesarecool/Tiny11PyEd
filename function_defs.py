import tomllib, shutil, os, subprocess, platform, win32com.client
#import os, subprocess
import multiprocessing as mp
from globals import PY_WIN_LOGO, TOTAL_CPUS, SYSTEM_ARCH,  __RAW_BANNER__   #srcPath, TOTAL_CPUS, WImfillPath, ESDfillPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath, defaultTinyPathWin11, appxPackagesToRemove
from globals import defaultTinyPathWin11, defaultTinyPathWimMount, defaultTinyPath
from globals import BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE, RESET
#import win32com.client

#import pywin32

def colored_print(color: str, message: str) -> None:
    print(f"{color}{message}{RESET}")

def confirmDocumentsPath() -> str:
    
    shell = win32com.client.Dispatch("WScript.Shell")
    documents_path = shell.SpecialFolders("MyDocuments")
    return documents_path


def calcCDriveSpace(drive: str) -> list:
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
        gb_space = [free_gb]
        return gb_space
#        print(f"{free_gb} GBs free")