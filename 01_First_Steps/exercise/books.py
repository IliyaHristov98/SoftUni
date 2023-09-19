pages = int(input())
page_per_hour = int(input())
days = int(input())
time_per_book = pages / page_per_hour
hours_per_day = time_per_book / days
print(int(hours_per_day))