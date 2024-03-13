from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):

    def __init__(self, name):
        super().__init__(name, strength=150)

    def can_climb(self):
        if self.strength >= 75:
            return True
        return False

    def climb(self, peak):
        if peak.difficulty_level == "Advanced":
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5

        self.conquered_peaks.append(peak.name)
