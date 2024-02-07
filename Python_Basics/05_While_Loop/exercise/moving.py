width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
filled_space = 0
room_full = True

while filled_space < volume:
    number_of_boxes = input()
    if number_of_boxes == 'Done':
        if filled_space < volume:
            room_full = False
            break
    filled_space += int(number_of_boxes)

if room_full:
    print(f'No more free space! You need {filled_space - volume} Cubic meters more.')
elif not room_full:
    print(f'{volume - filled_space} Cubic meters left.')