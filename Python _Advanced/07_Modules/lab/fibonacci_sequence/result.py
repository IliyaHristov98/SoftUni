from logic import create_fibonacci, locate

command = input().split()

while command[0] != "Stop":

    number = int(command[-1])

    if command[0] == "Create":
        sequence = create_fibonacci(number)
        print(" ".join(map(str, sequence)))
    else:
        print(locate(number, sequence))

    command = input().split()
