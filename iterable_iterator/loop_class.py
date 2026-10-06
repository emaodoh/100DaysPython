class OrderStream:
    def __init__(self, orders):
        self.orders = orders
        self.next = 0

    def __iter__(self):
        return self

    
    def __next__(self):

        if self.next < len(self.orders):

            order = self.orders[self.next]
            self.next += 1

            return order

        else:
            raise StopIteration



orders = OrderStream(['Latte', 'Mocha', 'Cappuccino'])
for order in orders:
    print(f"Processing: {order}")



