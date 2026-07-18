
import json
def add_expense(expenses):
    

    while True:
        expCategory = input("Enter the category of the expense:  ").strip().lower()
        expDate = input("Enter the date:  ").strip()
        expItem = input("Enter the item:  ").lower().strip()        
        if not expCategory or not expDate or not expItem:
            print("\n\033[31m[Error] Category, Date, and Item cannot be empty!\033[0m\n")
            continue
            
        
        try:
            expPrice = int(input("Enter price:  "))
            break
        except ValueError:
            print("\n \033[31m Enter only number\033[0m \n")
            continue
                    
    expenses.append({"category":expCategory,"item":expItem, "price":expPrice, "date":expDate})
    write_expenses(expenses)

def view_expenses(expenses):
    if not expenses:
        print("\n \033[31m Empty: No expense recorded \033[0m \n")
        return
    print("\n------ Expenses ------")    
    index =0        
    for expense in expenses:
        index+=1
        print(f"{index}.{expense["category"]}----{expense["item"]}----${expense["price"]}----{expense["date"]}")
        print()

def delete_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    while True:
        view_expenses(expenses)
        try:
            expdel = int(input("Enter number to delete: "))
        except ValueError:
            print("\n \033[31m Enter only the number of the list \033[0m \n")
            continue
                        
        if expdel >= 1 and expdel <= len(expenses):
            expdel -=1
            del expenses[expdel]
            print("\n \033[32m---expenses is deleted successfully---\033[0m  \n")
            write_expenses(expenses)

            break
        else:
            print("\n \033[31m ----invalid index\033[0m ----\n")
            continue

def total_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    amount = 0
    for expense in expenses:
        amount += expense["price"]
    print(f"\n Total expenses is: {amount}") 

def filter_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    expCategory = input("Enter category to filter:  ").strip().lower()
    index = 0
    found = False
    for expense in expenses:
        if expense["category"] == expCategory:
            found = True
            index += 1
            print(f"{index}.Item = {expense["item"]}-----price = {expense["price"]}-----Date = {expense["date"]}")
    if not found:
        print("\n \033[31m The category you entered is not in recorded\033[0m \n")
                    
def write_expenses(expenses):
    with open("expenses.json", "w") as data:
        json.dump(expenses, data, indent=3)