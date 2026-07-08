def calculator():
    print("Enter q to stop\n")

    while True:

        num1 = input("Enter the first number: ").strip()
        try:
            num1 = float(num1)
        except ValueError:
            print("That was not a valid number!")
            continue
        if num1 == "q":
            return "Goodbye"
        num2 = input("Enter the second number: ").strip()
        try:
            num2 = float(num2)
        except ValueError:
            print("That was not a valid number!")
            continue
        if num2 == "q":
            return "Goodbye"

        opt = input("Enter the operation(option +,/,- and *): ").strip()
        if  opt == "q":
            return "Goodbye"

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("That was not a valid number!")
            continue

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


result = calculator()
print(result)