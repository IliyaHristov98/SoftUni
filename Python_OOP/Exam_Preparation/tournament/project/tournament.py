import re

from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    TEAM_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam,
    }

    EQ_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pattern = r'^[a-zA-Z0-9]+$'

        if not re.match(pattern, value):
            raise ValueError(f"Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type):
        if equipment_type not in self.EQ_TYPES:
            raise Exception("Invalid equipment type!")

        eq = self.EQ_TYPES[equipment_type]()
        self.equipment.append(eq)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPES:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        team = self.TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        eq = next(filter(lambda e: e.TYPE_ == equipment_type, self.equipment[::-1]))
        team = next(filter(lambda t: t.name == team_name, self.teams))

        if team.budget < eq.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(eq)
        team.equipment.append(eq)
        team.budget -= eq.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count = 0

        for eq in self.equipment:
            if eq.TYPE_ == equipment_type:
                eq.increase_price()
                count += 1

        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        t1 = next(filter(lambda x: x.name == team_name1, self.teams))
        t2 = next(filter(lambda y: y.name == team_name2, self.teams))

        if not t1.TYPE_ == t2.TYPE_:
            raise Exception("Game cannot start! Team types mismatch!")

        t1_total = t1.advantage + sum(eq.protection for eq in t1.equipment)
        t2_total = t2.advantage + sum(eq.protection for eq in t2.equipment)

        if t1 == t2:
            return "No winner in this game."

        if t1_total > t2_total:
            t1.win()
            return f"The winner is {team_name1}."
        else:
            t2.win()
            return f"The winner is {team_name2}."

    def get_statistics(self):
        result = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", "Teams:"]

        for team in self.teams:
            result.append(team.get_statistics())

        return "\n".join(result)
