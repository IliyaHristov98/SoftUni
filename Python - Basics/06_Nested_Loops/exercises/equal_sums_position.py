first = int(input())
second = int(input())

for num in range(first, second + 1):
    number_to_str = str(num)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0 or index == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(num, end = ' ')
