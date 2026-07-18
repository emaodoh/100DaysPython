import helpers
import json


try:

    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    expenses = []
def tracker():
   
    
    
        
    print("select from this features to start")
    while True:
        operation = input("\n 1.Add expense \n 2.View all expenses \n 3.Delete expense \n 4.calculate total spending \n 5.Filter by category \n 6.Exist:  ").strip()

        try:
            operation = int(operation)
        except ValueError:
            print("\n \033[31m---------select the number of the operation to start eg Add == 1 ---------\033[0m\n")
            continue

        match operation:
            case 1:
                helpers.add_expense(expenses)
            case 2:
                helpers.view_expenses(expenses)
            case 3:   
                helpers.delete_expenses(expenses)
            case 4:
                helpers.total_expenses(expenses)
            case 5:
                helpers.filter_expenses(expenses)
            case 6:
                break
    print("Goodbye")


tracker()