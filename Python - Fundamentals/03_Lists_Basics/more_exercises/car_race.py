initial_list = input().split()
left_car_times = []
right_car_times = []
left_car_total_time = 0
right_car_total_time = 0
for i in range(len(initial_list)):
    if i < len(initial_list) // 2:
        left_car_times.append(int(initial_list[i]))
    elif i > len(initial_list) // 2:
        right_car_times.append(int(initial_list[i]))

for left in left_car_times:
    if left == 0:
        left_car_total_time = left_car_total_time * 0.8
    else:
        left_car_total_time += left

for right in right_car_times[::-1]:
    if right == 0:
        right_car_total_time = right_car_total_time * 0.8
    else:
        right_car_total_time += right

if right_car_total_time < left_car_total_time:
    print(f'The winner is right with total time: {right_car_total_time:.1f}')
elif left_car_total_time < right_car_total_time:
    print(f'The winner is left with total time: {left_car_total_time:.1f}')
