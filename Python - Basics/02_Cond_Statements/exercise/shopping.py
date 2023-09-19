VIDEO_CARD_PRICE = 250
DISCOUNT = 0.15

budget = float(input())
video_card_count = int(input())
processor_count = int(input())
ram_count = int(input())

video_card_total_price = video_card_count * VIDEO_CARD_PRICE
processor_total_price = (video_card_total_price * 0.35) * processor_count
ram_total_price = (video_card_total_price * 0.10) * ram_count

final_price = video_card_total_price + processor_total_price + ram_total_price

if video_card_count > processor_count:
    final_price = final_price - (final_price * DISCOUNT)

if budget >= final_price:
    print(f"You have {budget - final_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_price - budget:.2f} leva more!")