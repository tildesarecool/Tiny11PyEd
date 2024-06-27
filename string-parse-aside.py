import subprocess, os

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

#sample_input.s


def getIndexNumberPref() -> str:
    ESDPath = """P:\\ISOs\\Windows10-22h2\\sources\\install.esd"""
    LaptopSrcPath = """C:\\Users\\keith\\Documents\\tiny11\\Win11_23H2_x64v2-unmodified\\sources\\install.wim"""
#    DISMgetInfo = f"""
#& dism /English /Get-WimInfo /wimfile:'{ESDPath}'   | Select-String -Pattern 'Index :|Name :|Description :|Size :'
#"""

    DISMgetInfo = f"""& dism /English /Get-WimInfo /wimfile:'{LaptopSrcPath}'"""#   | Select-String -Pattern 'Index :|Name :|Description :|Size :'""" #.strip("\n")


    #print(f"DISMGet info is \n{DISMgetInfo}")
    print("Attempting to get ESD/WIM info now...")
    result = subprocess.run(["powershell", "-Command", DISMgetInfo], capture_output=True, text=True, check=True)
#    print("Info gathered successfully:")
    #DISMOutput = result.stdout.strip("\n")
    print(f"Output return is \n{result.stdout}")

#    try:    
#        print("Attempting to get ESD/WIM info now...")
#        result = subprocess.run(["powershell", "-Command", DISMgetInfo], capture_output=True, text=True, check=True)
#        print("Info gathered successfully:")
#        DISMOutput = result.stdout.strip("\n")
#        print(f"Output return is \n{result.stdout}")
#       # return DISMOutput
#    except subprocess.CalledProcessError as e:
#        print(f"Command failed with return code: {e.returncode}")
#        print(e.stderr)
#    except FileNotFoundError as e:
#        print(f"PowerShell not found: {e}")
#    except Exception as e:
#        print(f"An unexpected error occurred: {e}")
#    else:
       # return DISMOutput

        
    #print(f"Output return is \n{result.stdout}")
    #print(DISMOutput)
    
    
getIndexNumberPref()

def converIndexList(index_input) -> list:
    
    list_collect = []
    
    #split_input = index_input.split("\n\n") # have to use a different split character because of wim info output formatting
    split_input = index_input.split("Index")
#    split_input = split_input[0]
    #print(f"value of split_input outside for loop is \n{split_input}" )
    for indecies in range(len(split_input)):
        indexer = split_input[indecies]
        indexer = indexer.splitlines()
        indexer = indexer[:-2]
        
        if len(indexer) == 2:
            indexer[0] = indexer[0].replace("Index :", "")
            indexer[1] = indexer[1].replace("Name", "")
#        index_count = index_count + 1

        list_collect.append(indexer)
        
#        print(f"value of indexer inside for loop and pre-enjoinment is \n---{indexer}---" )
        
#    print(f"value of list collector outside for loop is \n---{list_collect}---" )
#    print(f"index 0 of list collect is \n---{list_collect[0]}---" )
    
    return list_collect

def processWimInfo():
    #dismWimIndexCMD = """& 'DISM' /Export-Image /SourceImageFile:"$DriveLetter\sources\install.esd" /SourceIndex:$index /DestinationImageFile:"$ScratchDisk\tiny11\sources\install.wim" /Compress:max /CheckIntegrity"""

    #processInput = converIndexList(sample_input)
    processInput = converIndexList(getIndexNumberPref())

    for osIndexes in processInput:
    #    print(f"OS {osIndexes[1]} is selection: {osIndexes[0]}  \t")
        print(f"{osIndexes[0]}\t for OS {osIndexes[1]}")

    print("0 to quit")
    response = input("Enter OS choice: ").strip()
    if response != "":
#        if int(response) == 0:
#            print("No OS entered")
#            pass

        for userIn in range(len(processInput)):
            print(f"userin is value {userIn}")
            if int(response) == 0:
                print("Please enter a number for an OS")
            elif int(response) == userIn and userIn != 0:
                response = userIn
    
    dismWimIndexCMD = f"""DISM /Export-Image /SourceImageFile: {response}  """.strip()
    print(dismWimIndexCMD)

    return response

#processWimInfo()

#f"""
#$dismOutput = & dism /English /Get-WimInfo /wimfile:'{ESDPath}'
#$startIndex = $dismOutput.IndexOf($dismOutput | Select-String -Pattern 'Index :' | Select-Object -First 1)
#$filteredOutput = $dismOutput.Substring($startIndex)
#$filteredOutput
#"""


#processWimInfo()

######### only if i want to convert to string really bad
#        indexer = "\n".join(indexer)
#        print(f"value of indexer outside for loop is \n{indexer}" )
#        print(f"Indexer is of data type {type(indexer)}")
        
        
        
    
#    entry_one = entry_one.splitlines()
#    
#    entry_one = entry_one[:-2] # slice of size and descr
#    print(f"After slice and splitlines(), value of entry one is \n{entry_one}" )
#    entry_one[0] = entry_one[0].replace("Index", "Enter")
#    entry_one[1] = entry_one[1].replace("Name", "For entry")
#    
#    print(f"after replacement, value of entry one is \n{entry_one}" )
#    
#    entry_one = "\n".join(entry_one)
#    
#    print(f"after after enjoinment, value of entry one is \n{entry_one}" )
    
        #        elif int(response) == 0:
        #        elif int(response) == 0:
        #        elif int(response) == 0:
        #        elif int(response) == 0:
        #        elif int(response) == 0:
        #        elif int(response) == 0:
        #        elif int(response) == 0:
        #        elif int(response) == 0:
        #        elif int(response) == 0:
        #        elif int(response) == 0:
    
#first_index = sample_input.split("\n\n")
#
##print(sample_input)
#print(f"index 0 of first_index is {first_index[0]}")
#print(f"type of varialbe index 0 is {type(first_index)}")
#
#index_zero = first_index[0]
#
#print(f"before split line, entry one is \n{index_zero}")
#
#index_zero = index_zero.splitlines()
#
#index_zero.pop()
#index_zero[0] = index_zero[0].replace("Index", "Enter")
#
#print(f"after split line, entry one is \n{index_zero[0]}")
#
#