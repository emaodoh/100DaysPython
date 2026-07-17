
def tracker():
    book = [
        {
            "category":"food",
            "item": "rice",
            "price": 12,
            "date":"17/07/2026",
        },

        {
            "category":"rent",
            "item":"monthly rent",
            "price": 30000,
            "date":"17/07/2026",
        },
        {
            "category":"rent",
            "item":"monthly rent",
            "price": 40000,
            "date":"17/07/2026",
        }
    ]
    print("select from this features to start")
    while True:
        operation = input("\n 1.Add expense \n 2.View all expenses \n 3.Delete expense \n 3.calculate total spending \n 4.Filter by category \n 5.Monthly summary \n 6.Exist:  ").strip()

        try:
            operation = int(operation)
        except ValueError:
            print("---------select the number of the operation to start eg Add == 1 ---------")
            continue

        match operation:
            case 1:
                expCategory = input("Enter the category of the expense:  ")
                try:
                    expPrice = int(input("Enter price:  "))
                except ValueError:
                    print("Enter only number")
                    continue
                expDate = input("Enter the date:  ")
                expItem = input("Enter the item:  ")
                
                book.append({"category":expCategory,"item":expItem, "price":expPrice, "date":expDate})
            case 2:
                print()
                index =0        
                for itm in book:
                    index+=1
                    print(f"{index}.{itm["category"]}----{itm["item"]}----${itm["price"]}----{itm["date"]}")
                print()
            case 3:        
                index =0        
                for itm in book:
                    index+=1
                    print(f"{index}.{itm["category"]}----{itm["item"]}----${itm["price"]}----{itm["date"]}")

                try:

                    expdel = int(input("Enter number to delete: "))

                except:
                    print("Enter only the number of the list")
                    continue
                
                if expdel >= 1 and expdel <= len(book):
                    expdel -=1
                    del book[expdel]
                    print("\n \033[32m---expenses is deleted successfully---\033[0m  \n")
                else:
                    print("\n \033[31m ----invalid index\033[0m ----\n")

            case 6:
                break


    

    # for itm in book:
    #     for key,value in itm.items():
    #         print(key)

tracker()