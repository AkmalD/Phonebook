import os
import re

def Menu():
    print(" _____  _                      ____              _")    
    print("|  __ \| |                    |  _ \            | |")   
    print("| |__) | |__   ___  _ __   ___| |_) | ___   ___ | | __")
    print("|  ___/| '_ \ / _ \| '_ \ / _ \  _ < / _ \ / _ \| |/ /")
    print("| |    | | | | (_) | | | |  __/ |_) | (_) | (_) |   <") 
    print("|_|    |_| |_|\___/|_| |_|\___|____/ \___/ \___/|_|\_\\")
    print("\n\n")

def AddContact():
    try:
            File1 = open("Name.txt", "a")
            temp1 = input("Enter contact name: ")
            temp2 = input("Enter phone number: ")
            File1.write("{}\n".format(temp1 + "\t\t" + temp2))
            File1.close()
    except Exception as e:
        print("There is a Problem", str(e))

def Display():
    os.system('cls')
    View = open("Name.txt", "r")
    print("======================\nName\t\tNumber\n======================")
    print(View.read())
    View.close()

def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print('Contact is exist')
        else:
            print('Contact does not exist')

def editContact():
    Choose = input("What do you want to edit (Name/Number)?")
    if Choose == "Name" or Choose == "name":
        obj2 = open("Name.txt","r")  
        old_ContactName= input("Enter old Contact Name : ")               
        new_ContactName= input("Enter new Contact Name : ")
        s = re.sub(old_ContactName, new_ContactName, obj2.read())      

        obj1 = open("Name.txt","w")
        obj1.writelines(s)
        obj2.close()
        obj1.close()
    elif Choose == "Number" or Choose == "number":
        obj2 = open("Name.txt","r")  
        old_ContactNumber= input("Enter old Contact Number : ")               
        new_ContactNumber= input("Enter new Contact Number : ")
        s = re.sub(old_ContactNumber, new_ContactNumber, obj2.read())     

        obj1 = open("Name.txt","w")
        obj1.writelines(s)
        obj2.close()
        obj1.close()
    else:
        print("It's a wrong input!!!")
        input("Click enter to next")

def DeleteContact(Confirm, Delete):
    if Confirm == 'y' or Confirm == 'Y':
        with open('Name.txt', 'r') as Name:
            Lines = Name.readlines()
            NewLine = [line for line in Lines if Delete not in line]
            with open('Name.txt', 'w') as Name:
                Name.writelines(NewLine)
        Display()
        print("\nContact has been deleted")
        input("Click enter to next")
    elif Confirm == 'n' or Confirm == 'N':
        print("This contact will not be deleted")
        input("Click enter to next")

while True:
    os.system('cls')
    try:
        os.system('cls')
        Menu()
        choice = int(input("Menu:\n1. Add new contact\n2. Delete Contact\n3. Search Contact\n4. Edit Contact\n5. Display Contact\n6. Exit\nEnter your choice: "))
        #Add Contact
        if choice == 1:
            AddContact()
        #Delete Contact
        elif choice == 2:
            if os.path.getsize('Name.txt') == 0:
                print("File is empty!")
                input("Click enter to next")
            else: 
                os.system('cls')
                Display()
                Delete = input("Choose a contact: ")
                with open("Name.txt", 'r') as file:
                    # read all content of a file
                    content = file.read()
                    # check if string present in a file
                    if Delete in content:
                        Confirm = input("Are you sure want to delete this contact y/n? ")
                        DeleteContact(Confirm, Delete)
                    else:
                        print("There's no contact with this name!")
                        input("Click enter to next")
        #Search Contact        
        elif choice == 3:
            os.system('cls')
            Cari =  input("Enter name of contact that you want to search: ")
            search_str('Name.txt', Cari)
            input("Click enter to next")
        #Edit Contact
        elif choice == 4:
            Display()
            editContact()

        #Display Contact
        elif choice == 5:
            if os.path.getsize('Name.txt') == 0:
                print("File is empty!")
                input("Click enter to next")
            else:
                Display()
                input("Click enter to next")
        #Exit Program
        elif choice == 6:
            exit()

        else:
            print("Invalid Input !!!")
            input()
    except Exception:
        print("There is a Problem, input must be integer")
        input("Click enter to next")

    