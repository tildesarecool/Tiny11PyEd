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
tempDir = None

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




menu_items = "0.\tQuit action" # 
#\n1.\tSet Windows install source directory \
#\n2.\tSet Temp eg `scratch` directory \
#\n3.\tView/edit Settings \
#\n4.\tCheck if ESD/Wim file exists  \
#\n5.\tCheck if dism available action: is_dism_available \
#\n999.\t!!Just do the thing already!! \
#"


def menu_list(menu):
    menu_collect = []
#    
    split_input = menu.split("\t")
    
    for m_items in range(len(split_input)):
        indexer = split_input[m_items]
        indexer = indexer.splitlines()
#        
        menu_collect.append(indexer)
    
    for list_cont in range(len(menu_collect)):
        print(f"content is {menu_collect[list_cont]}")
    
#    print(menu)
#    print(split_input)    
#    print(menu_collect)


#title:
#title:
#title:
#title:
#title:
#title:

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

def set_temp_dir() -> str:
    """ 
    This function is supposed to:
    a) use a default working directory path if none is specified (and create folder as necessary)
    b) let user specify a path to be used as a working directory
    c) --return false where necessary--> no return bools
    d) do appropriate exist checks on paths where required
    It could still use some work but it's close enough for now.
     """
        
    defpath = os.getenv('USERPROFILE') + """\documents\\tiny11"""
            
    print(f"Please enter path for a temp directory.\
    \nDefault: press enter to use ({os.getenv('USERPROFILE')}\documents\\tiny11) \
    \nNote: Assume at least ~20GB of drive space will be required (for ISOs etc) (ctrl+c to get quit script)")
    setworkpath = input("Enter a path (no quotes): ").strip().lower() # does adding .strip at the end work? Dare I to dream?
    #setworkpath = setworkpath.strip()

    if setworkpath == "":
        print(f"Working directory set to default location of {defpath}")
#        defpath = os.getenv('USERPROFILE') + "\documents\\tiny11"
        if checkIfPathExists(defpath): #os.path.exists(defpath):       
            print(f"\nThe default path of {defpath} is being used.")
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
            if checkUserInputYorN("y"): #YNCreateDir == "y":
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



def checkWIMorESDFileExists(WinInstallSourceRoot: str) -> str:
    WImfillPath = """\\sources\\install.wim"""
    ESDfillPath = """\\sources\\install.esd"""
    
    WimPath = WinInstallSourceRoot + WImfillPath
    ESDPath = WinInstallSourceRoot + ESDfillPath

    print(f"Value of wimpath is {WimPath}")
    print(f"Value of esdpath is {ESDPath}")
    
    
    
    if checkIfPathExists(WimPath):
        print(f"WIM file {WimPath} found")
        return WimPath
    elif checkIfPathExists(ESDPath):
        print(f"ESD file {ESDPath} found")
        return ESDPath
    else:
        print(f"No WIM or ESD file found at specified location")
        return ""
        
        
def action_save_settings():
    print("menu for saving settings to json etc coming soon. For now place holder")
#\n 5.\tSet windows source path \
    
    
def action_placeholder():
    print("Eventually this will do something. For now place holder")
    
    
def MainMenu():
    
    while True:
        print("Welcome to Tiny11 - Python Edition\n\n\n Please choose from the folowing options:")
    
        for item in menu_items:
            print(item["title"])
            
        userReply = input("Choose an option: ").strip().lower()
        
        try:
            user_choice = int(userReply)
            
            action = next((item["action"] for item in menu_items if int(item["title"].split('.')[0]) == user_choice), None)
            
            if action:
                action()
            else:
                print("Invalid choice, please try again.")
                
        except ValueError:
                print("Invalid choice, please try again.")

def converIndexList(index_input) -> list:
    
    list_collect = []
    
    split_input = index_input.split("\n\n")
    for indecies in range(len(split_input)):
        indexer = split_input[indecies]
        indexer = indexer.splitlines()
        indexer = indexer[:-2]
        
        if len(indexer) == 2:
            indexer[0] = indexer[0].replace("Index :", "")
            indexer[1] = indexer[1].replace("Name", "")

        list_collect.append(indexer)
            
    return list_collect

def processWimInfo():
    dismWimIndexCMD = """& 'DISM' /Export-Image /SourceImageFile:"$DriveLetter\sources\install.esd" /SourceIndex:$index /DestinationImageFile:"$ScratchDisk\tiny11\sources\install.wim" /Compress:max /CheckIntegrity"""

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
    
    dismWimIndexCMD = f"""DISM /Export-Image /SourceImageFile: {response}  """.strip()
    print(dismWimIndexCMD)

    return response


def convertESDtoWIM(ESDToConvertPath: str, WIMDestPath: str ):
    #destPath = f"{os.getenv('USERPROFILE')}\documents\\tiny11"
    #destPath = checkWIMorESDFileExists("P:\ISOs\Windows10-22h2")
    
    print(f"Your source folder has an install.esd file: Tiny 11 can only work with WIM files in order to \"Tiny it\". On a Core i7 from 2019 this takes about 7 minutes")
    print(f"Source ESD file location: {ESDToConvertPath}\nInstall.wim file will be saved to: {WIMDestPath}")
    
    if ESDToConvertPath[-1] == "d":
        #buildDISMFinal = f"""& DISM /Export-Image /SourceImageFile:'P:\ISOs\Windows10-22h2\sources\install.esd' /SourceIndex:3 /DestinationImageFile:'{destPath}\install.wim' /Compress:max /CheckIntegrity"""
        buildDISMFinal = f"""& DISM /Export-Image /SourceImageFile:'{ESDToConvertPath}' /SourceIndex:3 /DestinationImageFile:'{WIMDestPath}\install.wim' /Compress:max /CheckIntegrity"""
#    buildDISMTwo = f"'P:\ISOs\Windows10-22h2\sources\install.esd' /SourceIndex:3 /DestinationImageFile:"""
#    buildDISMThree = f"'{destPath}\install.wim /Compress:max /CheckIntegrity'"

#    buildDISMFinal = f"{buildDISMOne}{buildDISMTwo}{buildDISMThree}{buildDISMThree}"
    
        print(f"\nNow running conversion line --> \n")
        os.system(buildDISMFinal)


if __name__ == "__main__":
    convertESDtoWIM(checkWIMorESDFileExists("""P:\ISOs\Windows10-22h2"""), set_temp_dir() ) # f"""{ os.getenv('USERPROFILE')}\documents\\tiny11""")


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
#    set_temp_dir()
    
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
#    {"title": " 2.\tSet Temp eg `scratch` directory ", "action": set_temp_dir },
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
#        tempDir = set_temp_dir()
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