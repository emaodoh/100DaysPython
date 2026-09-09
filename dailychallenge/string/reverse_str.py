# Instructions

# Implement reverse_string(value) without using slicing shorthand like [::-1]. Return a new string containing the input characters in reverse order.

def reverse(value):
    new_word = ""
    x = len(value)
    while True:
        if x > 0:
            x-=1
            new_word += value[x]
        else:
            break
    
    print(new_word)
reverse("python is fun")