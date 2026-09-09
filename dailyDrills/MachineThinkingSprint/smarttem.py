# Instructions

# Implement smart_temperature(value). Convert value to a Celsius number. 
# If conversion fails, return Invalid temperature. Convert Celsius to Fahrenheit using the standard formula. 
# Return a three-line report with labels Celsius, Fahrenheit, and Status. Status is freezing when Celsius is less than or equal to 0, cold when below 20, warm when from 20 through 30, and hot when above 30.

def smart_temperature(value):
    try:
        celsius = float(value)
    except ValueError:
        return "Invalid temperature"
    status = ""

    if celsius <= 0:
        status = "freezing"

    elif celsius < 20:
        status = "cold"
    elif celsius in range(20,31):
        status = "warm"
    else:
        status = "hot" 

    fahrenheit = (celsius * 1.8) +32

    return f"Celsius: {celsius}\nFahrenheit: {fahrenheit}\nStatus: {status}"

