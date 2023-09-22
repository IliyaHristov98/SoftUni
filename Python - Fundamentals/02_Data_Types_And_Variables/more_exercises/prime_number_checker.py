number = int(input())
is_true = True
if number > 1:
    for x in range(2, number):
        for y in range(2, number):
            if x * y == number:
                is_true = False
                break
if is_true:
    print("True")
else:
    print("False")
