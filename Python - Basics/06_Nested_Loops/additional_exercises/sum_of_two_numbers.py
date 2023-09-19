start_number = int(input())
end_number = int(input())
magic_number = int(input())
count = 0
magic_number_is_found = False
for first in range(start_number, end_number + 1):
    for second in range(start_number, end_number + 1):
        count += 1
        if first + second == magic_number:
            print(f'Combination N:{count} ({first} + {second} = {magic_number})')
            magic_number_is_found = True
            break
    if first + second == magic_number:
        break

if not magic_number_is_found:
    print(f'{count} combinations - neither equals {magic_number}')
