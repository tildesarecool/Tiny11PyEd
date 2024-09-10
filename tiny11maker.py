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

import tomllib, shutil
import os, subprocess
#from helper_fun import is_dism_available, checkUserInputYorN, converIndexList, CheckOnMkDir, checkIfPathExists, GetWIMinfoReturnFormatted, convertESDtoWIM, ValidateSanitizePath
from globals import  defaultTinyPathWin11, defaultTinyPathWimMount, PY_WIN_LOGO, colored_print, TOTAL_CPUS, SYSTEM_ARCH, YELLOW, MAGENTA, RESET, CYAN, GREEN, BLUE, __RAW_BANNER__, defaultTinyPath  #srcPath, TOTAL_CPUS, WImfillPath, ESDfillPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath, defaultTinyPathWin11, appxPackagesToRemove

def calcCDriveSpace() -> list:
    total, used, free = shutil.disk_usage("C:/")
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

def main():

    colored_print(CYAN, __RAW_BANNER__)
    colored_print(GREEN, PY_WIN_LOGO)

#    colored_print(BLUE, f"Welcome to Tiny11 Maker\n\n")
    print("All below defaults can be customized in settings\n")
    print("Working directory is set to:") 
    colored_print(YELLOW, f"{defaultTinyPath}\n")
    print(f"Windows 11 install source (such as ISO contents) will be copied to:")
    colored_print( YELLOW, f"{defaultTinyPathWin11}\n")

    print(f"The install.wim file will be mounted at location:")
    colored_print( YELLOW, f"{defaultTinyPathWimMount}\n\n")

    if calcCDriveSpace()[0] != 0:
        print(f"You have {calcCDriveSpace()[0]} Gigabytes of free space") #{calcCDriveSpace()[1]}")
    else:
        print(f"You have {calcCDriveSpace()[0]} TBs, {calcCDriveSpace()[1]} GBs free")


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
        
        

if __name__ == "__main__":
    main()
    
    
































