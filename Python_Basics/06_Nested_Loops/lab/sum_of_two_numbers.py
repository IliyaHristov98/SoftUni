start = int(input())
end = int(input())
magic_number = int(input())
x1 = start
x2 = start
count = 0
combination_found = False
for x1 in range(start, end + 1):
    for x2 in range(start, end + 1):
        count += 1
        if x1 + x2 == magic_number:
            combination_found = True
            break
    if x1 + x2 == magic_number:
        combination_found = True
        break
if combination_found:
    print(f"Combination N:{count} ({x1} + {x2} = {magic_number})")
elif not combination_found:
    print(f"{count} combinations - neither equals {magic_number}")
