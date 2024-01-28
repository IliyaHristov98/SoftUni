def math_operations(*numbers, **kwargs):
    count = 0

    for number in numbers:
        count += 1
        if count == 1:
            kwargs["a"] += number
        elif count == 2:
            kwargs["s"] -= number
        elif count == 3:
            if number == 0:
                continue
            kwargs["d"] /= number
        elif count == 4:
            kwargs["m"] *= number
            count = 0

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f"{key}: {value:.1f}" for key, value in kwargs)
