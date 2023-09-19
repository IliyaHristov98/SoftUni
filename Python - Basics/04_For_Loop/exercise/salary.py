tabs = int(input())
salary = float(input())

for browser in range(tabs):
    page = input()
    if page == 'Facebook':
        salary -= 150
    elif page == 'Instagram':
        salary -= 100
    elif page == 'Reddit':
        salary -= 50

    if salary <= 0:
        print(f'You have lost your salary.')
        break

if salary > 0:
    print(round(salary))
