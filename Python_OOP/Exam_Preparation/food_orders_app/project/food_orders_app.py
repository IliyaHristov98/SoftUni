from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class FoodOrdersApp:
    MEALS = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.bills = 0

    def register_client(self, client_phone_number: str):
        try:
            next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
            raise Exception("The client has already been registered!")
        except StopIteration:
            self.clients_list.append(Client(client_phone_number))
            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in self.MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = []
        for meal in self.menu:
            result.append(meal.details())

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for name, quantity in meal_names_and_quantities.items():
            try:
                meal = next(filter(lambda m: m.name == name, self.menu))
                if meal.quantity < quantity:
                    raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")
            except StopIteration:
                raise Exception(f"{name} is not on the menu!")

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        for name, quantity in meal_names_and_quantities.items():
            meal = next(filter(lambda m: m.name == name, self.menu))
            client.shopping_cart.append(self.MEALS[meal.__class__.__name__](meal.name, meal.price, quantity))
            meal.quantity -= quantity
            client.ordered_items.append(meal.name)
            client.bill += quantity * meal.price

        return f"Client {client.phone_number} successfully ordered {', '.join(client.ordered_items)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            menu_item = next(filter(lambda m: m.name == meal.name, self.menu))
            menu_item.quantity += meal.quantity

        client.shopping_cart = []
        client.bill = 0
        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.bills += 1
        bill = client.bill
        client.bill = 0
        client.shopping_cart = []
        return f"Receipt #{self.bills} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
