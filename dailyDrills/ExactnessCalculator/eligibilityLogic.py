# Instructions

# Implement eligibility_logic(score, attendance, completed_drill). 
# Return "Eligible" only when score is greater than or equal to 70, attendance is greater than or equal to 80, and completed_drill is True. 
# Otherwise return "Not eligible".

def eligibility_logic(score, attendance, completed_drill):
    if score >= 70 and attendance >= 80 and completed_drill == True:
        return "Eligible"

    return "Not eligible"
