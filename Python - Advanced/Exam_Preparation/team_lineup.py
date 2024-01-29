def team_lineup(*args):
    nationalities = {}
    result = []

    for name, country in args:
        if country not in nationalities:
            nationalities[country] = []

        nationalities[country].append(name)

    nationalities = sorted(nationalities.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in nationalities:
        result.append(f"{key}:")
        for val in value:
            result.append(f"  -{val}")

    return "\n".join(result)
