number_of_day_off = int(input())

#Том обича да спи по 30 000 минути в годината - 500 часа
#време за игра, когато е на работа - 63 минути на ден
#време за игра, когато почива - 127 минути на ден
#една година е 365 дни

total_time_for_game = (number_of_day_off * 127) + (365 - number_of_day_off) * 63
difference = abs(30000 - total_time_for_game)
time_in_hours = difference // 60
time_in_minutes = difference % 60

if total_time_for_game <= 30000:
    print('Tom sleeps well')
    print(f'{time_in_hours} hours and {time_in_minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{time_in_hours} hours and {time_in_minutes} minutes more for play')