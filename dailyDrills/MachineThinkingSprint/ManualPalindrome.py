# Instructions

# Implement manual_palindrome(text). Ignore spaces and letter case.
#  Return true if the cleaned text reads the same forward and backward, otherwise return false. 
#  Do not use slicing shorthand or reversed. Students may need to research manual string reversal.

def manual_palindrome(text):
    text = text.lower().strip()

    text = text.replace(" ", "")
    
    rev_word = ""


    x = len(text)
    while True:
        if x > 0:
            x-=1
            rev_word += text[x]
        else:
            break

    if rev_word == text:
        return True

    return False
