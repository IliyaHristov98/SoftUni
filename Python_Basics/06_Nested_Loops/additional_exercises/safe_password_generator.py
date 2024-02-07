a = int(input())
b = int(input())
max_passwords = int(input())
count = 0
x_is_finished = False
y_is_finished = False
maximum_passwords_reached = False

for a_loop in range(35, 56):
    if x_is_finished and y_is_finished:
        break

    for b_loop in range(64, 97):
        if x_is_finished or y_is_finished:
            break
        A = a_loop
        B = b_loop

        for x in range(1, a + 1):
            if x == a:
                x_is_finished = True

            for y in range(1, b + 1):
                if y == b:
                    y_is_finished = True
                print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end="|")
                count += 1
                if count == max_passwords:
                    maximum_passwords_reached = True
                    break
                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64
            if maximum_passwords_reached:
                break
        if maximum_passwords_reached:
            break
    if maximum_passwords_reached:
        break
