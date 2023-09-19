students = int(input())

poor = 0
middle = 0
good = 0
excellent = 0
total = 0

for student in range(students):
    grade = float(input())
    total += grade

    if grade < 3:
        poor += 1
    elif grade < 4:
        middle += 1
    elif grade < 5:
        good += 1
    else:
        excellent += 1

print(f"Top students: {excellent / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {good / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {middle / students * 100:.2f}%")
print(f"Fail: {poor / students * 100:.2f}%")
print(f"Average: {total / students:.2f}")