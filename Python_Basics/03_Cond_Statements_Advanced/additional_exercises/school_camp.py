season = input()
gender = input()
students = int(input())
nights = int(input())

sport = ''
price = 0

if season == 'Winter':
    if gender == 'boys':
        price = 9.60
        sport = 'Judo'
    elif gender == 'girls':
        price = 9.60
        sport = 'Gymnastics'
    else:
        price = 10
        sport = 'Ski'
elif season == 'Spring':
    if gender == 'boys':
        price = 7.20
        sport = 'Tennis'
    elif gender == 'girls':
        price = 7.20
        sport = 'Athletics'
    else:
        price = 9.50
        sport = 'Cycling'
elif season == 'Summer':
    if gender == 'boys':
        price = 15
        sport = 'Football'
    elif gender == 'girls':
        price = 15
        sport = 'Volleyball'
    else:
        price = 20
        sport = 'Swimming'

final_price = students * nights * price

if students >= 50:
    final_price = final_price * 0.5
elif 20 <= students < 50:
    final_price = final_price * 0.85
elif 10 <= students < 20:
    final_price = final_price * 0.95

print(f'{sport} {final_price:.2f} lv.')