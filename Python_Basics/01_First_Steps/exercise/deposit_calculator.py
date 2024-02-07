deposit = float(input())
duration = int(input())
interest = float(input()) / 100
sum = deposit + duration * (deposit * interest) / 12
print(sum)