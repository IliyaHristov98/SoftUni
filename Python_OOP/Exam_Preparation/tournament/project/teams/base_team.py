from abc import ABC, abstractmethod
from math import floor


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(f"Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if not len(value.strip()) >= 2:
            raise ValueError(f"Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError(f"Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        eq_price = 0
        avg_protection = 0
        if len(self.equipment) > 0:
            for eq in self.equipment:
                eq_price += eq.price
                avg_protection += eq.protection
            avg_protection = floor(avg_protection / len(self.equipment))

        return f"Name: {self.name}\n" \
               f"Country: {self.country}\n" \
               f"Advantage: {self.advantage} points\n" \
               f"Budget: {self.budget:.2f}EUR\n" \
               f"Wins: {self.wins}\n" \
               f"Total Equipment Price: {eq_price:.2f}\n" \
               f"Average Protection: {avg_protection}"
