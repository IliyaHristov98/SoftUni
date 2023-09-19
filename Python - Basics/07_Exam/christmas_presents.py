years = input()
kids = 0
adults = 0
while years != 'Christmas':
    if int(years) <= 16:
        kids += 1
    else:
        adults += 1
    years = input()

sweaters_price = adults * 15
toys_price = kids * 5
print(f'Number of adults: {adults}\n'
      f'Number of kids: {kids}\n'
      f'Money for toys: {toys_price}\n'
      f'Money for sweaters: {sweaters_price}')
