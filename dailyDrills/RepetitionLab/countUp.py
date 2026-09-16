# Instructions

# Implement count_up(n). Return a list of numbers from 1 to n inclusive. 
# If n is less than 1, return an empty list. Use a loop and range.


def count_up(n):
    if n < 1:
        return []

    number = []
    for num in range(1,n+1):
        number.append(num)

    return number