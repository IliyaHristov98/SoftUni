from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy, name, price):
        try:
            c = next(filter(lambda d: d.name == name, self.delicacies))
            raise Exception(f"{name} already exists!")
        except StopIteration:
            pass

        if type_delicacy not in self.DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(self.DELICACIES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        try:
            b = next(filter(lambda b: b.booth_number == booth_number, self.booths))
            raise Exception(f"Booth number {booth_number} already exists!")
        except StopIteration:
            pass

        if type_booth not in self.BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(self.BOOTHS[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        try:
            booth = next(filter(lambda c: not c.is_reserved and c.capacity >= number_of_people, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number, delicacy_name):
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
