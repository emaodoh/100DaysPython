import services
import json

import storage




expenses = storage.load_expenses()


def tracker():
    
    
    print("select from this features to start")
    while True:
        operation = input("\n 1.Add expense \n 2.View all expenses \n 3.Delete expense \n 4.calculate total spending \n 5.Filter by category \n 6.Edit an Expenses \n 7.search by item \n 8.search by date \n 0.Exist:  ").strip()

        try:
            operation = int(operation)
        except ValueError:
            print("\n \033[31m---------select the number of the operation to start eg Add == 1 ---------\033[0m\n")
            continue

        match operation:
            case 1:
                services.add_expense(expenses)
            case 2:
                services.view_expenses(expenses)
            case 3:   
                services.delete_expenses(expenses)
            case 4:
                services.total_expenses(expenses)
            case 5:
                services.filter_expenses(expenses)
            case 6:
                services.edit_expenses(expenses)
            case 7:
                services.search_by_item(expenses)
            case 8:
                services.search_by_date(expenses)
            case 0:
                break
    print("Goodbye")


tracker()