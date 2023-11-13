given_input = input().split()
final_result = 0

for item in given_input:
    current_result = 0
    if item[0].isupper():
        current_result = int(item[1:-1]) / (ord(item[0]) - 64)
    else:
        current_result = int(item[1:-1]) * (ord(item[0]) - 96)

    if item[-1].isupper():
        current_result -= ord(item[-1]) - 64
    else:
        current_result += ord(item[-1]) - 96

    final_result += current_result

print(f"{final_result:.2f}")
