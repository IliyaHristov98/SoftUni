paper_price = 5.8
fabric_price = 7.2
glue_price = 1.2

paper_rows = int(input())
fabric_rows = int(input())
glue_liters = float(input())
discount_percentage = int(input())

price_before_discount = paper_rows * paper_price + fabric_rows * fabric_price + glue_liters * glue_price
discounted_price = price_before_discount * (1 - discount_percentage / 100)
print(f'{discounted_price:.3f}')
