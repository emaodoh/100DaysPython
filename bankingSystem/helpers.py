import json

def log_in(accountDetails):
    logInAttempt = 5
    logedIn = False
    userName = input("Enter userName:  ").strip()
    while True:
        accountPin = input("Enter your 4 digit pin: ").strip()
        if len(accountPin) != 4:
            print("pin can not be greater than or less then 4")
            continue
            
        try:
            accountPin = int(accountPin)
        except:
            print("\n \033[33m pleass enter your 4 digit pin \033[0m \n")
            continue
        for accounts in accountDetails:
            if accountPin == accounts["accountPin"] and userName == accounts["userName"]:
                print("\n \033[33m loged in successful \033[0m \n")
                return logedIn
                break
        if not logedIn:
            logInAttempt -=1
            print(f"\n \033[31m Invalid details you have {logInAttempt} attempt left \033[0m \n")

        if logInAttempt == 0:
            print("\n \033[31m Your account have been blocked \033[0m")
            return False



def Create_account(accountDetails):
    accountName = input("Enter your name:  ").strip().lower()

    while True:
            
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
            accountName.replace(" ", "")
            if len(accountName) > 6:
                userName = accountName[0:6]
            else:
                userName = accountName

            accountDetails.append({"accountName": accountName, "accountPin": accountPin, "accountNumber": accountNumber, "userName": userName})
            print(f"Your account have been created sucessfully \n Your username: {userName}")
                

            break




def write_accountDetails(accountDetails):
    with open("accountDetails.json", "w") as data:
        json.dump(accountDetails, data, indent=3)

