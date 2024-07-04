import os, subprocess
#from helper_fun import is_dism_available, checkUserInputYorN, CheckOnMkDir, checkIfPathExists #, get_processor_architecture
from globals import srcPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath


def is_dism_available():
    """
    Return bool for whether DISM is available on system. This really only needs to be called once. 
    And actually it could the single test that decides if the main() function is even called. Because
    the script doesn't work without DISM. 
    """
    # Use os.system to run 'dism /?' and check if it returns 0
    # I realized I could make this line return (os.system('cmd /c dism /? >null') == 0)
    # and i'll likely change it. Sorry to trigger anybody's OCD.
    foundDismOrNot =  os.system('cmd /c dism /? >null') == 0
    return foundDismOrNot


def checkUserInputYorN(userYNChoice: str) -> bool:
    """Like CheckOnMkDir(), this was supposed to a generic/all purpose function but it seems to still have some 
    left over lines tieing it directly to CheckOnMkDir(). This will have to be re-done in a refactor.

    Args:
        userYNChoice (str): y or n usually for yes or no questions. This needs to be re-written

    Returns:
        bool: Return True if user answers with y or a blank line. Return false in all other circumstances.
    """
    
    userYNChoice = input(f"Alternatively, would you like to create the directory? (Y/n default: Y) ").strip().lower()
    if userYNChoice == "y" or userYNChoice == "":
        return True
    else:
        return False



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



def CheckOnMkDir(DirToCreate: str) -> bool:
    """Attempt to create specified folder at specified location. This is supposed to be a generic
    re-usable function. I think I only use it once or twice. ATM it's probably not a big deal
    if it's not all purpose/generic.

    Args:
        DirToCreate (str): Path to folder to create

    Returns:
        bool: True if folder created successfully, return false with error code all other cases.
    """
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




def checkIfPathExists(PathToCheck: str) -> bool:
    """probably unncecessary abstraction to os.path.exists; sanitizes input if nothing else
    Possible ToDo: make sure this works if passed in path has spaces in it
    if that makes it not work come up with a way to deal with it
    """
    PathToCheck = PathToCheck.strip().lower()
    if os.path.exists(PathToCheck):
        return True
    else:
        return False



def GetWIMinfoReturnFormatted(ESDorWIMpath: str) -> str:
    """Runs the DISM GetWIMinfoReturnFormatted command against the path to the wim or ESD file and returns the PS window output
    as a string.

    Args:
        A path to the ESD or WIM file in the Windows source install folder (string).

    Returns:
        The re-formatted output of the DISM command as a string, such as below, no blank lines inbetween:
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
        print("Info gathered successfully:")
        # for later reference when researching another project i came across this line, which is what i need to utlize
        # just the endswith part, the email files is not really relevant 
        # email_files = [os.path.join(download_folder, f) for f in os.listdir(download_folder) if f.endswith('.eml')]
        # in retrospect i could have used lstrip/rstrip if i just wanted to cut out newlines at the top/bottom
        # but no blank lines at all is fine too
        DISMOutput = result.stdout.strip("\n")
#        print(f"Output return is \n{result.stdout}")
        print(f"Output return is \n{DISMOutput}")
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