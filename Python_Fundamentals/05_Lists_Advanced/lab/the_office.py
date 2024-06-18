all_employees = [int(x) for x in input().split()]
factor = int(input())
multiplied_happiness = [i*factor for i in all_employees]
average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
happy_employees = [y for y in multiplied_happiness if y >= average_happiness]
if len(happy_employees) >= len(all_employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(all_employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(all_employees)}. Employees are not happy!")
