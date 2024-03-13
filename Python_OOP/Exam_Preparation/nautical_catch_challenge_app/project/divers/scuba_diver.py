from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    STARTING_OXYGEN = 540

    def __init__(self, name):
        super().__init__(name, oxygen_level=self.STARTING_OXYGEN)

    def miss(self, time_to_catch: int):
        used_oxy = round(time_to_catch * 0.3)
        if self.oxygen_level < used_oxy:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used_oxy

    def renew_oxy(self):
        self.oxygen_level = self.STARTING_OXYGEN
