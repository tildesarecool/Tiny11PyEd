# based upon
#  tiny11maker.ps
# by ntdevlabs - https://github.com/ntdevlabs/tiny11builder
# 3 September 2024
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


import os, subprocess
#from helper_fun import is_dism_available, checkUserInputYorN, converIndexList, CheckOnMkDir, checkIfPathExists, GetWIMinfoReturnFormatted, convertESDtoWIM, ValidateSanitizePath
from globals import PY_WIN_LOGO, colored_print, TOTAL_CPUS, SYSTEM_ARCH, GREEN, BLUE  #srcPath, TOTAL_CPUS, WImfillPath, ESDfillPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath, defaultTinyPathWin11, appxPackagesToRemove








def main():

    colored_print(GREEN, PY_WIN_LOGO)


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
    
    
































