
import json

def load_borrow():
    try:
        with open("borrow_records.json", "r") as file:
            borrow_list = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

    else:

        return borrow_list


def save_borrow(borrow_list):
        with open("borrow_records.json", "w") as file:
            json.dump(borrow_list, file, indent=3)



def load_fellows():
    try:
        with open("fellows.json", "r") as file:
            fellows_list = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

    else:

        return fellows_list


def load_resources():
    try:
        with open("resources.json", "r") as file:
            resources = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

    else:

        return resources


def save_resources(resources):
        with open("resources.json", "w") as file:
            json.dump(resources, file, indent=3)

