class Expense:
    def __init__(self, category, item, date, price):
        self.category = category
        self.item = item
        self.date = date
        self.price = price

    def __repr__(self):
        return (
            f"Expense(category={self.category!r}, "
            f"item={self.item!r}, "
            f"date={self.date!r}, "
            f"price={self.price!r})"
        )

    def __str__(self):
        return (
            f"Category: {self.category} | "
            f"Item: {self.item} | "
            f"Date: {self.date} | "
            f"Price: ₦{self.price}"
        )

    def __eq__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented

        return (
            self.category == other.category
            and self.item == other.item
            and self.date == other.date
            and self.price == other.price
        )

    def to_dict(self):
        return {
            "category": self.category,
            "item": self.item,
            "date": self.date,
            "price": self.price,
        }