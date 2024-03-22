from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    MACHINES = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop,
    }

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.MACHINES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        machine = self.MACHINES[type_computer](manufacturer, model)
        result = machine.configure_computer(processor, ram)
        self.warehouse.append(machine)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for machine in self.warehouse:
            if machine.price <= client_budget \
                    and machine.processor == wanted_processor \
                    and machine.ram >= wanted_ram:

                self.profits += client_budget - machine.price
                self.warehouse.remove(machine)
                return f"{machine} sold for {client_budget}$."

        raise Exception(f"Sorry, we don't have a computer for you.")
