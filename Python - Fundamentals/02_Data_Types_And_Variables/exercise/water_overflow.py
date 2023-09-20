capacity = 255
number_of_lines = int(input())
max_liters = 0
for i in range(number_of_lines):
    liters_to_add = int(input())
    if capacity - liters_to_add < 0:
        print("Insufficient capacity!")
        continue
    elif capacity - liters_to_add >= 0:
        capacity -= liters_to_add
        max_liters += liters_to_add
print(max_liters)
