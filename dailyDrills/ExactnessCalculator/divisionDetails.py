# Instructions

# Implement division_details(a, b). Return a dictionary with three keys: "true_division", "floor_division", and "remainder". 
# true_division should be a / b rounded to 2 decimal places. floor_division should be a // b. remainder should be a % b.

def division_details(a, b):
    true_division = round(a/b, 2)
    floor_division = a // b
    remainder = a % b

    return {"true_division":true_division, "floor_division": floor_division, "remainder": remainder}
