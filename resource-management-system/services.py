from storage import load_fellows, load_resources, load_borrow, save_borrow, save_resources

def check_fellow_id(fellow_id):
    fellows = load_fellows()

    if fellow_id in fellows:
        return fellows[fellow_id]

    
    return None



def check_resource_id(resource_id):
    resources = load_resources()


    for resource in resources:
        if resource["id"] == resource_id:
            return resource
           

    return None

def update_borrow_list(fellow_id, resource, resource_quantity):

    borrow_list = load_borrow()

    found = False
    if resource_quantity <= resource["available"]:
        

        for lists in borrow_list:

            if lists["name"] == resource["name"] and lists["fellow_id"] == fellow_id:
                found = True
            if found:    
                lists["quantity"] +=  resource_quantity
                save_borrow(borrow_list)
                break

        if not found:
            borrow_list.append({"fellow_id": fellow_id, "name": resource["name"], "quantity": resource_quantity})
            save_borrow(borrow_list)
            

        resources = load_resources()

        for resource_list in resources:
            if resource_list["id"] == resource["id"]:
                resource_list["available"] -= resource_quantity
                save_resources(resources)

                return f"successful: available {resource_list["name"]} unit = {resource_list["available"]}"

    return f"Not enough quantity, only {resource["available"]} left"


def check_borrowed_infor(fellow_id, resource_name):
    borrow_list = load_borrow()
    found = False
    for lists in borrow_list:
        if lists["fellow_id"] == fellow_id:
            if lists["name"].lower() == resource_name:
                found = True


        if found:

            print(f"Enter number of {lists["name"]} to return")
            num = int(input())

            if num > 0 and num <= lists["quantity"]:
                lists["quantity"] -= num
                if lists["quantity"] == 0:


                    new_list = [
                        item for item in borrow_list
                            if not (
                        item["fellow_id"] == fellow_id
                        and item["name"].lower() == resource_name
                        )
                        ]

                    save_borrow(new_list)
                    update_resource(resource_name, num)
                    return f"successful: you have 0 record now"
                    
                save_borrow(borrow_list)
                    
                update_resource(resource_name, num)

                return f"successful: you have {lists["quantity"]} left"

            return f"You borrowed {lists["quantity"]}"

    return f"Fellow with ID: {fellow_id} have not borrowed {resource_name}"


        





def update_resource(resource_name, num):
    resources = load_resources()

    for resource in resources:
        if resource["name"].lower() == resource_name:
            resource["available"] += num
            save_resources(resources)


def search_by_name(name):
    resources = load_resources()
    for resource in resources:
        if resource["name"].lower() == name:
            return f"Id: {resource["id"]}, Name: {resource["name"]}, Category: {resource["category"]} Total: {resource["total"]}, Available: {resource["available"]}"
        
        
    return f"Item with name {name} is not in record."

def generate_general_report():
    resources = load_resources()
    borrow_list = load_borrow()

    overall_unit = 0
    available = 0
    borrowed = 0

    for resource in resources:
        overall_unit += resource["total"]
        available += resource["available"]

    for lists in borrow_list:
        borrowed += lists["quantity"]


    return overall_unit, available, borrowed


def add_resource(resource_id, name, category, total):
    resources = load_resources()
    available = total

    resources.append({"id": resource_id, "name": name, "category": category, "total": total, "available": available})
    save_resources(resources)

