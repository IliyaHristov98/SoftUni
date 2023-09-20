N = int(input())
ascii_sum = 0
for n in range(N):
    character = input()
    ascii_sum += ord(character)
print(f'The sum equals: {ascii_sum}')
