# based upon
#  tiny11maker.ps
# by ntdevlabs - https://github.com/ntdevlabs/tiny11builder
# 3 September 2024
# python -m venv venv
#  python -m pip install --upgrade pip   
# pip install -r .\requirements.txt   
# .\venv\Scripts\activate

# I created the image myself with Paint.NET and regualar paint. 
# Then converted it to ascii using 
# https://www.asciiart.eu/image-to-ascii
# It's supposed to be python shrinking Windows. Making it tiny. Did I pull it off? This one is for decoration.
# then this text ascii art I also found fun

# ████████╗██╗███╗   ██╗██╗   ██╗     ██╗ ██╗                              
# ╚══██╔══╝██║████╗  ██║╚██╗ ██╔╝    ███║███║                              
#    ██║   ██║██╔██╗ ██║ ╚████╔╝     ╚██║╚██║                              
#    ██║   ██║██║╚██╗██║  ╚██╔╝       ██║ ██║                              
#    ██║   ██║██║ ╚████║   ██║        ██║ ██║                              
#    ╚═╝   ╚═╝╚═╝  ╚═══╝   ╚═╝        ╚═╝ ╚═╝                              
#                                                                          
# ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗                               
# ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗                              
# ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝                              
# ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗                              
# ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║                              
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                              
#                                                                          
# ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗    ███████╗██████╗ 
# ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ██╔════╝██╔══██╗
# ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║    █████╗  ██║  ██║
# ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ██╔══╝  ██║  ██║
# ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ███████╗██████╔╝
# ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═════╝ 


#     
#                .-=+##@@@@@@@##+=:                                                                   
#            .-*@@@@@@@@@@@@@@@@@@@@%=:                                                               
#          .%@@@@@@@@@@@@@@@@@@@@@@@@@@@=.                                                            
#         #@@@@@@@@@@#+++++++++#@@@@@@@@@@#                                                           
#       *@@@@@@@@@=.            .=@@@@@@@@@@*                                                         
#     :@@@@@@@@@@*  @@%           :@@@@@@@@@@@:                                                       
#    =@@@@@@@@@@@+  *#+            @@@@@@@@@@@@=                                        -             
#   =@@@@@@@@@@@@*::::::::.        @@@@@@@@@@@@@=                               .  =:#%%@@#@+=-       
#  .@@@@@@@@%%%%%%%%%%%%%%=        @%%%%%@@@@@@@@.                             =@-.@@@@@@@@@*+@=      
#  @@@@@@@#                        @      -@@@@@@@                            .@@#@@@@@@@@@@@@#.-.    
# +@@@@@@+                         @       +@@@@@@+                          @@@@@@@@@@@@@@@@@@@+.    
# #@@@@@@                         =%        @@@@@@# #%%%:                    =@@@@@@@@@@@@@@@@@@+     
# @@@@@@+                       :+%.        *@@@@@@@@@@@@@%%+-:          =-+#@@@@@@@%##=====::+@@@    
# @@@@@@+         .=*+++++++++++#-          +@@@@@@=*****#%@@@@@##:.    .@@@@@@--:    +       .@@@*#*-
# @@@@@@+        +#:                        +@@@@@@         ==##%@@%**.+*@@@@@@...    +       .+@@@@@*
# #@@@@@@       +#                         .@@@@@@#               ==*@@@@@@@@@@...    +...    .+@@@@@%
# +@@@@@@+      ++                         +@@@@@@+                    -#@@@@@@+++++++#++++++++#@@@@@ 
#  @@@@@@@*     ++                        *@@@@@@@                      +@@@@@@.......+ .......+@@@@@ 
#  :@@@@@@@@%###%+        =#############%@@@@@@@@:                       *@@@@@ .     +        +@@@@@*
#   +@@@@@@@@@@@@+                 @@@@@@@@@@@@@+                        +@@@@@:......+........+@@@@* 
#    =@@@@@@@@@@@+            *#=  @@@@@@@@@@@@=                         :-=#@@@@@%##*#=-----..+@@@@+ 
#     :@@@@@@@@@@*.           #%= =@@@@@@@@@@@:                              @@@@@@@@@@@@@@@@@@@@+:   
#       *@@@@@@@@@%=.           .*@@@@@@@@@@*                                =*@@@@@@@@@@@%@@*=:      
#         #@@@@@@@@@@@@+++++++@@@@@@@@@@@@#                                       +#  +#@-            
#          :%@@@@@@@@@@@@@@@@@@@@@@@@@@@=:                                             ..             
#            .-*@@@@@@@@@@@@@@@@@@@@%+-                                                               
#                .-=*##@@@@@@@##*=:                                                                   
# 
# 

import tomllib, shutil, os, subprocess, platform
#import os, subprocess
#from helper_fun import is_dism_available, checkUserInputYorN, converIndexList, CheckOnMkDir, checkIfPathExists, GetWIMinfoReturnFormatted, convertESDtoWIM, ValidateSanitizePath
from globals import DEFAULT_TINY_PATH_WIN11, DEFAULT_TINY_PATH_WIM_MOUNT, PY_WIN_LOGO,  TOTAL_CPUS, SYSTEM_ARCH
from globals import __RAW_BANNER__, DEFAULT_TINY_PATH  #srcPath, TOTAL_CPUS, WImfillPath, ESDfillPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath, defaultTinyPathWin11, appxPackagesToRemove
from globals import BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN
from globals import BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE, RESET
from function_defs import colored_print, calcDriveSpace, confirmDocumentsPaths


def main():
    confirmDocumentsPath()
#    print(f"value of documents path is \n{confirmDocumentsPath()}")

    #colored_print(CYAN, __RAW_BANNER__)
    #colored_print(GREEN, PY_WIN_LOGO)

#    colored_print(BLUE, f"Welcome to Tiny11 Maker\n\n")

#    print(f"doc path is {confirmDocumentsPath()}")

    print("All below defaults can be customized in settings\n")
    print("Working directory is set to:")
    colored_print(YELLOW, f"{DEFAULT_TINY_PATH}\n")
    print(f"Windows 11 install source (such as ISO contents) will be copied to:")
    colored_print( YELLOW, f"{DEFAULT_TINY_PATH_WIN11}\n")

    print(f"The install.wim file will be mounted at location:")
    colored_print( YELLOW, f"{DEFAULT_TINY_PATH_WIM_MOUNT}\n\n")

if __name__ == "__main__":
    main()

    # print(f"calcDriveSpace(confirmDocumentsPath()) is now {calcDriveSpace(confirmDocumentsPath())}")
    # print(f"calcDriveSpace(confirmDocumentsPath())[0] is now {calcDriveSpace(confirmDocumentsPath())[0]}")
    # print(f"calcDriveSpace('c:')[0] is now {calcDriveSpace('c:')[0]}")
    
#    drive_space = calcDriveSpace('c:')[0]
#    if drive_space is not None:
#        print(f"calcDriveSpace('c:')[1] is now {calcDriveSpace('c:')[0]}")

#    if calcDriveSpace(confirmDocumentsPath())[0] == 0:
#        print(f"You have {calcDriveSpace(confirmDocumentsPath()[0])} Gigabytes of free space") #{calcCDriveSpace()[1]}")
#    else:
#        print(f"You have {calcDriveSpace(confirmDocumentsPath())[0]} TBs, {calcDriveSpace(confirmDocumentsPath())} GBs free")

#    if confirmDocumentsPath() == os.getenv('USERPROFILE') + "documents":
#        print("\n\nThe paths match")

#    WinSrcRoot = SetWindowsSourcePath()            
#    #print(f"Windows source dir is \n{WinSrcRoot}")
#    
#    WorkDir = SetTinyWorkDir()
#    #print(f"Work dir value is {WorkDir}")
#    
#    WIMPath = checkWIMorESDFileExists(WinSrcRoot)
#    
#    WIMInfoGet = GetWIMinfoReturnFormatted(WIMPath)
#    WimInfoAsList = converIndexList(WIMInfoGet)
#    UserOSPref = processWimInfo(WimInfoAsList)        
        
        



    
    

