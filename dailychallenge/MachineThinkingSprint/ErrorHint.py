# ErrorHint
# Instructions

# Implement error_hint(error_type). Return a helpful debugging hint for common Python errors. 
# For NameError return Check variable names and spelling. For TypeError return Check the types before using an operator. 
# For ValueError return Check whether the value can be converted. For ZeroDivisionError return Check that the denominator is not zero. 
# For IndexError return Check the index is inside the valid range. For anything else return Read the traceback carefully.

def error_hint(error_type):
    if error_type == "NameError":
        return "Check variable names and spelling."

    if error_type == "TypeError":
        return "Check the types before using an operator."

    if error_type == "ValueError":
        return "Check whether the value can be converted."

    if error_type == "ZeroDivisionError":
        return "Check that the denominator is not zero."

    if error_type == "IndexError":
        return "Check the index is inside the valid range."

    return "Read the traceback carefully."