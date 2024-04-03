from abc import ABC, abstractmethod


class BaseDiver(ABC):

    def __init__(self, name, oxygen_level):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self._competition_points = 0
        self.has_health_issues = False

    @property
    def competition_points(self):
        return round(self._competition_points, 1)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch):
        ...

    @abstractmethod
    def renew_oxy(self):
        ...

    def hit(self, fish):
        if self.oxygen_level > fish.time_to_catch:
            self.catch.append(fish)
            self._competition_points += fish.points
            self.oxygen_level -= fish.time_to_catch
            return

        self.oxygen_level = 0
        self.has_health_issues = True

    def update_health_status(self):
        self.has_health_issues = True if not self.has_health_issues else False

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"
