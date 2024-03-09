from math import ceil


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for row in range(self.pages):
            if len(self.photos[row]) < 4:
                index = len(self.photos[row]) + 1
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {row + 1} slot {index}"
        return "No more free slots"

    def display(self) -> str:
        result = [11 * "-", ]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(11 * "-")

        return "\n".join(result)
