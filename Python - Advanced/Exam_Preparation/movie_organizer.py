def movie_organizer(*movies):
    collection = {}
    final_string = ""
    for name, genre in movies:

        if genre not in collection:
            collection[genre] = []

        collection[genre].append(name)

    for genre in collection:
        collection[genre] = sorted(collection[genre])

    sorted_collection = sorted(collection.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, item in sorted_collection:
        final_string += f"{key} - {len(item)}\n"

        for movie in item:
            final_string += f"* {movie}\n"

    return final_string
