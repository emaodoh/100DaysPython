# Instructions

# Implement score_summary(name, a, b, c). Convert the three score values to numbers. 
# If conversion fails, return Invalid score. If any score is below 0 or above 100, return Invalid score. 
# Otherwise calculate the average, round it to 2 decimal places, choose a grade, and return a three-line report with labels Student, Average, and Grade. 
# Grade is A for 90 and above, B for 80 and above, C for 70 and above, and F below 70.

def score_summary(name, a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)

    except ValueError:
        return "Invalid score"

    if a > 100 or a < 0 or b <  0 or b > 100 or c < 0 or c > 100:
        return "Invalid score"
    
    average = (a + b + c) / 3

    grade = ""
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "F"

    return f"Student: {name}\nAverage: {average}\nGrade: {grade}"
