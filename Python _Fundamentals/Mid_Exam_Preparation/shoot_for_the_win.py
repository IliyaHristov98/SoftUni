targets = [int(x) for x in input().split()]
shot_targets = 0
while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if 0 <= index < len(targets) and targets[index] != -1:
        value = targets[index]
        for i in range(len(targets)):
            if targets[i] == -1:
                continue
            elif targets[i] <= value:
                targets[i] += value
            else:
                targets[i] -= value

        shot_targets += 1
        targets[index] = -1

print(f"Shot targets: {shot_targets} -> {' '.join(map(str,targets))}")
