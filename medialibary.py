#!/usr/bin/python3
#Billy Yost
#1/27/2020

def edit():
    print("running edit()")
    

def  print_all():
    print("running print_all()")
    

def search_by_title():
    print("running search_by_title")
    
    
def remove_game():
    print("running romove_game()")
    
    
def save():
    print("saving")
    
    
def quit():
    print("Quiting. Goodbye.")
    exit()
    
    
while True:
    print('''
    
    --------------------------
    
    MAIN MENU    
    1) Edit
    2) Print All Games
    3) Search by Title
    4) Remove a Game
    5) Save
    
    0) Quit
    ''')
    choice = input("What would you like to do? ")
    
    if choice == "1":
        edit()
    elif choice == "2":
        print_all()
    elif choice == "3":
        search_by_title()
    elif choice == "4":
        remove_game()
    elif choice == "5":
        save()
    
    elif choice == "0":
        quit()
    else:
        print("*** NOT A VALID CHOICE ***" "\n")        