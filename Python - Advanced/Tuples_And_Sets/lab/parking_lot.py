n = int(input())
cars = set()

for _ in range(n):
    direction, plate = input().split(", ")
    if direction == "IN":
        cars.add(plate)
    else:
        if plate in cars:
            cars.remove(plate)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
