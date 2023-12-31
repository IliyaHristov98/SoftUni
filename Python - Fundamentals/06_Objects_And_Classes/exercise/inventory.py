class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, items: str):
        if len(self.items) < self.__capacity:
            self.items.append(items)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.get_capacity() - len(self.items)}"
