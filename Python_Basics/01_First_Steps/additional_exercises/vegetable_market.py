EUR = 0.51546391752

vegetable_price = float(input())
fruit_price = float(input())
vegetable_kgs = int(input())
fruit_kgs = int(input())

total_price_bgn = vegetable_price * vegetable_kgs + fruit_price * fruit_kgs
total_price_eur = total_price_bgn * EUR
print("%.2f" % total_price_eur)