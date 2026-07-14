
import time



def add(book):
    contactName = input("Enter name:  ").strip()
    if contactName in book:
        print("contact already exist")
        question = input("Contact exists. Update it? (y/n):  ").strip().lower()

        if question != "n" and question != "y":
            print("invalid input")
        if question == "n":
            return 
    contactNum = input("Enter number:  ").strip()
    if contactNum.isdigit():
        book[contactName] =  contactNum
        print("-----contact have been added successfully----")                
    else:
        print("--------contact most be a number--------")

def search(book):
    contactName = input("Enter contact name to search:  ")
    if contactName in book:            
            number = book[contactName]
            print(number)
    else:
        question = input("Contact does not exists. Add it? (y/n):  ").strip().lower()
        if question != "n" and question != "y":
            print("invalid input")

        elif question == "y":
            contactNum = input("Enter number:  ")
            if contactNum.isdigit():
                book[contactName] = contactNum
                print("contact have been added successfully")
            else:
                print("\n--------contact most be a number-------")


def update(book):
    contactName = input("Enter contact name to update:  ")
    if contactName in book:
            
        contactNum = input("Enter number:  ")
        if contactNum.isdigit():
            book[contactName] = contactNum
            print("contact have been updated successfully")
        else:
            print("\n-------contact most be a number-------")
    else:
        print("contact does not exist enter 1 to add")


def delete(book):
    contactName = input("Enter contact name:  ")
    if contactName in book:
            
        del book[contactName]
        print("contact have been delected successfully")
    else:
        print("contact does not exist enter 1 to add")


def view(book):
    print("---------List of contacts--------")
    for keys,values in book.items():
        time.sleep(0.5)
        print(f"Name: {keys} Number: {values}")