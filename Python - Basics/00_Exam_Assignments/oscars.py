rent = int(input())
statues = rent * 0.7
catering = statues * 0.85
sound = catering * 0.5


total_cost = rent + statues + catering + sound
print(f'{total_cost:.2f}')
