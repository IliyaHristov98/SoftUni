product = input()

type = ''

if product == 'banana' or product == 'apple' or product == 'kiwi' or product =='cherry' or\
        product == 'lemon' or product == 'grapes':
    type = 'fruit'
elif product == 'tomato' or product == 'cucumber' or product == 'carrot' or product == 'pepper':
    type = 'vegetable'
else:
    type = 'unknown'

print(type)