time_a = int(input())
time_b = int(input())
time_c = int(input())

total_time_in_seconds = time_a + time_b + time_c

minutes = total_time_in_seconds // 60
seconds = total_time_in_seconds % 60

print(f'{minutes}:{seconds :02d}')

