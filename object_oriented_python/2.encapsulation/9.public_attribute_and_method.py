class StoreItem:
    # (1/14/25)(1104-1109pm)(Tue)
    def __init__(self, name: str, price: int):
        # Add: name, price
        self.name = name
        self.price = price

chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them
print(chips.name)
print(chips.price)

