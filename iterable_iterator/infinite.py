class OrderStream:
    def __init__(self, orders):
        self.orders = orders
        self.index = 0

    def __iter__(self):
        return self

    
    def __next__(self):
        order = self.orders[self.index]

        self.index +=1

        if self.index == len(self.orders):
            self.index = 0

        return order


orders = OrderStream(['Latte', 'Mocha', 'Cappuccino'])
for order in orders:
    print(f"Processing: {order}")
