def forecast(*args):
    dict_of_results = {"Sunny": [], "Cloudy": [], "Rainy": []}
    result = ""

    for arg in args:
        city, weather = arg
        dict_of_results[weather].append(city)

        result = ''.join([f"{val} - {key}\n" for key, value in dict_of_results.items() for val in sorted(value)])

    return result
