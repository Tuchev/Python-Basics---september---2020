from math import ceil
name_of_film = input()
time_of_film = int(input())
time_of_lunch_break = int(input())

time_for_lunch = time_of_lunch_break * 1 / 8
time_for_relax = time_of_lunch_break * 1 / 4

time_left = time_of_lunch_break - time_for_lunch - time_for_relax
diff = abs(time_left - time_of_film)

if time_left >= time_of_film:
    print(f"You have enough time to watch {name_of_film} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_film}, you need {ceil(diff)} more minutes.")