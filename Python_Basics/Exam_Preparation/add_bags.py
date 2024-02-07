bag_fee = float(input())
weight_in_kgs = float(input())
days_left = int(input())
bags_count = int(input())

if weight_in_kgs < 10:
    bag_fee = bag_fee * 0.2
elif weight_in_kgs <= 20:
    bag_fee = bag_fee * 0.5

if days_left > 30:
    bag_fee = bag_fee + bag_fee * 0.10
elif days_left >= 7:
    bag_fee = bag_fee + bag_fee * 0.15
else:
    bag_fee = bag_fee + bag_fee * 0.40

final_fee = bag_fee * bags_count

print(f'The total price of bags is: {final_fee:.2f} lv.')