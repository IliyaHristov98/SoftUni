def age_assignment(*names, **ages):
    result = []

    for letter, age in ages.items():
        for name in names:
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")
                break

    return "\n".join(sorted(result))
