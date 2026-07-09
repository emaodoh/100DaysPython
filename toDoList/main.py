
def todo():
    book = []
    while True:
        print("\n--------select one from the list of opration--------\n")
        option = input("1.Add task\n2.View tasks\n3.Remove task\n4.Exit: ")
        try:
            option = int(option)
        except ValueError:
            print("enter only the number of the task eg Add task = 1")
            continue
        if option == 1:
            task = input("Enter task:  ")
            book.append(task)
        elif option == 2:
            if not book:
                print("\nNo task available")
                continue
            num = 0
            print("\n-----------List of task-----------\n")
            for task in book:
                num +=1
                
                print(f"{num}.{task}")
        elif option == 3:
            taskNum = input("number of task to remove: ")

            try:
                taskNum = int(taskNum)
    # use except ValueError as e: to see the error message
            except ValueError :
                print(f"Enter the number of task to remove")
                continue

            if taskNum != 0:
                taskNum -=1

            if taskNum > len(book)-1 or taskNum < 0:
                print("No task with that number. View tasks and try again")
                continue

    # when deleting one item just enter the indix
            del book[taskNum]
            print("\nTask deleted successfully\n")

        elif option == 4:
            break
        else:
            print("\nInvalid input")

    return "Goodbye"
        

result = todo()

print(result)