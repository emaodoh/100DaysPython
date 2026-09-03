

import storage
import validate
import expense


  



def add_expense(expense_object: list[Expense]) -> None:
    """add expenses to the a file"""
    

    while True:
            
        expense_category = input("Enter the category of the expense:  ").strip().lower()
        expense_item = input("Enter the item:  ").lower().strip()
        if not expense_category or not expense_item:
            print("\n\033[31m[Error] Category and Item cannot be empty!\033[0m\n")
            continue
        break
    expense_date = validate.validate_date()
        
    expense_price = validate.validate_price()

        
             
    expense = expense.Expense(expense_category,expense_item,str(expense_date),expense_price)
    expense_object.append(expense)
    storage.save_expenses(expense_object)

def view_expenses(expense_object: list[Expense]) -> None:
    """view all expense """
    if not validate.has_expenses(expense_object):
        return
    print("\n-----------------------------------------------------------------------")    
    index =0        
    
    for expense in expense_object:

        index+=1

        print(f"{index}.{expense.category}   {expense.item}   ${expense.price}   {expense.date}")
        print("---------------------------------------------------------------------")

def delete_expenses(expenses: list[Expense]) -> None:
    """delete existing expense by index""" 

    if not validate.has_expenses(expenses):
        return

    view_expenses(expenses)

    delete_index = validate.validate_index(expenses)                    
    if delete_index >= 1 and delete_index <= len(expenses):
        delete_index -=1
        question = input("are you sure you want to delete (y/n)").lower().strip()
        if question == "y" or question == "yes":
            del expenses[delete_index]
            print("\n \033[32m---expenses is deleted successfully---\033[0m  \n")
            storage.save_expenses(expenses)
        
    
    else:
        print("\n \033[31m ----invalid index\033[0m ---- \n")
        

def total_expenses(expenses: list[Expense]) -> None:
    """sum of all expenses recoded"""

    if not validate.has_expenses(expenses):
        return
        

    amount = 0
    for expense in expenses:
        amount += expense.price
    print(f"\n Total expenses is: {amount}") 

def filter_expenses(expenses: list[Expense]) -> None:
    """filter expenses to display by category"""

    if not validate.has_expenses(expenses):
        return

    expense_category = input("Enter category to filter:  ").strip().lower()
    index = 0
    found = False
    for expense in expenses:
        if expense.category == expense_category:
            found = True
            index += 1
            print(f"\033[34m{index}.Item: {expense.item}      price:  {expense.price}     Date: {expense.date}\033[0m")
    if not found:
        print("\n \033[31m The category you entered is not  recorded\033[0m \n")
 
def edit_expenses(expenses: list[Expense]) -> None:
    """edit existing expenses by index"""
    
    if not validate.has_expenses(expenses):
        return
        
    view_expenses(expenses)

    num = validate.validate_index(expenses)

    num -=1
    print(f"\n current category: {expenses[num].category}")
    newCategory = input("new category (press enter to skip): ").strip().lower()

    if newCategory:
        expenses[num].category = newCategory
    print(f"\n current item: {expenses[num].item}")
    newItem = input("new Item (press enter to skip):  ").strip().lower()
    if newItem:
        expenses[num].item = newItem
    


    new_Price = validate.validate_new_price(expenses, num)

    expenses[num].price = new_Price
    print(f"\n current date: {expenses[num].date}")
    new_Date = validate.validate_date()

                   
    expenses[num].date = new_Date

    print("\n \033[32mExpense updated successfully!\033[0m\n")
    storage.save_expenses(expenses)


def search_by_item(expenses: list[Expense]) -> None:
    """search through expenses by item"""

    if not validate.has_expenses(expenses):
        return
    item = input("Enter item: ").strip().lower()
    found = False
    for expense in expenses:
        if item in expense.item:
            found = True
            print("-" * 30)
            print(f"{expense.item}: {expense.price}")
            print("-" * 30)
    if not found:
        print("\n \033[31m Item not found \033[0m \n")


def search_by_date(expenses: list[Expense]) -> None:
    """search through expenses with date"""

    
    date = validate.validate_date()
    found = False
    for expense in expenses:
        if expense.date == date:
            found = True
            print(f"{expense.item}: {expense.price}")
    if not found:
        print("\n \033[31m Date not found \033[0m \n")



