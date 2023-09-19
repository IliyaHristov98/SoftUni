shirt_price = float(input())
ball_winning_threshold = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (shorts_price + shirt_price) * 2
discount_percentage = 0.15

final_price = (shirt_price + shorts_price + shoes_price + socks_price) * (1 - discount_percentage)
if final_price >= ball_winning_threshold:
    print(f"Yes, he will earn the world-cup replica ball!\n"
          f"His sum is {final_price:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.\n"
          f"He needs {ball_winning_threshold - final_price:.2f} lv. more.")
