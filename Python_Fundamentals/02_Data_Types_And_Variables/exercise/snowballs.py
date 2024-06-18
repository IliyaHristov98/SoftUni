number_of_snowballs = int(input())
best_snowball_value = 0
best_weight = 0
best_time = 0
best_quality = 0
for ball in range(number_of_snowballs):
    weight = int(input())
    travel_time = int(input())
    quality = int(input())
    value = (weight / travel_time) ** quality
    if value > best_snowball_value:
        best_snowball_value = value
        best_weight = weight
        best_time = travel_time
        best_quality = quality
print(f"{best_weight} : {best_time} = {int(best_snowball_value)} ({best_quality})")
