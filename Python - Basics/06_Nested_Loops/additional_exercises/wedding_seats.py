last_sector = input()
first_sector_rows = int(input())
odd_rows_seats = int(input())
even_rows_seats = odd_rows_seats + 2
total_seats = 0

for sector in range(65, ord(last_sector) + 1):

    for row in range(1, first_sector_rows + 1):

        if row % 2 != 0:
            for seat_odd in range(1, odd_rows_seats + 1):
                ascii_seat = chr(seat_odd + 96)
                print(f'{chr(sector)}{row}{ascii_seat}')
                total_seats += 1
        else:
            for seat_even in range(1, even_rows_seats + 1):
                ascii_seat = chr(seat_even + 96)
                print(f'{chr(sector)}{row}{ascii_seat}')
                total_seats += 1

    first_sector_rows += 1
print(total_seats)
