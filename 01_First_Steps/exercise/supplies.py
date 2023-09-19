pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input()) / 100

total_before_discount = pens * 5.8 + markers * 7.2 + detergent * 1.2
final_total = total_before_discount - total_before_discount * discount
print(final_total)