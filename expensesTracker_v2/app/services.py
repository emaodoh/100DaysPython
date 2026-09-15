from . import storage
from . import models

expenses = storage.load_expenses()


def expense_statistics(expenses):

    if not expenses:
        return {
            "total": 0,
            "count": 0,
            "highest": 0
        }


    total = sum(expense.price for expense in expenses)

    count = len(expenses)

    highest = max(
        expense.price 
        for expense in expenses
    )


    return {
        "total": total,
        "count": count,
        "highest": highest
    }


def get_expense_by_id(id):
    for expense in expenses:

        if expense.new_id == id:
            return expense

    return None

def update_expense(expense, category, item, price, date):
    expense.item = item
    expense.price = price
    expense.category = category
    expense.date = date

    return storage.save_expenses(expenses)
        
def add_expense(new_id, category, item, date, price):
    user_expense = models.Expense(new_id, category, item, str(date), price)
    expenses.append(user_expense)
    storage.save_expenses(expenses)


def delete_expense(id):
    for expense in expenses:
        if expense.new_id == id:
            expenses.remove(expense)
            break
    storage.save_expenses(expenses)

