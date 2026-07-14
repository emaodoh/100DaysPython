
import helpers

def contacts():
    book = {}
    print("\nselect an operation to start")

    while True:
        operation = input("\n1.Add contacts\n2.Search contact\n3.Update contact\n4.Delete Contact\n5.View Contact\n6.Exit:  ")

        try:
            operation = int(operation)
        except ValueError:
            print("\nEnter the number of operation eg Add contacts = 1")   
            continue    

        match operation:
            case 1:
                helpers.add(book)
           
            case 2:
                helpers.search(book)
            case 3:
                helpers.update(book)
            
            case 4:
                helpers.delete(book)
            
            case 5:
                helpers.view(book)
            case 6:
                break
            case _:
                 print("\n----------------number most be between 1 and 6----------------")
            

    return "Goodbye"


con = contacts()
print(con)