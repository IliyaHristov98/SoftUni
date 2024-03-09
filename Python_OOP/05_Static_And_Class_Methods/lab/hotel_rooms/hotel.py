class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        result = room.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        people = room.guests
        result = room.free_room()

        if result is None:
            self.guests -= people

    def status(self):
        free = ', '.join(str(room.number) for room in self.rooms if not room.is_taken)
        taken = ', '.join(str(room.number) for room in self.rooms if room.is_taken)
        result = f"Hotel {self.name} has {self.guests} total guests" \
                 f"\nFree rooms: {free}" \
                 f"\nTaken rooms: {taken}"
        return result
