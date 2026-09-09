# ReceiptFormatter

# Instructions

# Implement receipt_formatter(name, quantity, price). Calculate subtotal as quantity multiplied by price. Calculate tax as 7.5 percent of subtotal. Calculate total as subtotal plus tax. Return a four-line report with labels Customer, Subtotal, Tax, and Total. Round subtotal, tax, and total to 2 decimal places.

def receipt_formatter(name, quantity, price):
    subtotal = quantity * price
    tax = (7.5/100) * subtotal
    total = subtotal + tax

    return f"Customer: {name}\nSubtotal: {subtotal:.1f}\nTax: {round(tax, 2)}\nTotal: {round(total, 2)}"


result = receipt_formatter("john", 200, 7.5)

print(result)