def vowel_filter(function):
    def wrapper():
        result = function()
        return [el for el in result if el.lower() in "aeyiou"]

    return wrapper
