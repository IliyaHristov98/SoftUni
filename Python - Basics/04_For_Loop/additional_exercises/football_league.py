capacity = int(input())
fans = int(input())

a_sector = 0
b_sector = 0
v_sector = 0
g_sector = 0

for fan in range(fans):
    sector = input()
    if sector == 'A':
        a_sector += 1
    elif sector == 'B':
        b_sector += 1
    elif sector == 'V':
        v_sector += 1
    else:
        g_sector += 1

print(f'{a_sector / fans * 100:.2f}%\n'
      f'{b_sector / fans * 100:.2f}%\n'
      f'{v_sector / fans * 100:.2f}%\n'
      f'{g_sector / fans * 100:.2f}%\n'
      f'{fans / capacity * 100:.2f}%')
