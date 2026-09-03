import json
import expense
                
def save_expenses(expense_object: list[Expense]) -> None:

    """svae expense to a file"""

    expenses = []
    
    for expense in expense_object:
        
        
        expenses.append(expense.to_dict())

    with open("expenses.json", "w") as data:
        json.dump(expenses, data, indent=3)


def load_expenses() -> list[object]:

    """load expense from a file"""

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        
                
        expense_object = []

        for expense1 in expenses:
            
  
            expense_obj = expense.Expense(expense1["category"], expense1["item"], expense1["date"], expense1["price"])

            expense_object.append(expense_obj)
        
        return expense_object

    except (FileNotFoundError, json.JSONDecodeError):
        return []