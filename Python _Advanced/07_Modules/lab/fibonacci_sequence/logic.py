def create_fibonacci(length):
    sequence = [0, 1]

    for i in range(length - 2):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


def locate(number, fibonacci_sequence):
    try:
        index = fibonacci_sequence.index(number)
        return f"The number - {number} is at index {index}"

    except ValueError:
        return f"The number {number} is not in the sequence!"
