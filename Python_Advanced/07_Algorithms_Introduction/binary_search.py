def binary_search(numbers, aim):
    left = 0
    right = len(numbers) - 1

    while left <= right:

        middle = (left + right) // 2
        middle_value = numbers[middle]

        if middle_value == aim:
            return middle
        elif middle_value < aim:
            left = middle + 1
        elif middle_value > aim:
            right = middle - 1

    return -1


values = sorted([int(x) for x in input().split()])
target = int(input())

print(binary_search(values, target))
