train_list = [0 for x in range(int(input()))]
command = input().split()

while command[0] != "End":
    if command[0] == "add":
        people = int(command[1])
        train_list[-1] += people

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        train_list[index] += people

    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        train_list[index] -= people

    command = input().split()

print(train_list)
