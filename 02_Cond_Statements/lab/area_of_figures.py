from math import pi

shape = input()
if shape == 'square':
    side = float(input())
    area = side * side
    print(f"{area:.3f}")
elif shape == 'rectangle':
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
    print(f"{area:.3f}")
elif shape == 'circle':
    radius = float(input())
    area = pi * radius ** 2
    print(f"{area:.3f}")
elif shape == 'triangle':
    side = float(input())
    height = float(input())
    area = side * height / 2
    print(f"{area:.3f}")


