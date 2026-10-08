from services import check_fellow_id, check_resource_id, update_borrow_list, check_borrowed_infor, search_by_name, generate_general_report, add_resource

def add_resources():

    category = input("Enter category: ").strip()
    name = input("Enter Item: ").strip()
    resource_id = input("Enter ID: ")
    total = input("Total number: ")

    if category and name and resource_id and total:
        add_resource(resource_id, name, category, total)
        return "Resource added successfully!"

    return "Invalid input please follow the prompt"

def borrow():
    fellow_id = input("Fellows ID: ").strip()
    resource_id = input("Enter resource ID: ").strip()
    while True:
        try:
            resource_quantity = int(input("Enter quatity: "))
            if resource_quantity > 0:
                break

        except ValueError:
            print("Enter a valid number")


    fellow = check_fellow_id(fellow_id)
    resource = check_resource_id(resource_id)
    if fellow and resource:
        reponse = update_borrow_list(fellow_id, resource, resource_quantity)

        return reponse

    else:
        return "invalid ID"
    
def return_item():
    fellow_id = input("Fellows ID: ").strip()
    resource_name = input("Resource Name: ").strip().lower()

    if fellow_id and resource_name:
        reponse = check_borrowed_infor(fellow_id, resource_name)

    else:
        return "Invalid input"

    return reponse

def search_category():
    name = input("Name of item: ").strip().lower()

    reponse = search_by_name(name)

    return reponse


def general_report():
    overall_unit, available, borrowed = generate_general_report()

    return f"overall units: {overall_unit}, Available unit: {available}, Borrowed: {borrowed}"




def menu():
    while True:
        print("\n===== Resource Management System =====")
        print("1. Borrow Resource")
        print("2. Return Resource")
        print("3. Search Resource")
        print("4. General Report")
        print("5. Add Resource")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(borrow())

        elif choice == "2":
            print(return_item())

        elif choice == "3":
            print(search_category())

        elif choice == "4":
            print(general_report())

        elif choice == "5":
            print(add_resources())

        elif choice == "6":
            print("Goodbye!")
            break


        else:
            print("Invalid choice. Please select between 1 and 5.")

menu()



