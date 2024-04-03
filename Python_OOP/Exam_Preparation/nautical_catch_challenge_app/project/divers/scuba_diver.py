from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name):
        super().__init__(name, oxygen_level=540)

    def miss(self, time_to_catch):
        if self.oxygen_level > round(0.3 * time_to_catch):
            self.oxygen_level -= round(0.3 * time_to_catch)
            return

        self.oxygen_level = 0
        self.has_health_issues = True

    def renew_oxy(self):
        self.oxygen_level = 540
