# Instructions

# Implement top_scorer(scores). The scores argument is a dictionary mapping student names to numeric scores. 
# Return the name of the student with the highest score. 
# If the dictionary is empty, return No scores. If there is a tie, return the name that comes first alphabetically.


def top_scorer(scores):
    if not scores:
        return "No scores"

    num = next(iter(scores.values()))
    
    for name, score in scores.items():
        if score > num:
            num = score
    

    names = []
    for name, score in scores.items():
        
        if num == score:

            names.append(name)
    names.sort()
  

    return names[0]
