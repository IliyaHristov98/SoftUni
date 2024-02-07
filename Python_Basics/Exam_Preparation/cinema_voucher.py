voucher_value = int(input())
item = input()
tickets = 0
other_items = 0
while item != 'End':
    if len(item) > 8:
        price = (ord(item[0]) + ord(item[1]))
        if voucher_value < price:
            break
        else:
            voucher_value -= price
        tickets += 1
    else:
        price = ord(item[0])
        if voucher_value < price:
            break
        else:
            voucher_value -= price
        other_items += 1

    item = input()

print(f'{tickets}\n'
      f'{other_items}')

