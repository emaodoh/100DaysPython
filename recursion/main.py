n = 6

# Print numbers from n down to 1
def count_num(number):
    if number == 0:
        print("done and dusted")
        return
    
    print(number)
    
    count_num(number-1)


# Print numbers from 1 to n
def count_down(number):
    if number == 0:
        return

    count_down(number - 1)
    print(number)    


count_down(n)
count_num(n)