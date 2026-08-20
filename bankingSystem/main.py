import json
import helpers

try:

    with open("accountDetails.json", "r") as file:
        accountDetails = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    accountDetails = []


print(" --------- \033[33m   welcome to chatgpt bank \033[0m --------------\n 1. Login account \n 2. Create account")
while True:
    operation = input().strip()
    if operation != "1" and operation != "2":
        print("Enter 1 to login or 2 to create account")
        continue
    else:
        break

match operation:
    case "1":
        helpers.log_in(accountDetails)
    case "2":
        helpers.Create_account(accountDetails)
        helpers.write_accountDetails(accountDetails)









