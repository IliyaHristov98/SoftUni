# for x1 in range(1, 11):
#     for x2 in range(1, 11):
#         print(f'{x1} * {x2} = {x1 * x2}')

x1 = 1
while x1 <= 10:
    x2 = 1
    while x2 <= 10:
        result = x1 * x2
        print(f'{x1} * {x2} = {result}')
        x2 += 1
    x1 += 1
