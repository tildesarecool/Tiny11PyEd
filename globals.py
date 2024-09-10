import os, platform
import multiprocessing as mp

srcPath = None
tempDir = None

FAT32_MAX_FILE_SIZE = 4 * 1024**3  # 4 GB

TOTAL_CPUS = mp.cpu_count()

SYSTEM_ARCH = platform.architecture()[0]



# packages to remove. Use '#' to comment out any you don't want removed.
appxPackagesToRemove: tuple = (
'Clipchamp.Clipchamp_', 
'Microsoft.BingNews_', 
'Microsoft.BingWeather_', 
'Microsoft.GamingApp_', 
'Microsoft.GetHelp_', 
'Microsoft.Getstarted_', 
'Microsoft.MicrosoftOfficeHub_', 
'Microsoft.MicrosoftSolitaireCollection_', 
'Microsoft.People_', 
'Microsoft.PowerAutomateDesktop_', 
'Microsoft.Todos_', 
'Microsoft.WindowsAlarms_', 
'microsoft.windowscommunicationsapps_', 
'Microsoft.WindowsFeedbackHub_', 
'Microsoft.WindowsMaps_', 
'Microsoft.WindowsSoundRecorder_', 
'Microsoft.Xbox.TCUI_', 
'Microsoft.XboxGamingOverlay_', 
'Microsoft.XboxGameOverlay_', 
'Microsoft.XboxSpeechToTextOverlay_', 
'Microsoft.YourPhone_', 
'Microsoft.ZuneMusic_', 
'Microsoft.ZuneVideo_', 
'MicrosoftCorporationII.MicrosoftFamily_', 
'MicrosoftCorporationII.QuickAssist_', 
'MicrosoftTeams_', 
'Microsoft.549981C3F5F10_')

############################################################################################################
# THESE COLORS ONLY WORK ON WINDOWS 10 AND LATER (not made with Linux etc in mind)
# This is an alternative to having to use another library like colorama. Not very many colors but I can work with it
# example using with normal print: 
# print(f"{RED}This is red text{RESET}")

# Standard Colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright Colors
BRIGHT_BLACK = "\033[90m"   # Often appears as gray
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Reset
RESET = "\033[0m"    
###########################    

# Could also use this utility function...
def colored_print(color, message):
    print(f"{color}{message}{RESET}")

# Usage
#colored_print(RED, "This is red text")
#colored_print(BRIGHT_GREEN, "This is bright green text")
ANSI_COLORS: tuple = (
BLACK, 
RED, 
GREEN, 
YELLOW, 
BLUE, 
MAGENTA, 
CYAN, 
WHITE, 
BRIGHT_BLACK, 
BRIGHT_RED, 
BRIGHT_GREEN, 
BRIGHT_YELLOW, 
BRIGHT_BLUE, 
BRIGHT_MAGENTA, 
BRIGHT_CYAN, 
BRIGHT_WHITE, 
RESET
)
############################################################################################################


__RAW_BANNER__ = '''
████████╗██╗███╗   ██╗██╗   ██╗     ██╗ ██╗                              
╚══██╔══╝██║████╗  ██║╚██╗ ██╔╝    ███║███║                              
   ██║   ██║██╔██╗ ██║ ╚████╔╝     ╚██║╚██║                              
   ██║   ██║██║╚██╗██║  ╚██╔╝       ██║ ██║                              
   ██║   ██║██║ ╚████║   ██║        ██║ ██║                              
   ╚═╝   ╚═╝╚═╝  ╚═══╝   ╚═╝        ╚═╝ ╚═╝                              
                                                                         
███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗                               
████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗                              
██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝                              
██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗                              
██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║                              
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                              
                                                                         
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗    ███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ██╔════╝██╔══██╗
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║    █████╗  ██║  ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ██╔══╝  ██║  ██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ███████╗██████╔╝
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═════╝ '''


PY_WIN_LOGO = """
               .-=+##@@@@@@@##+=:                                                                   
           .-*@@@@@@@@@@@@@@@@@@@@%=:                                                               
         .%@@@@@@@@@@@@@@@@@@@@@@@@@@@=.                                                            
        #@@@@@@@@@@#+++++++++#@@@@@@@@@@#                                                           
      *@@@@@@@@@=.            .=@@@@@@@@@@*                                                         
    :@@@@@@@@@@*  @@%           :@@@@@@@@@@@:                                                       
   =@@@@@@@@@@@+  *#+            @@@@@@@@@@@@=                                        -             
  =@@@@@@@@@@@@*::::::::.        @@@@@@@@@@@@@=                               .  =:#%%@@#@+=-       
 .@@@@@@@@%%%%%%%%%%%%%%=        @%%%%%@@@@@@@@.                             =@-.@@@@@@@@@*+@=      
 @@@@@@@#                        @      -@@@@@@@                            .@@#@@@@@@@@@@@@#.-.    
+@@@@@@+                         @       +@@@@@@+                          @@@@@@@@@@@@@@@@@@@+.    
#@@@@@@                         =%        @@@@@@# #%%%:                    =@@@@@@@@@@@@@@@@@@+     
@@@@@@+                       :+%.        *@@@@@@@@@@@@@%%+-:          =-+#@@@@@@@%##=====::+@@@    
@@@@@@+         .=*+++++++++++#-          +@@@@@@=*****#%@@@@@##:.    .@@@@@@--:    +       .@@@*#*-
@@@@@@+        +#:                        +@@@@@@         ==##%@@%**.+*@@@@@@...    +       .+@@@@@*
#@@@@@@       +#                         .@@@@@@#               ==*@@@@@@@@@@...    +...    .+@@@@@%
+@@@@@@+      ++                         +@@@@@@+                    -#@@@@@@+++++++#++++++++#@@@@@ 
 @@@@@@@*     ++                        *@@@@@@@                      +@@@@@@.......+ .......+@@@@@ 
 :@@@@@@@@%###%+        =#############%@@@@@@@@:                       *@@@@@ .     +        +@@@@@*
  +@@@@@@@@@@@@+                 @@@@@@@@@@@@@+                        +@@@@@:......+........+@@@@* 
   =@@@@@@@@@@@+            *#=  @@@@@@@@@@@@=                         :-=#@@@@@%##*#=-----..+@@@@+ 
    :@@@@@@@@@@*.           #%= =@@@@@@@@@@@:                              @@@@@@@@@@@@@@@@@@@@+:   
      *@@@@@@@@@%=.           .*@@@@@@@@@@*                                =*@@@@@@@@@@@%@@*=:      
        #@@@@@@@@@@@@+++++++@@@@@@@@@@@@#                                       +#  +#@-            
         :%@@@@@@@@@@@@@@@@@@@@@@@@@@@=:                                             ..             
           .-*@@@@@@@@@@@@@@@@@@@@%+-                                                               
               .-=*##@@@@@@@##*=:                                                                   

"""


ESDPathAlien = """P:\\ISOs\\Windows10-22h2\\sources\\install.esd"""

defaultTinyPath: str = os.getenv('USERPROFILE') + """\\documents\\tiny11""" 

defaultTinyPathWin11: str = defaultTinyPath + """\\win11"""
defaultTinyPathWimMount: str = defaultTinyPath + """\\WimMount"""

CreateTiny11Tree = f"""Create folder tree for Tiny11:
Default: 
{defaultTinyPath}
---> Win11
---> WimMount
"""


WIM_REL_PATH = """\\sources\\install.wim"""
ESD_REL_PATH = """\\sources\\install.esd"""

# WimPath = WinInstallSourceRoot + WImfillPath
# ESDPath = WinInstallSourceRoot + ESDfillPath

# not sure i already thought of this: check if 
# userprofile/documents/tiny11 already exists


menu_items = "0.\tQuit action" # 
#\n1.\tSet Windows install source directory \
#\n2.\tSet Temp eg `scratch` directory \
#\n3.\tView/edit Settings \
#\n4.\tCheck if ESD/Wim file exists  \
#\n5.\tCheck if dism available action: is_dism_available \
#\n999.\t!!Just do the thing already!! \
#"





sample_input = """Index : 1
Name : Windows 11 Home
Description : Windows 11 Home
Size : 18,638,210,474 bytes

Index : 2
Name : Windows 11 Home N
Description : Windows 11 Home N
Size : 17,934,598,356 bytes

Index : 3
Name : Windows 11 Home Single Language
Description : Windows 11 Home Single Language
Size : 18,601,482,575 bytes

Index : 4
Name : Windows 11 Education
Description : Windows 11 Education
Size : 18,903,796,443 bytes

Index : 5
Name : Windows 11 Education N
Description : Windows 11 Education N
Size : 18,240,855,358 bytes

Index : 6
Name : Windows 11 Pro
Description : Windows 11 Pro
Size : 18,936,583,647 bytes

Index : 7
Name : Windows 11 Pro N
Description : Windows 11 Pro N
Size : 18,259,384,849 bytes

Index : 8
Name : Windows 11 Pro Education
Description : Windows 11 Pro Education
Size : 18,903,746,653 bytes

Index : 9
Name : Windows 11 Pro Education N
Description : Windows 11 Pro Education N
Size : 18,240,804,668 bytes

Index : 10
Name : Windows 11 Pro for Workstations
Description : Windows 11 Pro for Workstations
Size : 18,903,771,548 bytes

Index : 11
Name : Windows 11 Pro N for Workstations
Description : Windows 11 Pro N for Workstations
Size : 18,240,830,013 bytes"""


