n = int(input())
cars = {}
for _ in range(n):
    car, mileage, fuel = input().split("|")
    cars[car] = {}
    cars[car]["Mileage"] = int(mileage)
    cars[car]["Fuel"] = int(fuel)

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split(" : ")
    car = command[1]
    if command[0] == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car]["Fuel"] < fuel:
            print(f"Not enough fuel to make that ride")
        else:
            cars[car]["Fuel"] -= fuel
            cars[car]["Mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    elif command[0] == "Refuel":
        fuel = int(command[2])
        previous_fuel = cars[car]["Fuel"]
        current_fuel = cars[car]["Fuel"]
        added = 0
        if current_fuel < 75:
            current_fuel += fuel
            if current_fuel >= 75:
                added = 75 - previous_fuel
                cars[car]["Fuel"] = 75
            else:
                added = fuel
                cars[car]["Fuel"] = current_fuel
        print(f"{car} refueled with {added} liters")

    else:
        kilometers = int(command[2])
        previous_mileage = cars[car]["Mileage"]
        current_mileage = cars[car]["Mileage"] - kilometers
        if current_mileage < 10000:
            cars[car]["Mileage"] = 10000
        else:
            cars[car]["Mileage"] = current_mileage
            print(f"{car} mileage decreased by {kilometers} kilometers")

    if cars[car]["Mileage"] >= 100000:
        del cars[car]
        print(f"Time to sell the {car}!")

for key, value in cars.items():
    print(f"{key} -> Mileage: {cars[key]['Mileage']} kms, Fuel in the tank: {cars[key]['Fuel']} lt.")
