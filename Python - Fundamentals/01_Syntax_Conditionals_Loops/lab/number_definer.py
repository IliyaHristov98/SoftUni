number = float(input())
small_or_large = ""
if 1 > number > 0 or 0 > number > -1:
    small_or_large = "small "
elif number > 1000000 or number < -1000000:
    small_or_large = "large "

if number == 0:
    print("zero")
elif number < 0:
    print(f"{small_or_large}negative")
elif number > 0:
    print(f"{small_or_large}positive")

