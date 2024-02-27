from album import Album
from song import Song


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        try:
            album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if album.published:
            return f"Album has been published. It cannot be removed."

        self.albums.remove(album)
        return f"Album {album.name} has been removed."

    def details(self):
        details = "\n".join(a.details() for a in self.albums)
        return f"Band {self.name}\n{details}"
