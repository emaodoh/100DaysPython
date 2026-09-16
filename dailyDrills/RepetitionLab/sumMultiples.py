# Instructions

# Implement sum_multiples(limit, divisor). Return the sum of all positive numbers from 1 to limit inclusive that are divisible by divisor. 
# If divisor is zero, return Invalid divisor. Do not use the built-in sum function.

def sum_multiples(limit, divisor):
    if divisor == 0:
        return "Invalid divisor"

    positive_num = 0

    for num in range(limit+1):
        if num%divisor == 0:
            positive_num += num

    return positive_num
        