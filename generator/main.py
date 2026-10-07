import sys

def get_orders_list(n):
    orders = []
    for i in range(n):
        orders.append(f"Order #{i}")
    return orders

# Generates 1,000,000 items in memory all at once
massive_list = get_orders_list(1000000)
print(f"Memory size: {sys.getsizeof(massive_list)} bytes")



def get_orders_generator(n):
    for i in range(n):
        yield f"Order #{i}"

# Instantly returns a generator object using almost zero memory
massive_gen = get_orders_generator(1000000)
print(f"Memory size: {sys.getsizeof(massive_gen)} bytes")



list_comp = [x * x for x in range(10000)]
gen_expr = (x * x for x in range(10000))
print("List comp size:", sys.getsizeof(list_comp), "bytes")
print("Gen expr size:", sys.getsizeof(gen_expr), "bytes")


# drinks = ['Coffee', 'Tea', 'Juice']
# order_id = 2  # 1 % 3 = 1

# # This evaluates to drinks[1]
# drink = drinks[order_id % len(drinks)]

# print(drink)  # Output: Tea
