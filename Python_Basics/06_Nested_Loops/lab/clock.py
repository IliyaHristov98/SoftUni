# for h in range(24):
#     for m in range(60):
#         print(f'{h}:{m}')

hour = 0
while hour < 24:
    minute = 0
    while minute < 60:
        print(f'{hour}:{minute}')
        minute += 1
    hour += 1
