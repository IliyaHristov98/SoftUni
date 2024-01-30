def accommodate_new_pets(cap, max_weight, *args):
    result = []
    guests = {}

    for type_pet, weight in args:
        if cap == 0:
            result.append("You did not manage to accommodate all pets!")
            break

        if weight > max_weight:
            continue

        if type_pet in guests:
            guests[type_pet] += 1
        else:
            guests[type_pet] = 1

        cap -= 1

    else:
        result.append(f"All pets are accommodated! Available capacity: {cap}.")

    result.append("Accommodated pets:")
    guests = sorted(guests.items(), key=lambda x: x[0])
    for guest in guests:
        result.append(f"{guest[0]}: {guest[1]}")

    return "\n".join(result)
