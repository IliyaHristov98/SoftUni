input_numbers = [int(i) for i in input().split(", ")]

print(f"Positive: {', '. join(str(x) for x in input_numbers if x >= 0)}")
print(f"Negative: {', '. join(str(y) for y in input_numbers if y < 0)}")
print(f"Even: {', '. join(str(z) for z in input_numbers if z % 2 == 0)}")
print(f"Odd: {', '. join(str(m) for m in input_numbers if m % 2 != 0)}")
