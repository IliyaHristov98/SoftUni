name = input()
year = 1
total_grade = 0
fails = 0

while year <= 12:
    yearly_grade = float(input())
    if yearly_grade < 4:
        fails += 1
        if fails > 1:
            break
        continue
    year += 1
    total_grade += yearly_grade

if year < 12:
    print(f'{name} has been excluded at {year} grade')
else:
    print(f'{name} graduated. Average grade: {total_grade / 12:.2f}')
