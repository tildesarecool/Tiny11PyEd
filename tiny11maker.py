# based upon
#  tiny11maker.ps
# by ntdevlabs - https://github.com/ntdevlabs/tiny11builder
# 5 June 2024
# 
#  Todo: check if script is running with local admin privileges.
#  Probably implement this last or later at least
# 
import os


srcPath = None
MenuItemTitle     = f"""Welcome to Tiny11 - Python Edition\n\n\n Please choose from the folowing options:"""
MenuItemZero      = f"""\n 0.\tQuit """
MenuItemOne       = f""" 1.\tSet Windows install source directory  """
MenuItemTwo       = f""" 2.\tSet Temp eg `scratch` directory """
MenuItemThree     = f""" 3.\tView/edit Settings """
MenuItemFour      = f""" 4.\tCheck if ESD/Wim file exists """
MenuItemFive      = f""" 5.\tCheck if dism available """
MenuItemNineNine  = f"""\n999.\t!!Just do the thing already!! """

def checkUserInputYorN(userYNChoice: str) -> bool:
    userYNChoice = input(f"Alternatively, would you like to create the directory? (Y/n default: Y) ").strip().lower()
    if userYNChoice == "y" or userYNChoice == "":
        return True
    else:
        return False

def is_dism_available():
    """
    Return bool for whether DISM is available on system.
    """
    # Use os.system to run 'dism /?' and check if it returns 0
    foundDismOrNot = os.system('cmd /c dism /? >null') == 0
    return foundDismOrNot

def buildUpDismCLI():
    if is_dism_available():
        
        pass

def get_processor_architecture():
    """ 
    I'm actually not sure what this arch identification is going to be used for. 
    ---> In the original PS script this is used in a path later on involving looking for 
    oscdimg.exe file in the ADK installation folder. Not a very high priority, in other words.
    """
    # processor_architecture = os.getenv('PROCESSOR_ARCHITECTURE')
    if os.getenv('PROCESSOR_ARCHITECTURE'):
        #print("processor arch found")
        return os.getenv('PROCESSOR_ARCHITECTURE')
    else:
        print("no value for processor arch found")
        return False

def set_temp_dir():
    """ 
    This function is supposed to:
    a) use a default working directory path if none is specified (and create folder as necessary)
    b) let user specify a path to be used as a working directory
    c) return false where necessary
    d) do appropriate exist checks on paths where required
    It could still use some work but it's close enough for now.
     """
        
    defpath = os.getenv('USERPROFILE') + """\documents\\tiny11"""
            
    print(f"Please enter path for a temp directory.\
    \nDefault: ({os.getenv('USERPROFILE')}\documents\\tiny11) \
    \nNote: Assume at least ~20GB of drive space will be required (for ISOs etc) ")
    setworkpath = input("Enter a path (no quotes): ").strip().lower() # does adding .strip at the end work? Dare I to dream?
    #setworkpath = setworkpath.strip()

    if setworkpath == "":
        print(f"Working directory set to default location of {defpath}")
#        defpath = os.getenv('USERPROFILE') + "\documents\\tiny11"
        if checkIfPathExists(defpath): #os.path.exists(defpath):       
            print(f"The default path of {defpath} is being used.")
            return defpath 
            
        else:
            print(f"Default path {defpath} not found, creating directory.")
            if CheckOnMkDir(setworkpath): #os.makedirs(defpath):
                print(f"Path {defpath} created. Path set.")
                return defpath
            else:
                set_temp_dir()

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
            if checkUserInputYorN(y): #YNCreateDir == "y":
                if CheckOnMkDir(setworkpath):
                    print(f"Path '{setworkpath}' successfully created  ")
                    return setworkpath
                else:
                    set_temp_dir()
            else:
                set_temp_dir()




def CheckOnMkDir(DirToCreate: str) -> bool:
    DirToCreate = DirToCreate.strip().lower()
    try: 
        os.makedirs(DirToCreate)
        return True
        #print(f"Successfully created path {setworkpath}")
    except OSError as e:
        #return str(e)
        
        print(f"Attempt to create path {DirToCreate} resulted in an error, please try again. \
\n\nError message for reference: \n\n{e}.\n")
        
        return False
#        set_temp_dir()



def SetWindowsSourcePath() -> str:
    print("Please specifiy a path for the root of a Windows 11 installations source. \
\nThis can be a mounted ISO, a physical CD/DVD drive with an install disk, \
\nor a directory (extracted from an ISO for instance). The 'root' will have a 'sources' subfolder \
\nSample Paths: \
\nD: \
\nc:\ISOs\Windows11-24h1 \
\nNote: Do not include any quotes around the path \
\n(You can try a UNC but I don't think it would work and would be really slow anyway)")

    winSourcePath = input("\nEnter path to Windows install drive (or directory): ").strip().lower()
#    This srcpath is true thing is worst way to do this. But I don't feel like making it more
#   elegant at the moment so it'll have to do.

    srcpath = checkIfPathExists(winSourcePath) # os.path.exists(winSourcePath)

    
    if srcpath:
        print(f"Install directory source set to '{winSourcePath}'")
        return winSourcePath
    else:
        print(f"Path {winSourcePath} not found. Please enter a path.\n")
        SetWindowsSourcePath()

def checkIfPathExists(PathToCheck: str) -> bool:
    """probably unncecessary abstraction to os.path.exists
    Possible ToDo: make sure this works if passed in path has spaces in it
    if that makes it not work come up with a way to deal with it
    """
    PathToCheck = PathToCheck.strip().lower()
    if os.path.exists(PathToCheck):
        return True
    else:
        return False



def checkWIMorESDFileExists(WinInstallSourceRoot: str):
    WImfillPath = """\\sources\\install.wim"""
    ESDfillPath = """\\sources\\install.esd"""
    
    WimPath = WinInstallSourceRoot + WImfillPath
    ESDPath = WinInstallSourceRoot + ESDfillPath
    
    if checkIfPathExists(WimPath):
        print(f"WIM file {WimPath} found")
        return WimPath
    elif checkIfPathExists(ESDPath):
        print(f"ESD file {ESDPath} found")
        return ESDPath
    else:
        print(f"No WIM or ESD file found at specified location")
        return ""
        
#\n 5.\tSet windows source path \
def MainMenu():
    
    global srcPath
    global MenuItemTitle
    global MenuItemZero
    global MenuItemOne
    global MenuItemTwo
    global MenuItemThree
    global MenuItemFour
    global MenuItemFive
    global MenuItemNineNine

    print(MenuItemTitle) 
    print(MenuItemZero)
    print(MenuItemOne)
    print(MenuItemTwo)
    print(MenuItemThree)
    print(MenuItemFour)
    print(MenuItemFive)
    print(MenuItemNineNine)


    userReply = input().strip().lower()    

    if int(userReply) == 0 or userReply == "": 
        exit()

    elif int(userReply) == 1:
        srcPath = SetWindowsSourcePath()
        print(f"Windows Source Path set to {srcPath}")

        MainMenu()
    elif int(userReply) == 2:
        tempDir = set_temp_dir()
        MainMenu()
    elif int(userReply) == 3:
        print("menu for saving settings to json etc coming soon. For now place holder")
        MainMenu()
        pass
    elif int(userReply) == 4:
        if srcPath is not None:
            
            WimEsd = checkWIMorESDFileExists(srcPath)
            print(f"--VALUE OF wimESD IS {WimEsd}--")
        else:
            print("Path not yet set")
        
        #WimEsd = checkWIMorESDFileExists(srcPath)
        MainMenu()
    elif int(userReply) == 5:
        print(f"Found DISM value is: {is_dism_available()}")        
        MainMenu()
    elif int(userReply) == 999:
        print("Eventually this will do something. For now place holder")
        MainMenu()
        pass
    if tempDir:
        print(f"Temp dir currently set to {tempDir}")
    else:
        print("temp dir not set")

#    print(f"")
#    print(f"")
#    print(f"")

if __name__ == "__main__":
#    cpu_arch = get_processor_architecture()
#    set_temp_dir()
    
#    SetWindowsSourcePath()
    #checkWIMorESDFileExists("P:\ISOs\Win 11\Win11_23H2_English_x64v2")
    #checkWIMorESDFileExists(SetWindowsSourcePath())
    
    MainMenu()
