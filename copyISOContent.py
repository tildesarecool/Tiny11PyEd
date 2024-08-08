

from globals import srcPath, WImfillPath, ESDfillPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath, defaultTinyPathWin11, appxPackagesToRemove, FAT32_MAX_FILE_SIZE
from typing import Union

from helper_fun import is_dism_available, checkUserInputYorN, converIndexList, CheckOnMkDir, checkIfPathExists, GetWIMinfoReturnFormatted, convertESDtoWIM, ValidateSanitizePath

import multiprocessing as mp
from multiprocessing import Pool
import os, shutil, time, threading, argparse, sys, msgpack

#FAT32_MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4 GB


#print(f"number is {FAT32_MAX_FILE_SIZE}")

