from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    STARTING_OXYGEN = 120

    def __init__(self, name):
        super().__init__(name, oxygen_level=self.STARTING_OXYGEN)

    def miss(self, time_to_catch: int):
        used_oxy = round(time_to_catch * 0.6)
        if self.oxygen_level < used_oxy:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used_oxy

    def renew_oxy(self):
        self.oxygen_level = self.STARTING_OXYGEN

