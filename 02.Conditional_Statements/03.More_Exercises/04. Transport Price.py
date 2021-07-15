n_number_of_kilometers = int(input())
day_or_night = input()

day_price_of_taxi = 0.70 + (0.79 * n_number_of_kilometers)
night_price_of_taxi = 0.70 + (0.90 * n_number_of_kilometers)
price_of_bus = 0.09 * n_number_of_kilometers
price_of_train = 0.06 * n_number_of_kilometers

if n_number_of_kilometers < 20:
    if day_or_night == "day":
        print(f'{day_price_of_taxi:.2f}')
    elif day_or_night == "night":
        print(f'{night_price_of_taxi:.2f}')
elif 20 <= n_number_of_kilometers < 100:
    print(f'{price_of_bus:.2f}')
else:
    print(f'{price_of_train:.2f}')