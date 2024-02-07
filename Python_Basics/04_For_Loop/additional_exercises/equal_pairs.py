n = int(input())
prev_pair = int(input()) + int(input())
max_diff = 0

for pair in range(n - 1):
    current_pair = int(input()) + int(input())

    if abs(prev_pair-current_pair) > max_diff:
        max_diff = abs(prev_pair-current_pair)

    prev_pair = current_pair

if max_diff == 0:
    print(f'Yes, value={prev_pair}')
else:
    print(f'No, maxdiff={max_diff}')


