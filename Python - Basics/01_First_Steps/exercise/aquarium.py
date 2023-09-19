l = int(input())
w = int(input())
h = int(input())
percentage = float(input()) / 100

total_intake = l * w * h
liters = total_intake / 1000

total_liters = liters - liters * percentage
print(float(total_liters))