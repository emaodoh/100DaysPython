
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
        if option == 2:
            num = 0
            print("\n-----------List of task-----------\n")
            for task in book:
                num +=1
                
                print(f"{num}.{task}")
        if option == 3:
            taskNum = input("number of task to remove: ")

            try:
                taskNum = int(taskNum)

            except ValueError:
                print("Enter the number of task to remove")
                continue

            if taskNum != 0:
                taskNum -=1

            if taskNum > len(book) or taskNum < 0:
                print("No task with that number. View tasks and try again")
                continue

            del book[taskNum:taskNum+1]
            print("\nTask deleted successfully\n")

        if option == 4:
            break

    return "Goodbye"
        

result = todo()

print(result)