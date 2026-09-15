# Instructions

# Implement safe_calculator(a, operator, b). Return the result of applying the operator to the two numbers. 
# Supported operators are "+", "-", "*", "/", "%", and "**". If the operator is unknown, return "Invalid operator". 
# If the operator is "/" or "%" and b is 0, return "Cannot divide by zero". Round division results to 2 decimal places.

def safe_calculator(a, operator, b):
    a = float(a)
    b = float(b)
    if operator not in ["+", "-", "*", "/", "%", "**"]:
        return "Invalid operator"

    if b == 0 and (operator == "/" or operator == "%"):
        return "Cannot divide by zero"

    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a *b
        case "/":
            return round(a/b, 2)
        case "%":
            return a%b
        case "**":
            return a ** b
