

def validate_num() -> int:
    """ validate input (numbers) from user"""
    
    while True:
        try:
            number = int (input(">").strip())
        
        except ValueError:
            print("invalid number")
            continue

        else:
            return number
