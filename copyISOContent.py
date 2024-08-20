

from globals import srcPath, TOTAL_CPUS, WImfillPath, ESDfillPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath, defaultTinyPathWin11, appxPackagesToRemove, FAT32_MAX_FILE_SIZE
from typing import Union

from helper_fun import is_dism_available, checkUserInputYorN, converIndexList, CheckOnMkDir, checkIfPathExists, GetWIMinfoReturnFormatted, convertESDtoWIM, ValidateSanitizePath

import multiprocessing as mp
from multiprocessing import Pool
import os, shutil, time, threading, argparse, sys, msgpack

PROGRESS_RUNNING = False

# moved to globals file
#FAT32_MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4 GB


#print(f"number is {FAT32_MAX_FILE_SIZE}")

class CopyISOTree:
    def __init__():
        pass
    def fs_fat32_determine(drvletter: str) -> int:
        """Return true or false for fat32 filesystem given a drive letter.
        
        Also false if there is no such drive letter since the 'raise ValueError' apparently doesn't work
        
        drive letters created by google drive return fat32...
        
        """
        validate_drive = os.path.splitdrive(drvletter)[0].rstrip().lstrip()
        
    #PathToCheck = PathToCheck.lstrip().rstrip()
        if os.path.exists(validate_drive): # and os.path.isdir(PathToCheck):
#            print(os.path.exists(validate_drive))

            drive_info = os.popen(f"fsutil fsinfo volumeinfo {validate_drive}").read()
            if 'FAT32' in drive_info:
                #return 'FAT32'
                return 1
            return 0
        else:
            return -1


############# how to use the fat32 method           
#fat32_true_false = CopyISOTree.fs_fat32_determine('k:')
#print(f"fat32_true_false true/false is {fat32_true_false}")
#
#if fat32_true_false < 0:
#    print("drive letter does not exist")
#elif fat32_true_false == 0:
#    print("drive letter found and it is NOT fat32")
#else:
#    print("drive letter found and it IS fat32")
############# how to use the fat32 method


