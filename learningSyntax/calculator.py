def calculator():
    print("Enter q to stop")

    while True:
        num1 = input("Enter the first number: ")
        if num1 == "q":
            return "Goodbye"
        num2 = input("Enter the second number: ")
        if num2 == "q":
            return "Goodbye"
        
        opt = input("Enter the operation(option +,/,- and *): ")
        if  opt == "q":
            return "Goodbye"
            
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            if opt == "+":
                result = num1 + num2
            elif opt == "-":
                result = num1 - num2
            elif opt == "/":
                if int(num2) == 0:
                     print("Error: You cannot divide by zero!\n")
                     continue
                else:
                    result = num1 / num2
            elif opt == "*":
                result = num1 * num2
            else:
                print ("invalid opration")
                continue
            return result
        print ("invalid input:  enter a valid number")


result = calculator()
print(result)