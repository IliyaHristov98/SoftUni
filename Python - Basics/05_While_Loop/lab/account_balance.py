total = 0
funds = input()
while funds != 'NoMoreMoney':
    if float(funds) < 0:
        print(f'Invalid operation!')
        break
    print(f'Increase: {float(funds):.2f}')
    total += float(funds)
    funds = input()
print(f'Total: {total:.2f}')
