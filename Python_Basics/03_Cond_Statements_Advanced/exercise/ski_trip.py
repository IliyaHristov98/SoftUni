days = int(input())
type_of_room = input()
opinion = input()

nights = days - 1
room_for_one = 18
apartment = 25
president = 35
total_price = 0

if type_of_room == 'room for one person':
    total_price = room_for_one * nights
elif type_of_room == "apartment":
    total_price = apartment * nights
    if nights < 10:
        total_price = total_price * 0.7
    elif 10 < nights <= 15:
        total_price = total_price * 0.65
    elif nights > 15:
        total_price = total_price * 0.5
elif type_of_room == "president apartment":
    total_price = president * nights
    if nights < 10:
        total_price = total_price * 0.9
    elif 10 < nights <= 15:
        total_price = total_price * 0.85
    elif nights > 15:
        total_price = total_price * 0.8

if opinion == 'positive':
    total_price = total_price * 1.25
else:
    total_price = total_price * 0.9

print(f'{total_price:.2f}')