items = []
prices = []
total = 0

while True:
    item = input("Enter a item (click q to stop): ")
    if item.lower() == "q":
        break
    else:
        price = input(f"{item} how much: ")
        try:
            price = float(price)
        except ValueError:
            print("\nEnter a valid number\n")
            continue
        items.append(item)
        prices.append(price)
for item in items:
        print(f"item =  {item}",end=" ") 
for price in prices:
    total += price
    print()
print(f"Total amount is {total}")