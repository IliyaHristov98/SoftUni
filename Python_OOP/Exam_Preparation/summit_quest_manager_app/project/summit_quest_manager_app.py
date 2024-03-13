from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    PEAK_TYPES = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}
    total_climbed = 0

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."
        except StopIteration:
            pass

        self.climbers.append(self.CLIMBER_TYPES[climber_type](climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(self.PEAK_TYPES[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear):
        climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        peak = next(filter(lambda p: p.name == peak_name, self.peaks))

        required_gear = set(peak.get_recommended_gear())
        missing_gear = required_gear - set(gear)

        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. " \
               f"Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        elif not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb " \
                   f"{peak_name} and is therefore taking some rest."

        climber.climb(peak)
        self.total_climbed += 1
        return f"{climber_name} conquered {peak_name} " \
               f"whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks],
                                 key=lambda climber: (-len(climber.conquered_peaks), climber.name))

        result = [
            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"
        ]

        climber_statistics = "\n".join(str(c) for c in sorted_climbers)
        result.append(climber_statistics)

        return '\n'.join(result)
