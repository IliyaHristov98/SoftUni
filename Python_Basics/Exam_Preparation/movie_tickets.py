a1 = int(input())
a2 = int(input())
n = int(input())
n1 = int(n/2-1)

for symbol_one in range(a1, a2):
    for symbol_two in range(1, n):
        for symbol_three in range(1, n1 + 1):
            symbol_four = ord(chr(symbol_one))
            if symbol_one % 2 != 0 and (symbol_two + symbol_three + symbol_four) % 2 != 0:
                print(f'{chr(symbol_one)}-{symbol_two}{symbol_three}{symbol_four}')
