from typing import List


class reverse_iter:

    def __init__(self, iterable: List):
        self.iterable = iterable
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if abs(self.current) <= len(self.iterable):
            return self.iterable[self.current]
        raise StopIteration
