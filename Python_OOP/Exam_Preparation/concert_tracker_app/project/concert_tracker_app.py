from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    NEEDED_TYPES = ["Guitarist", "Drummer", "Singer"]
    GENRE_NEEDS = {
        "Rock": ["play the drums with drumsticks", "sing high pitch notes", "play rock"],
        "Metal": ["play the drums with drumsticks", "sing low pitch notes", "play metal"],
        "Jazz": ["play the drums with drum brushes", "play jazz"],
    }
    JAZZ_SINGER_NEEDS = ["sing high pitch notes", "sing low pitch notes"]

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):
        if musician_type not in self.MUSICIANS:
            raise ValueError("Invalid musician type!")

        try:
            musician = next(filter(lambda m: m.name == name, self.musicians))
            raise Exception(f"{name} is already a musician!")
        except StopIteration:
            self.musicians.append(self.MUSICIANS[musician_type](name, age))
            return f"{name} is now a {musician_type}."

    def create_band(self, name):
        try:
            band = next(filter(lambda b: b.name == name, self.bands))
            raise Exception(f"{name} band is already created!")
        except StopIteration:
            self.bands.append(Band(name))
            return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        try:
            concert = next(filter(lambda c: c.place == place, self.concerts))
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")
        except StopIteration:
            self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name, band_name):
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        self.musicians.remove(musician)
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        self.musicians.append(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        band = next(filter(lambda b: b.name == band_name, self.bands))

        for musician in band.members:
            if type(musician).__name__ in self.NEEDED_TYPES:
                self.NEEDED_TYPES.remove(type(musician).__name__)

        if self.NEEDED_TYPES:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        a = True

        for musician in band.members:

            if type(musician).__name__ == "Drummer":
                if not self.GENRE_NEEDS[concert.genre][0] in musician.skills:
                    a = False
            elif type(musician).__name__ == "Guitarist":
                if not self.GENRE_NEEDS[concert.genre][-1] in musician.skills:
                    a = False
            elif type(musician).__name__ == "Singer":
                if concert.genre == "Jazz":
                    if self.JAZZ_SINGER_NEEDS[0] not in musician.skills \
                            or self.JAZZ_SINGER_NEEDS[1] not in musician.skills:
                        a = False
                else:
                    if not self.GENRE_NEEDS[concert.genre][1] in musician.skills:
                        a = False

        if not a:
            raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
