import json
                
def save_expenses(expenses: list) -> None:
    """svae expense to a file"""
    with open("expenses.json", "w") as data:
        json.dump(expenses, data, indent=3)


def load_expenses() -> list:
    """load expense from a file"""
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            return expenses
    except (FileNotFoundError, json.JSONDecodeError):
        return []