age = float(input())
gender = input()

title = ''

if gender == 'm':
    if age < 16:
        title = 'Master'
    else:
        title = 'Mr.'
elif gender == 'f':
    if age < 16:
        title = 'Miss'
    else:
        title = 'Ms.'

print(title)