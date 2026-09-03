class Expenses:
    def __init__(self, category, item, date, price):
        self.category = category
        self.item = item
        self.date = date
        self.price = price
  
    def to_dict(self):
        return {
                "category": self.category,
                "item": self.item,
                "date": self.date,
                "price": self.price
                }