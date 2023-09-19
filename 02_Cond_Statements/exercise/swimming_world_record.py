record_time_seconds = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

time_needed = distance_in_meters * time_per_meter
resistance = (distance_in_meters // 15) * 12.5
total_time = time_needed + resistance
difference = total_time - record_time_seconds

if total_time < record_time_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
