
import services
import login_create_acc
import validate
import storage

accountDetails = storage.load_accountDatails()


print(" --------- \033[33m   welcome to chatgpt bank \033[0m --------------\n 1. Login account \n 2. Create account")
while True:
    operation = validate.validate_num()

    if operation in (1,2):
        break
    else:
        print("pleass select from 1 and 2")
        continue

match operation:
    case 1:
        loged_in, accountInfor = login_create_acc.log_in(accountDetails)
        if loged_in:
            print("1 deposite \n2 withdraw \n3 show balance")
            
            while True:
                service = validate.validate_num()


                if service in (1,2,3):
                    break
                else:
                    print("pleass select from 1-3")
                    continue
            bank_services = services.BankServices(accountInfor["balance"])
            match service:
                case 1:

                    print("Enter amount to deposite")
                    
                        
                    amount = validate.validate_num()

                    
                    bank_services.deposite(amount)
                    print(bank_services.show_balance())

                    accountInfor["balance"] = bank_services.balance
                    storage.save_accountDetails(accountDetails)
                    
                case 2:
                    print("Enter amount to withdral")

                    amount = validate.validate_num()

                    bank_services.withdraw(amount)

                    print(bank_services.show_balance())

                    accountInfor["balance"] = bank_services.balance
                    storage.save_accountDetails(accountDetails)
                    
                case 3:
                    print(bank_services.show_balance())
    case 2:
        login_create_acc.Create_account(accountDetails)
        storage.save_accountDetails(accountDetails)









