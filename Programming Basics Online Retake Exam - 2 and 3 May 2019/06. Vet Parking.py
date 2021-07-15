number_of_days = int(input())
hours_per_day = int(input())

sum_per_day = 0
total_sum = 0
day_count = 0

for day in range(1, number_of_days + 1):
    day_count += 1
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 == 1:
            sum_per_day += 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            sum_per_day += 1.25
        else:
            sum_per_day += 1
    print(f"Day: {day_count} - {sum_per_day:.2f} leva")
    total_sum += sum_per_day
    sum_per_day = 0
print(f"Total: {total_sum:.2f} leva")