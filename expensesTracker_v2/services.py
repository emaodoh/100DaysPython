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