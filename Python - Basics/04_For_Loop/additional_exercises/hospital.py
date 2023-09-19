days = int(input())
treated = 0
untreated = 0
doctors = 7

for day in range(1, days + 1):
    patients = int(input())

    if day % 3 == 0 and untreated > treated:
        doctors += 1

    if patients <= 7:
        treated += patients
    else:
        treated += doctors
        untreated += patients - doctors

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')
