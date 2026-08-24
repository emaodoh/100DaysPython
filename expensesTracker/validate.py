from datetime import datetime,date

def has_expenses(expenses: list) -> bool:
    """check for empty expenses list"""
    if not expenses:
        print("\n \033[31m Empty: No expense recorded \033[0m \n")
        return False
    return True


def validate_date() -> datetime:
    """accept and validate user date """
    
    while True:
        expense_Date = input('Enter date "YYYY-MM-DD":  ').strip()
        try:
            expense_Date = datetime.strptime(expense_Date, "%Y-%m-%d").date()

            if expense_Date > date.today():
                print("futur date is not allowed")
                continue
            else:
                return str(expense_Date)

        except ValueError:
            print("invalide date pleass follow this formate YYYY-MM-DD")
            continue


def validate_price() -> float:
    """validate price of expenses from user"""

    while True:
        try:
            expense_Price = float ( input("Enter price:  ") )

        except ValueError:
            print("\n \033[31m Enter only number\033[0m \n")
            continue
        else:
            if expense_Price <= 0:
                print("Invalid input.\n Price must be a positive integer.")
                continue

        return expense_Price


def validate_index (expenses: list) -> int:

    while True:

        try:
            num = int(input().strip())

        except ValueError:
            print("pleass enter a number")
            continue
                    
        if len(expenses) >= num and num >0:
            return num
        else:
            print(" \033[31m pleass select a number of expenses to edit \033[0m ")
            continue

def validate_new_price(expenses: list, num: int) -> int:
                   
    while True:
        try:
            print(f"\n current price: {expenses[num]["price"]}")
            new_Price = input("new price (price enter to skip): ").strip()
            if new_Price == "":
                return expenses[num]["price"]
            else:
                new_Price = int (new_Price)
                        
                        
        except ValueError:
            print("\n \033[31m price most be a number \033[0m \n")
            continue
        else:
            if new_Price:
                return new_Price
