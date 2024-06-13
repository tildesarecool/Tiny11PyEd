# based upon
#  tiny11Coremaker.ps
# by Tiny11 by ntdevlabs - https://github.com/ntdevlabs/tiny11builder
# 5 June 2024
# 
#  Todo: check if script is running with local admin privileges.
#  Probably implment this last or later at least
# 
import os

def is_dism_available():
    """
    Return bool for whether DISM is available on system.
    """
    # Use os.system to run 'dism /?' and check if it returns 0
    return os.system('dism /?') == 0

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
# Ideas for later:
# Report free space of the SystemRoot (C:) drive and compare to estimated required. 
# Also other ideas to be filled in here
#      
    defpath = os.getenv('USERPROFILE') + "\documents\\tiny11"
    if os.path.exists(defpath):        
        print(f"defpath is {defpath}")
    else:
        os.makedirs(defpath)
        print(f"Folder successfully created: {defpath}")
    print(f"Please enter path for a temp directory.\
    \nDefault: ({os.getenv('USERPROFILE')}\documents\\tiny11) \
    \nNote: Assume at least ~20GB of drive space will be required (for ISOs etc) ")
    setworkpath = input("Enter a path (no quotes): ").strip() # does adding .strip at the end work? Dare I to dream?
    #setworkpath = setworkpath.strip()

    if setworkpath == "":
        print(f"Working directory set to {defpath}")
        return defpath

    elif setworkpath != "":
        if os.path.exists(setworkpath):
            print(f"Working directory set to '{setworkpath}'")
            return setworkpath
        else:
            print(f"The path '{setworkpath}' could not be found. Things to check: no quotes are required, make sure path is a folder not a file, also try shift+right click to 'copy as path' a folder and paste")
            return False

def SetWindowsSourcePath():
    print("Please specifiy a path for the root of a Windows 10 or 11 installations source. \
\nThis can be a mounted ISO, a physical CD/DVD drive with an install disk, \
\nor a directory  (extracted from an ISO for instance). The 'root' will have a 'sources' subfolder \
\nSample Paths: \
\nD: \
\nc:\ISOs\Windows11-24h1 \
\n(You can try a UNC but I don't think it would work and would be really slow anyway)")

    winSourcePath = input("Enter path to Windows install drive (or directory): ")
    winSourcePath = winSourcePath.strip()

    if winSourcePath != "":
        srcpath = True
    else:
        srcpath = False
    
    if srcpath and os.path.exists(winSourcePath):
        print(f"Install directory source set to '{winSourcePath}'")
        return winSourcePath
    else:
        pass


if __name__ == "__main__":
#    cpu_arch = get_processor_architecture()
    if set_temp_dir():
        pass
        #tempdir = set_temp_dir()
    else:
        set_temp_dir()
    
    SetWindowsSourcePath()
