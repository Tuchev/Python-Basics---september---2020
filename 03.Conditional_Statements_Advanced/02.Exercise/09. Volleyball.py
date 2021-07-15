from math import floor
year = input()
holidays = int(input())
weekends_to_travel = int(input())

total_weekends = 48
number_of_games_Sofia_in_weekend = (total_weekends - weekends_to_travel) * 3 / 4

number_of_games_Sofia_in_holiday = holidays * 2 / 3

total_games = number_of_games_Sofia_in_weekend + number_of_games_Sofia_in_holiday + weekends_to_travel

if year == "leap":
    total_games *= 1.15
print(f"{floor(total_games)}")