import os, subprocess
#from helper_fun import is_dism_available, checkUserInputYorN, CheckOnMkDir, checkIfPathExists #, get_processor_architecture
from globals import srcPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath, defaultTinyPathWin11, appxPackagesToRemove


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


def remove_quotes(path: str) -> str:
    """simple utility function to remove any single ' or double " quotes the user might have included in the path. 
    This version makes sure to remove only leading/trailing quotes, to avoid removing ' and/or " in file or folder names.

    Args:
        path (str): Path to have quotes stripped out of (leading/trailing)

    Returns:
        str: string path with no quotes
    """
    # it occured to me the last folder could just end with a quote mark. actually i think this boolean covers this edge case.
    
    if (path.startswith('"') and path.endswith('"')) or (path.startswith("'") and path.endswith("'")):
        return path[1:-1]
    return path


def is_dism_available():
    """
    Return bool for whether DISM is available on system. This really only needs to be called once. 
    And actually it could be the single test that decides if the main() function is even called. Because
    the script doesn't work without DISM. 
    """
    # Use os.system to run 'dism /?' and check if it returns 0
    # I realized I could make this line 
    # return (os.system('cmd /c dism /? >null') == 0)
    # and i'll likely change it. Sorry to trigger anybody's OCD.
    foundDismOrNot = os.system('cmd /c dism /? >null') == 0
    return foundDismOrNot


def checkUserInputYorN(userYNChoice: str, userInputPrompt: str) -> bool:
    """Like CheckOnMkDir(), this was supposed to a generic/all purpose function but it seems to still have some 
    left over lines tieing it directly to CheckOnMkDir(). This will have to be re-done in a refactor.

    Args:
        userYNChoice (str): y or n usually for yes or no questions. This needs to be re-written
        userInputPrompt (str): the prompt to the user asking for for Y or N 

    Returns:
        bool: Return True if user answers with y or a blank line. Return false in all other circumstances.
    """
    
#    userYNChoice = input(f"Alternatively, would you like to create the directory? (Y/n default: Y) ").strip().lower()
    if userInputPrompt != "":
        userYNChoice = input(f"{userInputPrompt.strip()} ").strip().lower()
    
    if userYNChoice == "y" or userYNChoice == "":
        return True
    else:
        return False


def CheckOnMkDir(DirToCreate: str) -> bool:
    """Attempt to create specified folder at specified location. This is supposed to be a generic
    re-usable function. I think I only use it once or twice. ATM it's probably not a big deal
    if it's not all purpose/generic.

    Args:
        DirToCreate (str): Path to folder to create

    Returns:
        bool: True if folder created successfully, return false with error code all other cases.
    """
    #DirToCreate = DirToCreate
    DirToCreate = remove_quotes(DirToCreate).strip().lower()
    
    # if the passed in path does NOT exist
    if not checkIfPathExists(DirToCreate):
        try: 
            # attempt to make passed in path/new folder and return true upon success
            print(f"value of dirtocreate is {DirToCreate}")
            os.makedirs(DirToCreate)
            return True
        # if the attempt to create the folder fails, throw an exception and print the error
        except OSError as e:
            #return str(e)
            print(f"Attempt to create path {DirToCreate} resulted in an error, please try again. \
\n\nError message for reference: \n\n{e}.\n")
        # then return false
        return False
    else:
        # if the path already exists, return true
        return True

def checkIfPathExists(PathToCheck: str) -> bool:
    """probably unncecessary abstraction to os.path.exists; sanitizes input if nothing else
    Possible ToDo: make sure this works if passed in path has spaces in it
    if that makes it not work come up with a way to deal with it

    There's at least one instance I use this function to check if a file exists - the esd/wim check exist function checkIfPathExists()
    I changed this to also check if the passed in PathToCheck is a directory or not
    so I need to either add a second parameter to specify checking on directory versus file or just use the one off check
    in that checkIfPathExists() function.
    """
    
    PathToCheck = PathToCheck.strip().lower()
    if os.path.exists(PathToCheck) and os.path.isdir(PathToCheck):
        return True
    else:
        return False



def GetWIMinfoReturnFormatted(ESDorWIMpath: str) -> str:
    """Runs the DISM GetWIMinfoReturnFormatted command against the path to the wim or ESD file and returns the PS window output
    as a string.

    Args:
        A path to the ESD or WIM file in the Windows source install folder (string).

    Returns:
        The re-formatted output of the DISM command as a string, such as below, no blank lines in between:
            Index : 1
            Name : Windows 11 Home
            Description : Windows 11 Home
            Size : 18,638,210,474 bytes
            Index : 2
            Name : Windows 11 Home N
            Description : Windows 11 Home N
            Size : 17,934,598,356 bytes
    """
    DISMgetInfo = f"""& dism /English /Get-WimInfo /wimfile:'{ESDorWIMpath}' | Select-String -Pattern 'Index :|Name :|Description :|Size :'""" #.strip("\n")

#    result = subprocess.run(["powershell", "-Command", DISMgetInfo], capture_output=True, text=True, check=True)

    try:    
        print("Attempting to get ESD/WIM info now...")
        result = subprocess.run(["powershell", "-Command", DISMgetInfo], capture_output=True, text=True, check=True)
        #print("Info gathered successfully:")
        # for later reference when researching another project i came across this line, which is what i need to utlize
        # just the endswith part, the email files is not really relevant 
        # email_files = [os.path.join(download_folder, f) for f in os.listdir(download_folder) if f.endswith('.eml')]
        # in retrospect i could have used lstrip/rstrip if i just wanted to cut out newlines at the top/bottom
        # but no blank lines at all is fine too
        DISMOutput = result.stdout.strip("\n")
#        print(f"Output return is \n{result.stdout}")
        #print(f"Output return is \n{DISMOutput}")
        return DISMOutput
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code: {e.returncode}")
        print(e.stderr)
    except FileNotFoundError as e:
        print(f"PowerShell not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
#    else:
       # return DISMOutput

def converIndexList(index_input: str) -> list:
    """Take in wim info output - see GetWIMinfoReturnFormatted() - and return only the needed portion of it

    Args:
        index_input (str): output of the dism /wiminfo command fully formatted as a string - 
        I've got it to the point this function works with the input in format such as
        
        Index : 1
        Name : Windows 11 Home
        Description : Windows 11 Home
        Size : 18,638,210,474 bytes
        Index : 2
        Name : Windows 11 Home N
        Description : Windows 11 Home N
        Size : 17,934,598,356 bytes

    Returns:
        list: After twice splitting the wim info, return the wim info as a list-of-lists.
        the return value will be returned in this format (with no line breaks) ready for the menu
        to prompt the user
        
        [['1', 'Windows 11 Home'], ['2', 'Windows 11 Home N'], ['3', 'Windows 11 Home Single Language'], 
        ['4', 'Windows 11 Education'], ['5', 'Windows 11 Education N'], ['6', 'Windows 11 Pro'], 
        ['7', 'Windows 11 Pro N'], ['8', 'Windows 11 Pro Education'], ['9', 'Windows 11 Pro Education N'], 
        ['10', 'Windows 11 Pro for Workstations'], ['11', 'Windows 11 Pro N for Workstations']]
        
        
    """
    
    
    list_collect = []
    
    split_value = "Index : ".strip()
    
    split_input = index_input.split(split_value)
    for indecies in range(len(split_input)):
        indexer = split_input[indecies]
        indexer = indexer.splitlines()
        indexer = indexer[:-2]
        
#        print(f"value of indexer is {indexer}")
        if indexer != []:
            indexer[0] = indexer[0].lstrip()
            indexer[1] = indexer[1].replace("Name : ", "")
            list_collect.append(indexer)    
            
    return list_collect


###### for possible use in future maybe
#def buildUpDismCLI():
#    if is_dism_available():
#        
#        pass



#    split_input = index_input.split("\n\n")
#    for indecies in range(len(split_input)):
#        indexer = split_input[indecies]
#        indexer = indexer.splitlines()
#        indexer = indexer[:-2]
#        
#        if len(indexer) == 2:
#            indexer[0] = indexer[0].replace("Index :", "")
#            indexer[1] = indexer[1].replace("Name", "")
#
#        list_collect.append(indexer)



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