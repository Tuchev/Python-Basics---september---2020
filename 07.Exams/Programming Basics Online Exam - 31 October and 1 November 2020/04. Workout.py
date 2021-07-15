from math import ceil

number_of_days = int(input())
km_per_day = float(input())
total_km = 0

for day in range(1, number_of_days + 2):
    if day == 1:
        total_km += km_per_day
        continue
    percent = int(input())
    km_per_day = km_per_day + (km_per_day * percent / 100)
    total_km += km_per_day
if total_km >= 1000:
    print(f"You've done a great job running {ceil(total_km - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - total_km)} more kilometers")