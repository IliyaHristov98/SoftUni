city = input()
sales = float(input())

commision = 0

if sales <= 500:
    if city == 'Sofia':
        commision = sales * 0.05
    elif city == 'Varna':
        commision  = sales * 0.045
    elif city == 'Plovdiv':
        commision  = sales * 0.055
elif sales <= 1000:
    if city == 'Sofia':
        commision = sales * 0.07
    elif city == 'Varna':
        commision  = sales * 0.075
    elif city == 'Plovdiv':
        commision  = sales * 0.08
elif sales <= 10000:
    if city == 'Sofia':
        commision = sales * 0.08
    elif city == 'Varna':
        commision  = sales * 0.1
    elif city == 'Plovdiv':
        commision  = sales * 0.12
elif sales > 10000:
    if city == 'Sofia':
        commision = sales * 0.12
    elif city == 'Varna':
        commision  = sales * 0.13
    elif city == 'Plovdiv':
        commision  = sales * 0.145

if sales < 0:
    print('error')
elif commision == 0:
    print('error')
else:
    print(f'{commision:.2f}')