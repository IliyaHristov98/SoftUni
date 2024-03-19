class vowels:
    VOWELS = ["a", "e", "i", "u", "y", "o"]

    def __init__(self, given_string):
        self.given_string = given_string
        self.current = -1
        self.vowels = [c for c in self.given_string if c.lower() in self.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1

        if self.current < len(self.vowels):
            return self.vowels[self.current]
        raise StopIteration
