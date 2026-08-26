import json



def log_in(accountDetails: list[dict]) -> dict:
    
    """ log in to a already existing account"""

    MaxlogInAttempt = 5
    
    
    while True:

        userName = input("Enter userName:  ").strip()

        if not userName:
            print("pleass enter your user name")
            continue

        accountPin = input("Enter your 4 digit pin: ").strip()
        if len(accountPin) != 4:
            print("pin can not be greater than or less then 4")
            continue
            
        try:
            accountPin = int(accountPin)
        except:
            print("\n \033[33m pleass enter your 4 digit pin \033[0m \n")
            continue
        for accountInfor in accountDetails:
            if accountPin == accountInfor["accountPin"] and userName == accountInfor["userName"]:
                print("\n \033[33m loged in successful \033[0m \n")
                return True, accountInfor
                
            
        MaxlogInAttempt -=1
        print(f"\n \033[31m Invalid details you have {MaxlogInAttempt} attempt left \033[0m \n")
        

        if MaxlogInAttempt == 0:
            print("\n \033[31m Your account have been blocked \033[0m")
            return False



def Create_account(accountDetails: list[dict]) -> None:

    """create a new account """
    

    while True:
        
        accountName = input("Enter your name:  ").strip().lower()

        if not accountName:
            print("Pleass enter your account name")
            continue

        accountNumber = input("Enter your phone number:  ").strip().lower()
            
        if len(accountNumber) != 11 and len(accountNumber) != 10:
            print("\n \033[31m Invalid account number (enter your phone number) \033[0m \n ")
            continue
        if len(accountNumber) == 11:
                accountNumber = accountNumber[:0] + accountNumber[1:]
            
        try:
            accountNumber = int(accountNumber)
            
        except ValueError:
            print("Account most be a number")
            continue
        else:
                
            break


    while True:
        accountPin = input("Enter 4 digit pin:  ").strip()
        if len(accountPin) != 4:
            print("\n \033[31m pin can not be less than or greater than 4 \033[0m \n")
            continue
                
        try:
            accountPin = int(accountPin)

        except ValueError:
            print("\n \033[31m pin most be a number \033[0m \n")
            continue
        else:
            remove_space_from_name = accountName.replace(" ", "")
            if len(remove_space_from_name) > 6:
                userName = remove_space_from_name[0:6]
            else:
                userName = accountName

            accountDetails.append({"accountName": accountName, "accountPin": accountPin, "accountNumber": accountNumber, "userName": userName, "balance": 0})
            print(f"Your account have been created sucessfully \n Your username: {userName}")
                

            break



