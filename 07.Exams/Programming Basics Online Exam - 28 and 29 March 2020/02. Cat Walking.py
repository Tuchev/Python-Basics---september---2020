minutes_per_day = int(input())
number_of_daily_walk = int(input())
calories_per_den = int(input())

total_time_of_daily_walk = minutes_per_day * number_of_daily_walk
total_spent_calories = total_time_of_daily_walk * 5

if total_spent_calories >= calories_per_den / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_spent_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_spent_calories}.')