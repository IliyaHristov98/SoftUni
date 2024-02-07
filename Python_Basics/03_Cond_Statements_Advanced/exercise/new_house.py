flower = input()
number_of_flowers = int(input())
budget = int(input())

price = 0

if flower == "Roses":
    if number_of_flowers > 80:
        price = number_of_flowers * 5 * 0.9
    else:
        price = number_of_flowers * 5
elif flower == "Dahlias":
    if number_of_flowers > 90:
        price = number_of_flowers * 3.80 * 0.85
    else:
        price = number_of_flowers * 3.80
elif flower == "Tulips":
    if number_of_flowers > 80:
        price = number_of_flowers * 2.80 * 0.85
    else:
        price = number_of_flowers * 2.80
elif flower == "Narcissus":
    if number_of_flowers < 120:
        price = number_of_flowers * 3 * 1.15
    else:
        price = number_of_flowers * 3
elif flower == "Gladiolus":
    if number_of_flowers < 80:
        price = number_of_flowers * 2.5 * 1.20
    else:
        price = number_of_flowers * 2.5

if price <= budget:
    print(f'Hey, you have a great garden with {number_of_flowers} {flower} and {budget - price:.2f} leva left.')
elif price > budget:
    print(f'Not enough money, you need {price - budget:.2f} leva more.')