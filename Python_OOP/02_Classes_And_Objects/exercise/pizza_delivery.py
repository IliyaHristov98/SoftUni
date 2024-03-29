class PizzaDelivery:

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return self.already_ordered()

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return self.already_ordered()

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with " \
               f"{', '.join([f'{ingredient}: {quantity}' for ingredient, quantity in self.ingredients.items()])} " \
               f"and the price will be {self.price}lv."

    def already_ordered(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"
