# based upon
#  tiny11maker.ps
# by ntdevlabs - https://github.com/ntdevlabs/tiny11builder
# 5 June 2024
# 
#  Todo: check if script is running with local admin privileges.
#  Probably implement this last or later at least
# 
import os, subprocess
from helper_fun import is_dism_available, checkUserInputYorN, converIndexList, CheckOnMkDir, checkIfPathExists, GetWIMinfoReturnFormatted, remove_quotes #, get_processor_architecture
from globals import srcPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath, defaultTinyPathWin11

def SetTinyWorkDir() -> str:
    """    This function is supposed to:
    
    a) use a default working directory path if none is specified (and create folder as necessary)
    
    b) let user specify a path to be used as a working directory
    
    c) continue running this function until a valid path is reached. Should probably use an infinite
    loop rather than recursion. Something for later maybe.
    
    d) do appropriate exist checks on paths where required and sanitize input for easy return
    
    It could still use some work but it's close enough for now.GetWIMinfoReturnFormatted

    Returns:
        str: Once the directory path has been set return that path as a string (presumably sanitized and validated).
    """
    
    
    
        
            
    print(f"Please enter path for a temp directory.\
    \nDefault: press enter to use '{defaultTinyPath}' \
    \nNote: Assume at least ~20GB of drive space will be required (for ISOs etc) (ctrl+c to get quit script)")
    setworkpath = input("Enter a path (no quotes): ") # does adding .strip at the end work? Dare I to dream?
    setworkpath = remove_quotes(setworkpath).strip().lower()

    if setworkpath == "":
        print(f"Working directory set to default location of {defaultTinyPath}")
#        defaultTinyPath = os.getenv('USERPROFILE') + "\documents\\tiny11"
        if checkIfPathExists(defaultTinyPath): #os.path.exists(defaultTinyPath):       
            print(f"\nThe default path of {defaultTinyPath} is being used.")
            return defaultTinyPath 
            
        else:
            print(f"Default path {defaultTinyPath} not found, creating directory.")
            if CheckOnMkDir(setworkpath): #os.makedirs(defaultTinyPath):
                print(f"Path {defaultTinyPath} created. Path set.")
                return defaultTinyPath
            else:
                SetTinyWorkDir()

    elif setworkpath != "":
        if checkIfPathExists(setworkpath): # os.path.exists(setworkpath):
            print(f"Working directory set to '{setworkpath}'")
            return setworkpath
        else:
            print(f"The path '{setworkpath}' could not be found. Things to check: \
\n1. no quotes are required, remove at leading/trailing quotes \
\n2. make sure path is a folder not a file, \
\n3. also try shift+right click to copy as path a folder and paste (and remove quotes) \
\n- on Win 11 you may have to `see more options` \
\n") 
            #YNCreateDir = input(f"Alternatively, would you like to create directory {setworkpath}? (Y/N) ").strip().lower()
            if checkUserInputYorN("y", "Alternatively, would you like to create the directory? (Y/n default: Y)"): #YNCreateDir == "y":
                if CheckOnMkDir(setworkpath):
                    print(f"Path '{setworkpath}' successfully created  ")
                    return setworkpath
                else:
                    SetTinyWorkDir()
            else:
                SetTinyWorkDir()


def SetWindowsSourcePath() -> str:
    """Ask user for the source of the windows install. This can be a mounted ISO like D: 
    or the full path to an existing install source. During the file copy this will what it's 
    copying from. Or the "source". Does a check to see if the path exists and runs strips spaces.

    Returns:
        str: This returns a sanitized string of the path the user specified (after it's checked if it exists).
    """
    
    
    
    print("Please specifiy a path for the root of a Windows 11 installations source. \
\nThis can be a mounted ISO, a physical CD/DVD drive with an install disk, \
\nor a directory (extracted from an ISO for instance). The 'root' will have a 'sources' subfolder \
\nSample Paths: \
\nD: \
\nc:\\ISOs\\Windows11-24h1 \
\nNote: Do not include any quotes around the path \
\n(You can try a UNC but I don't think it would work and would be really slow anyway)")

    winSourcePath = input("\nEnter path to Windows install drive (or directory): ").lower().lstrip().rstrip()
#    This srcpath is true thing is worst way to do this. But I don't feel like making it more
#   elegant at the moment so it'll have to do.

    srcpath = checkIfPathExists(winSourcePath) # os.path.exists(winSourcePath)

    
    if srcpath:
        print(f"Install directory source set to '{winSourcePath}'")
        return winSourcePath
    else:
        print(f"Path {winSourcePath} not found. Please enter a path.\n")
        SetWindowsSourcePath()


def checkWIMorESDFileExists(WinInstallSourceRoot: str) -> str:
    """
    Takes in string as path and returns path string
    
    Takes in a path to a root of the an install source and 
    combines it with the location of either a WIM or ESD
    It checks if that ESD or WIM exists and returns either that path
    or an empty string.    
    """
    
    WImfillPath = """\\sources\\install.wim"""
    ESDfillPath = """\\sources\\install.esd"""
    
    WimPath = WinInstallSourceRoot + WImfillPath
    ESDPath = WinInstallSourceRoot + ESDfillPath

#    print(f"Value of wimpath is {WimPath}")
#    print(f"Value of esdpath is {ESDPath}")
    
    
    
    if checkIfPathExists(WimPath):
        print(f"WIM file {WimPath} found")
        return WimPath
    elif checkIfPathExists(ESDPath):
        print(f"ESD file {ESDPath} found")
        return ESDPath
    else:
        print(f"No WIM or ESD file found at specified location")
        return ""
        
        


def processWimInfo():
    """Use the output of converIndexList() to present the information to the user and ask for an index number

    Args:
        None

    Returns:
        Return the user's index number to be used for the next step - either convertESDtoWIM() or (coming soon)
    """


    
#    dismWimIndexCMD = """& 'DISM' /Export-Image /SourceImageFile:"$DriveLetter\sources\install.esd" /SourceIndex:$index /DestinationImageFile:"$ScratchDisk\tiny11\sources\install.wim" /Compress:max /CheckIntegrity"""

    processInput = converIndexList(sample_input)

    for osIndexes in processInput:
        print(f"{osIndexes[0]}\t for OS {osIndexes[1]}")

    print("0 to quit")
    response = input("Enter OS choice: ").strip()
    if response != "":

        for userIn in range(len(processInput)):
            print(f"userin is value {userIn}")
            if int(response) == 0:
                print("Please enter a number for an OS")
            elif int(response) == userIn and userIn != 0:
                response = userIn
    
#    dismWimIndexCMD = f"""DISM /Export-Image /SourceImageFile: {response}""".strip()
#    print(dismWimIndexCMD)

    return response

def convertESDtoWIM(ESDToConvertPath: str, WIMDestPath: str ):
    """Take in path the input ESD and path to output WIM file. save WIM file at the end. This function only runs if an ESD is used.

    Args:
        These need work. Full path to ESD and WIM path. I think the wim path is only for the folder since the default file name of
        install.wim is used (technically the only input is install.esd)

    Returns:
        None at the moment. this may change.
    """
    
    
    
    print(f"Your source folder has an install.esd file: Tiny 11 can only work with WIM files in order to \"Tiny it\". \nOn a Core i7 from 2019 this takes about 7 minutes")
    print(f"Source ESD file location: {ESDToConvertPath}\nInstall.wim file will be saved to: {WIMDestPath}")
    
    if ESDToConvertPath[-1] == "d":

        buildDISMFinal = f"""& DISM /Export-Image /SourceImageFile:'{ESDToConvertPath}' /SourceIndex:3 /DestinationImageFile:'{WIMDestPath}\\install.wim' /Compress:max /CheckIntegrity"""

        try:
            print("Starting ESD to WIM conversion now...")
            result = subprocess.run(["powershell", "-Command", buildDISMFinal], capture_output=True, text=True, check=True)
            print("Conversion completed successfully")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code: {e.returncode}")
            print(e.stderr)
        except FileNotFoundError as e:
            print(f"PowerShell not found: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def processWimInfo(WIMInfoList: str) -> int:
    #dismWimIndexCMD = """& 'DISM' /Export-Image /SourceImageFile:"$DriveLetter\sources\install.esd" /SourceIndex:$index /DestinationImageFile:"$ScratchDisk\tiny11\sources\install.wim" /Compress:max /CheckIntegrity"""

    #processInput = converIndexList(sample_input)
    #processInput = converIndexList(GetWIMinfoReturnFormatted())

    for osIndexes in WIMInfoList:
    #    print(f"OS {osIndexes[1]} is selection: {osIndexes[0]}  \t")
    # the default for \t is 8 spaces and apparently you can change this to another value. so 4.
        print(f"{osIndexes[0]}\tfor {osIndexes[1]}".expandtabs(4))

    print("0 to quit")
    response = input("Enter OS choice: ").strip()
    if response != "":
#        if int(response) == 0:
#            print("No OS entered")
#            pass

        for userIn in range(len(WIMInfoList)):
            #print(f"userin is value {userIn}")
            if int(response) == 0:
                print("Please enter a number for an OS")
            elif int(response) == userIn and userIn != 0:
                response = userIn
    
#    dismWimIndexCMD = f"""DISM /Export-Image /SourceImageFile: {response}  """.strip()
    #print(dismWimIndexCMD)

    return response


if __name__ == "__main__":
    def main():
    #convertESDtoWIM(checkWIMorESDFileExists("""P:\ISOs\Windows10-22h2"""), SetTinyWorkDir() ) # f"""{ os.getenv('USERPROFILE')}\documents\\tiny11""")

        #print(f"value returned by is dism available is --{is_dism_available()}--")        
        
        if is_dism_available() and defaultTinyPath:
#            WinSrcRoot = SetWindowsSourcePath()            
#            
#            #print(f"Windows source dir is {WinSrcRoot}")
#            WIMPath = checkWIMorESDFileExists(WinSrcRoot)
#            #print(f"wimpath value is {WIMPath}")
#            WIMInfoGet = GetWIMinfoReturnFormatted(WIMPath)
#
#            WimInfoAsList = converIndexList(WIMInfoGet)
#            #print(f"wiminfo as list is {WimInfoAsList}")
#            UserOSPref = processWimInfo(WimInfoAsList)
#            print(f"After processing WIM info user os pref value is {UserOSPref}")

            WorkDir = SetTinyWorkDir()

            print(f"Work dir value is {WorkDir}")
#
#        WinSrcRoot = SetWindowsSourcePath()
#
#        print(f"Windows source dir is {WinSrcRoot}")
#
#        checkWIMorESDFileExists(WinSrcRoot)

        #pass


main()

#        print(f"\nNow running conversion line --> \n")
#        os.system(buildDISMFinal)
    #destPath = f"{os.getenv('USERPROFILE')}\documents\\tiny11"
    #destPath = checkWIMorESDFileExists("P:\ISOs\Windows10-22h2")
        #buildDISMFinal = f"""& DISM /Export-Image /SourceImageFile:'P:\ISOs\Windows10-22h2\sources\install.esd' /SourceIndex:3 /DestinationImageFile:'{destPath}\install.wim' /Compress:max /CheckIntegrity"""
#    buildDISMTwo = f"'P:\ISOs\Windows10-22h2\sources\install.esd' /SourceIndex:3 /DestinationImageFile:"""
#    buildDISMThree = f"'{destPath}\install.wim /Compress:max /CheckIntegrity'"

#    buildDISMFinal = f"{buildDISMOne}{buildDISMTwo}{buildDISMThree}{buildDISMThree}"

# & DISM /Export-Image /SourceImageFile:P:\ISOs\Windows10-22h2\sources\install.esd /SourceIndex:3 /DestinationImageFile:'C:\Users\Keith\documents\tiny11\install.wim' /Compress:max /CheckIntegrity



    #pass
#    menu_list(menu_items)
#    WimOrESD = checkWIMorESDFileExists( SetWindowsSourcePath() )
#    print(f"WimOrESD value is {WimOrESD}")
#    if WimOrESD is not "":
#        if WimOrESD[-1] == "d":
#            processWimInfo()

# & DISM /Export-Image /SourceImageFile:"'P:\ISOs\Windows10-22h2\sources\install.esd' /SourceIndex:3 /DestinationImageFile:'C:\Users\Keith\documents\tiny11\install.wim' /Compress:max /CheckIntegrity


#    cpu_arch = get_processor_architecture()
#    SetTinyWorkDir()
    
#    SetWindowsSourcePath()
    #checkWIMorESDFileExists("P:\ISOs\Win 11\Win11_23H2_English_x64v2")
    #checkWIMorESDFileExists(SetWindowsSourcePath())

#########    
#    MainMenu()
##########



#menu_items = [
#
##    {"title": "Welcome to Tiny11 - Python Edition\n\n\n Please choose from the folowing options:" , "action": action_placeholder },
#    {"title": "\n 0.\tQuit " , "action": exit},
#    {"title": " 1.\tSet Windows install source directory", "action": SetWindowsSourcePath},
#    {"title": " 2.\tSet Temp eg `scratch` directory ", "action": SetTinyWorkDir },
#    {"title": " 3.\tView/edit Settings " , "action": action_save_settings},
#    {"title": " 4.\tCheck if ESD/Wim file exists " , "action": checkIfPathExists },
#    {"title": " 5.\tCheck if dism available " , "action": is_dism_available},
#    {"title": "\n999.\t!!Just do the thing already!! ", "action": action_placeholder }
#
#]






#    global srcPath
#    global MenuItemTitle
#    global MenuItemZero
#    global MenuItemOne
#    global MenuItemTwo
#    global MenuItemThree
#    global MenuItemFour
#    global MenuItemFive
#    global MenuItemNineNine
#
#    print(MenuItemTitle) 
#    print(MenuItemZero)
#    print(MenuItemOne)
#    print(MenuItemTwo)
#    print(MenuItemThree)
#    print(MenuItemFour)
#    print(MenuItemFive)
#    print(MenuItemNineNine)
#
#
#    userReply = input().strip().lower()    
#
#    if int(userReply) == 0 or userReply == "": 
#        exit()
#
#    elif int(userReply) == 1:
#        srcPath = SetWindowsSourcePath()
#        print(f"Windows Source Path set to {srcPath}")
#
#        MainMenu()
#    elif int(userReply) == 2:
#        tempDir = SetTinyWorkDir()
#        MainMenu()
#    elif int(userReply) == 3:
#        print("menu for saving settings to json etc coming soon. For now place holder")
#        MainMenu()
#        pass
#    elif int(userReply) == 4:
#        if srcPath is not None:
#            
#            WimEsd = checkWIMorESDFileExists(srcPath)
#            print(f"--VALUE OF wimESD IS {WimEsd}--")
#        else:
#            print("Path not yet set")
#        
#        #WimEsd = checkWIMorESDFileExists(srcPath)
#        MainMenu()
#    elif int(userReply) == 5:
#        print(f"Found DISM value is: {is_dism_available()}")        
#        MainMenu()
#    elif int(userReply) == 999:
#        print("Eventually this will do something. For now place holder")
#        MainMenu()
#        pass
#    if tempDir:
#        print(f"Temp dir currently set to {tempDir}")
#    else:
#        print("temp dir not set")

#    print(f"")
#    print(f"")
#    print(f"")



# MenuItemTitle
# MenuItemZero
# MenuItemOne
# MenuItemTwo
# MenuItemThree
# MenuItemFour
# MenuItemFive
# MenuItemNineNine

#"title": "Welcome to Tiny11 - Python Edition\n\n\n Please choose from the folowing options:" , "action": action_placeholder 



