kilometers = int(input())
time_of_day = input()

TAXI_INITIAL_FEE = 0.70
BUS_COST_PER_KM = 0.09
TRAIN_COST_PER_KM = 0.06

taxi_cost_per_km = 0

if time_of_day == "day":
    taxi_cost_per_km = 0.79
else:
    taxi_cost_per_km = 0.90

total_taxi_cost = kilometers * taxi_cost_per_km + TAXI_INITIAL_FEE
total_bus_cost = kilometers * BUS_COST_PER_KM
total_train_cost = kilometers * TRAIN_COST_PER_KM

if kilometers < 20:
    print(f'{total_taxi_cost:.2f}')
elif kilometers < 100:
    print(f'{total_bus_cost:.2f}')
else:
    print(f'{total_train_cost:.2f}')