stack = []
count = int(input())

for _ in range(count):
    query = input().split()
    action = query[0]

    if action == "1":
        stack.append(int(query[1]))
    elif action == "2" and stack:
        stack.pop()
    elif action == "3" and stack:
        print(max(stack))
    elif action == "4" and stack:
        print(min(stack))

stack.reverse()
print(*stack, sep=", ")
