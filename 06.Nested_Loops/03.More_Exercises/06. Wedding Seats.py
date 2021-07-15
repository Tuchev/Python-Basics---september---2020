last_sector = input()
rows_first_sector = int(input())
number_of_seats_odd_row = int(input())

counter_seat = 0
start_sector = 65
start_seat = 97

for sector in range(start_sector, ord(last_sector) + 1):
    for row in range(1, rows_first_sector + 1):
        if row % 2 != 0:
            for seat in range(start_seat, (start_seat + number_of_seats_odd_row)):
                print(f"{chr(sector)}{row}{chr(seat)}")
                counter_seat += 1
        elif row % 2 == 0:
            for seat in range(start_seat, (start_seat + number_of_seats_odd_row + 2)):
                print(f"{chr(sector)}{row}{chr(seat)}")
                counter_seat += 1
    if rows_first_sector + 1 > rows_first_sector:
        rows_first_sector += 1
print(counter_seat)