# Tiny11Builder - Python Edition

Scripts to build a trimmed-down Windows 11 image - now in...Python?

Below I have something of a development log (in case you have a need to read boring stuff). 
<p>

This started out as a fork of [Tiny11 by ntdevlabs](https://github.com/ntdevlabs/tiny11builder), a PowerShell script to remove certain components from a Windows 10/11 install source.  Today I decided to save the fork repo for a PS edition fork and save this python edition to a separate repo. That went about as well as I expected (time consuming/difficult).

</p>

<p>

Just so there's no confusion here, I don't think this will ever replace the PS version of this script. And there's no reason to write this in Python given the advantages of using PS for the purpose. This is more of an exercise than anything else.

Also, One of the main motivations for wanting to re-write this (besides Python practice) is the amount time it takes for the various tasks, such as generating the new ISO (I'm hoping I can improve on the time required). I am also working on much more communications with the user. 

I might actually come back and re-write it using actually PS too. Or you know re-write my Python script based on a PS script...in PS.

</p>

<p>
I haven't dissected the PS script yet but I should be able to support Windows 10 and 11 and any architecture (though since I don't care about ARM that will be at the bottom of the priority list).
</p>

<p>
One possible disadvantage of using this version is needing an install of Python (I wasn't planning to convert to exe).
</p>

<p>

I'm not sure yet if I'll utilize the same approach to creating a bootable ISO using oscdimg but I likely will not be able to get around using DISM. I will use the included unattend file at as a base for my own - I happen to have my own unattend files and want to skip a lot more things (like UELA agreement checkbox, keyboard language/layout and OS language).

</p>

<p>

Like the original, this is open-source, **so feel free to add or remove anything you want!** Feedback is also much appreciated.

</p>

<p>

It's too soon to say if I'll try to also reproduce  **tiny11 core builder**.  I will have to save that for last and deicied if it's worthwhile.
</p>

Instructions:

1. Download Windows 11 from the Microsoft website (<https://www.microsoft.com/software-download/windows11>)
2. Mount the downloaded ISO image using Windows Explorer.
3. (This step will be replaced/TBD)
4. Select the SKU that you want the image to be based: I'll replace the UI/presentation of this step
5. Sit back and relax :)
6. Re-building an ISO takes too long. I really hope I can improve this. 

What is removed (TBD):

- Clipchamp
- News
- Weather
- Xbox (although Xbox Identity provider is still here, so it should be possible to be reinstalled with no issues)
- GetHelp
- GetStarted
- Office Hub
- Solitaire
- PeopleApp
- PowerAutomate
- ToDo
- Alarms
- Mail and Calendar
- Feedback Hub
- Maps
- Sound Recorder
- Your Phone
- Media Player
- QuickAssist
- Internet Explorer
- Tablet PC Math
- Edge
- OneDrive

For tiny11 core (TBD):

Known issues:

TBD

Features to be implemented:

- option to import a custom hosts file?
- maybe a GUI? A TUI?
- Autounattend.xml selection/generation?
- Save settings as profile and select that for later? 
- Settings saved to JSON file?
- Error handling?
- I could offer to make Win 11 skip CPU etc checks. This might be too complicated. 

<p>

### Prior to June 6th 2024

I started breaking out the different sections into functions. The PS original is just one giant long block of code with very few breaks. I wanted to put it into sections to make it easier to read as well easier to debug later. I didn't get very far in, just barely started.

I'm doing this Python re-write in the worst way possible: just writing functions as I read the code. What I should do is re-organize the PS script to have spacing between different sections, summarize the functionality and then list out what I'm going to write step-by-step before I even written one line of Python. But instead I'm writing a Python version as I read a section of PS script. 

This why I wrote that get_processor_architecture() function already even though I have no idea where or if it will be needed later on. I also did it via environment variable like the PS script did even though that's likely not necessary.

I have already come with some improvements, though: instead of simply creating an arbibrary folder on the root of the user's C: drive I ask the user if they'd like to specify a working directory and mention the path that can be used by default if none is specified. This just seems more elegant and considerate of the user. I even do some input validation and offer suggestions if a path comes back invalid. I'm going to come back to that later but I already like it more than before.  

The next problem I had with the PS version was the script only except a drive letter (with no colon) for the Windows install source. I mean when I used this PS script I actually used a really old DOS command called SUBST so I could use a subdirectory as the source rather than actually mounting an ISO. I mean it just copies the contents some place else anyway I don't think I really that made the process better. But my script will let the user specify either a drive letter OR a folder some place on the PC.  This functionality doesn't work all the way quite yet but will by the time the script is done.

<hr>

### 7 June 2024

So far I've learned that the scratch directory is actually the location in the filesystem the the WIM file is mounted.

Since I defaulted this directory to %USERPROFILE%\documents\tiny11 that is where the WIM filesystem will be located.  I also realized the script converts an install.ESD file to a WIM file. Might explain some of the time it takes to run. 
 
I've made a few edits but mostly researched a possible solution to one of the script's operations taking a really long time. Which I'll do in the most needlessly complicated way possible (you're welcome). It invovles MemoryFS, tmpfile and symbolic links. I'll probably do some benchmarks to prove the feasibility before really adding it in. Or add it in anyway because hilarious. 


### 8 June 2024

I spent an emberacing amount of time trying to figure out if I could use DISM to take in an ESD file and output a WIM file directly to a RAM disk. The answer is no, not that I can find. I mean maybe there's a way using more advanced memory manipulation, I don't know. But in short without a device driver to make a piece of RAM look like a block device for Windows to write to, there doesn't seem to be a way. 

So the choices are either a) just write the converted WIM file to the local storage like some kind of normal person or b) use imDisk to create the RAM disk and write it. I was trying to avoid having to use a third party utility but if that's the only way than that's what I'll have to do. Since I don't know if I'm allowed to redistribute imDisk or if user's would even be open to utilizing it I haven't decided if I want to bother. I'll do some bench marks and see if it's worth bothering. Or just label it "experimental". I think imDisk functions can be access via PS. I have read into that more.

As an aside, I ended up finding a lot of scripts on GitHub that do basically the same thing as Tiny11Builder. Like a script doing this is some kind of right of passage. 

I did this research instead of what I really needed to do: create a simple algorithm for taking in the output a DISM command and presenting that informaiton as a menu. 

The command is 

```
dism "/Get-WimInfo" "/wimfile:$DriveLetter\sources\install.esd"
```

This produces output in format

```
Index : 1
Name : Windows 11 Home
Description : Windows 11 Home
Size : 18,638,210,474 bytes

Index : 2
Name : Windows 11 Home N
Description : Windows 11 Home N
Size : 17,934,598,356 bytes
```

Except with 7 or 8 indexes. 

What I need is a function that takes in that output, splits each grouping of index/name/description/size into seperate lists (using '\n\n' as the iterator) and takes *each list* and: chops off size and descripotion, changes the word "Index" to something else like "Enter" and "Name" to "for version" or something like that. 

So for instance 

```
Index : 1
Name : Windows 11 Home
Description : Windows 11 Home
Size : 18,638,210,474 bytes
```

Is index 0 (including the line breaks). 

I was able to remember pop() cuts off the last elements of a list. But I found a reference that reminded that slice is a thing. Something like this:

```Python
entryOne = [
    "Index : 1",
    "Name : Windows 11 Home",
    "Description : Windows 11 Home",
    "Size : 18,638,210,474 bytes"
]

# Slice the last two lines
entryOne = entryOne[:-2]
```
This seems much better.

Now all I need is a for-loop to do that to all the entries. 

Alright, in a separate experimental script I ended up with this function. It's not "pretty"  but it takes in that list of indexes and returns of list-of-lists for the edited entries.

The idea is I'll use a for loop to generate a menu for the user to select. Of course I still have to build out a menu that excepts input for each of these entries and responds. And other minor details. But I'm so glad I at least got this far.

```Python
def converIndexList(index_input) -> list:
    
    list_collect = []
    
    split_input = index_input.split("\n\n")
#    split_input = split_input[0]
    #print(f"value of split_input outside for loop is \n{split_input}" )
    for indecies in range(len(split_input)):
        indexer = split_input[indecies]
        indexer = indexer.splitlines()
        indexer = indexer[:-2]
        
        if len(indexer) == 2:
            indexer[0] = indexer[0].replace("Index", "Enter")
            indexer[1] = indexer[1].replace("Name", "For entry")
#        index_count = index_count + 1

        list_collect.append(indexer)
        
#        print(f"value of indexer inside for loop and pre-enjoinment is \n---{indexer}---" )
        
    print(f"value of list collector outside for loop is \n---{list_collect}---" )
    print(f"index 0 of list collect is \n---{list_collect[0]}---" )
    
    return list_collect

```

### 9 June 2024

As I progress through the PS script the full picture of it starts to get more and more clarified. And my opinion on the quality hasn't increased at all. 

 I'm going to ignore several things for now, perhaps maybe coming back later:
 - non-english/international languages for UI etc
 - 32-bit and arm based sources

The script goes through several things before it it really even gets to the meat of it:
- it establishes a "scratch drive" - it copies the whole source to a tiny11 subfolder
- converts any install.esd file to an install.WIM file/deletes the ESD 
- removes read-only flag from wim file if found
- asks user for which index file listed in the install.wim file to use
- based on the entered index, mounts the install wim file to root of the scratch directory
- Then removes a list of appx packages from the mounted WIM file

I was wondering what took it so long to complete various tasks. I think I have my answer. Even with a decent CPU and an NVME drive these tasks are going to take a while. And there's still the minor detail of re-creating an ISO. Using that third party RAM disk utility is sounding more and more tempting. Since it takes ~45 minutes to complete this task right now.

What I'd kind of like to do is query a list of available appx packages and present that to the user. And maybe add a yes/no to continue if not a choose each individual one. Somehow that seems better than the just-trust-me-bro approach to an arbirary list of appx packages to remove. Maybe it's just me. Or I think a default list of packages to be removed with a bail-out option to add/remove other packages manually somehow. 

### 12 June 2024

Only the two functions for taking in and processing the WIM output got most done today. Well one takes in the WIM info as a big string and converts that string to a lists of lists. The second function loops through the that list and prints out a menu to select to the OS. I still haven't gone through and  done all the if/else statements to use those menu items to actually select which OS. That will likely come next. 

### 13 June 2024

I switched python edition to a new repo so I can save the fork repo for later. And made progress on the actual script, too.

### 16 June 2024

I have done some further diving into the PS version of the script and actually broke up the code a bit by adding some new lines and comments designating diffrent areas of the script. I found some redundant code that seems like it was just made for a function.

I also came up what I believe to be a clever way to get the user's preference on an index number for the WIM file. You know, instead of just showing the user the output of the /wiminfo DISM command, saving it to a variable and using that variable in the finished DISM mount command. That sounds easier when I say it like that. Input validation and a for loop is way better probably. Obviously the script still needs a lot of work. 

### 17 June 2024

I came up with a special function just for handling attempts to create a subfolder for the user: attempt to create folder and if it's successful return true other wise print a message displaying the error from the OS then return false.

This worked out since I've already needed to call it twice.

There's another instance where I copy/pasted some code which should obviously also be a seperate function. And I would do that but at some point it feels like I probably want to do some actual WIM processing.

Writing that sparked a random thougt: would it be possible to set some the tasks in the script as a background process with python? For instance in doing the file copy of the install source to the working directory could I put that in the back ground then continue the script to get to the ESD/WIM conversion and put that into the background and continue. Then I might have to also have progress bars always on the screen too. But that probably isn't a big deal. Also have to handle error message gracefully as well. That could be harder. Maybe if I partioned the screen up. That's a thing, right?

### 18 June 2024

I made some helper or "utility" functions and started implementing in the functions they're needed. I also made the first function towards the task of converting an install.esd to install.wim if found.

I also added the try/except of the script. I was having an issue returning the value of an error for the calling function to utilize. I assume that's possible.

I think next I'll probably create the main menu function.

### 19 June 2024

I started on the main menu. It has some choices and calls some functions but doesn't actually do anything yet.

### 24 June 2024

I continued to work on the menu system and managed to make it worse I think. I might have to come back to this.

### 25 June 2024

I decided to put the menu system on hold while I work on more functionality of the actual script: I wrote a new function for converting an install.ESD to an install.WIM file. 

Actually it's not technically done. I'm still working on making python call the DISM command. My testing so far has only involved printing the final DISM command and my manually copy/pasting that output into PowerShell. I have found a solution though so that will likely come in tomorrow.

### 26 June 2024

I've worked further on the best way to get the output from various powershell commands and save the output. I think I made progress on this but there's still many steps left.

### 28 June 2024

I've been working on this same little bit for what seems like entirely too long. But really I just don't spend enough time per day working on it then stretched out over weeks. 

That's a long way to say I did some re-organizing and refactoring today: firstly I split the main python file into multiple files and secondly I did some refactoring. Hopefully it will be easier to track functions and what they do this way. I often do this on fly. The bob ross approach to programming. Which is definitely the right way.

</p>
