import os, subprocess
from helper_fun import is_dism_available, checkUserInputYorN, CheckOnMkDir, checkIfPathExists, GetWIMinfoReturnFormatted #, get_processor_architecture
from globals import srcPath, tempDir, sample_input, menu_items, ESDPathAlien, defaultTinyPath


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
    

def action_save_settings():
    print("menu for saving settings to json etc coming soon. For now place holder")
    
    
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






#    print(menu)
#    print(split_input)    
#    print(menu_collect)


#title:
#title:
#title:
#title:
#title:
#title:
