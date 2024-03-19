from typing import Dict


class dictionary_iter:

    def __init__(self, dictionary: Dict):
        self.dictionary = list(dictionary.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.dictionary):
            return self.dictionary[self.index]
        raise StopIteration
