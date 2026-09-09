# PasswordStrength
# Tests passed ✓
# Next challenge
# Instructions

# Implement password_strength(password). Return Weak if the password has fewer than 8 characters. Return Medium if it has at least 8 characters but does not contain both letters and digits. Return Strong if it has at least 8 characters and contains at least one letter and at least one digit. Students may need to research isalpha and isdigit.


def password_strength(password):
    if len(password) < 8:
        return "Weak"

    letter = False
    digit = False

    if len(password) >= 8:
        for letters in password:
            if letters.isdigit():
                digit = True
            if letters.isalpha():
                letter = True
            
        if  letter == True and digit == True:
            return "Strong"
        else:
            return "Medium"

    
result = password_strength("lllllllllllllll")

print(result)
