from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):

    def __init__(self, name, points):
        super().__init__(name, points, time_to_catch=90)

    def fish_details(self):
        return f"{type(self).__name__}: {self.name} " \
               f"[Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"
