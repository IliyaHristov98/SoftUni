from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):

    def __init__(self, name):
        super().__init__(name, strength=200)

    def can_climb(self):
        if self.strength >= 100:
            return True
        return False

    def climb(self, peak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)
