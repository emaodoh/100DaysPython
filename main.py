def summarise_amounts(raw_values):
    total = 0
    rejected = 0
    for raw in raw_values:
        try:
            num = int(raw)
            if num < 0:
                rejected +=1
            else:
                total +=num
        except:
            rejected +=1
    return {"total": total, "rejected": rejected}


result  = summarise_amounts(["10", " 5 ", "bad", "-3", "0", ""])


assert result["rejected"] == 3, "rejected is not correct"
assert result["total"] == 15, "total is incorrect"

result = summarise_amounts([])

assert result["total"] == 0, 
assert result["rejected"] == 0

print(result)