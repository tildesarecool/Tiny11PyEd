import os, subprocess
#from helper_fun import is_dism_available, checkUserInputYorN, CheckOnMkDir, checkIfPathExists #, get_processor_architecture
from globals import srcPath, tempDir, sample_input, menu_items, ESDPathAlien


def is_dism_available():
    """
    Return bool for whether DISM is available on system.
    """
    # Use os.system to run 'dism /?' and check if it returns 0
    foundDismOrNot = os.system('cmd /c dism /? >null') == 0
    return foundDismOrNot


def checkUserInputYorN(userYNChoice: str) -> bool:
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
    """probably unncecessary abstraction to os.path.exists
    Possible ToDo: make sure this works if passed in path has spaces in it
    if that makes it not work come up with a way to deal with it
    """
    PathToCheck = PathToCheck.strip().lower()
    if os.path.exists(PathToCheck):
        return True
    else:
        return False



def getIndexNumberPref() -> str:
#    ESDPathAlien = """P:\\ISOs\\Windows10-22h2\\sources\\install.esd"""
#    LaptopSrcPath = """C:\\Users\\keith\\Documents\\tiny11\\Win11_23H2_x64v2-unmodified\\sources\\install.wim"""

#    DISMgetInfo = f"""
#& dism /English /Get-WimInfo /wimfile:'{ESDPathAlien}'   | Select-String -Pattern 'Index :|Name :|Description :|Size :'
#"""

    DISMgetInfo = f"""& dism /English /Get-WimInfo /wimfile:'{ESDPathAlien}'   | Select-String -Pattern 'Index :|Name :|Description :|Size :'""" #.strip("\n")


    #print(f"DISMGet info is \n{DISMgetInfo}")
    #print("Attempting to get ESD/WIM info now...")
    result = subprocess.run(["powershell", "-Command", DISMgetInfo], capture_output=True, text=True, check=True)
#    print("Info gathered successfully:")
    #DISMOutput = result.stdout.strip("\n")
#    print(f"Output return is \n{result.stdout}")

    try:    
        print("Attempting to get ESD/WIM info now...")
        result = subprocess.run(["powershell", "-Command", DISMgetInfo], capture_output=True, text=True, check=True)
        print("Info gathered successfully:")
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




###### for possible use in future maybe
#def buildUpDismCLI():
#    if is_dism_available():
#        
#        pass