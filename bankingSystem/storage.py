import json


def save_accountDetails(accountDetails: list[dict]):
    """ save account details to json file"""
    
    with open("accountDetails.json", "w") as data:
        json.dump(accountDetails, data, indent=3)


def load_accountDatails() -> list:
    """ load account details from json file"""
        
    try:

        with open("accountDetails.json", "r") as file:
            accountDetails = json.load(file)
            
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    else:
        return accountDetails
