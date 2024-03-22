from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200,
    }

    VALID_RAMS = {
        2: 1, 4: 2, 8: 3, 16: 4, 32: 5, 64: 6
    }

    MAX_RAM = 64

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram not in self.VALID_RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.PROCESSORS[processor] + (100 * self.VALID_RAMS[ram])
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
