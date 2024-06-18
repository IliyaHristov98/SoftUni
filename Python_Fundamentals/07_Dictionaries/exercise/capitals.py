countries = input().split(", ")
capitals = input().split(", ")

pairs = {countries: capitals for countries, capitals in zip(countries, capitals)}

for country, capital in pairs.items():
    print(f"{country} -> {capital}")
