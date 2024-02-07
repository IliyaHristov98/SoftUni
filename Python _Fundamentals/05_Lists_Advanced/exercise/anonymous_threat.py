initial_list = input().split()
while True:
    command = input().split()
    if command[0] == "3:1":
        break

    if command[0] == "merge":
        start = int(command[1])
        end = int(command[2])
        if start < 0:
            start = 0
        if end > len(initial_list) - 1:
            end = len(initial_list) - 1

        for index, word in enumerate(initial_list):
            if start < index <= end:
                initial_list[start] += initial_list[index]
        for index in range(end, start, -1):
            initial_list.pop(index)

    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        if partitions > len(initial_list[index]):
            step = 1
        else:
            step = len(initial_list[index]) // partitions

        popped_index = initial_list.pop(index)
        start = 0

        for steps in range(partitions):
            if steps == partitions - 1:
                initial_list.insert(index, popped_index[start::])
                break
            else:
                initial_list.insert(index, popped_index[start: start + step:])
                start += step
                index += 1

print(" ".join(initial_list))
