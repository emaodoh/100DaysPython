# Next challenge
# Instructions

# Implement initials_badge(full_name). Remove leading 
# and trailing spaces, split the name into words, take the first character of each word, convert each initial to uppercase,
#  and return the initials joined with dots. 
# The returned badge should end with a dot.

def initials_badge(full_name):
    full_name = full_name.strip()

    split_word = full_name.split()
    result = ""
    for word in split_word:

        result += word[:1].upper() + "."

    return result