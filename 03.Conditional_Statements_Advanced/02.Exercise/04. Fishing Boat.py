budget = int(input())
season = input() # "Spring", "Summer", "Autumn" или "Winter"
number_of_fishermans = int(input())
price = 0
if season == "Spring":
    price = 3000
    if number_of_fishermans <= 6:
        price *= 0.9
        if number_of_fishermans % 2 == 0:
            price *= 0.95
    elif 7 < number_of_fishermans <= 11:
        price *= 0.85
        if number_of_fishermans % 2 == 0:
            price *= 0.95
    elif number_of_fishermans >= 12:
        price *= 0.75
        if number_of_fishermans % 2 == 0:
            price *= 0.95
elif season == "Summer":
    price = 4200
    if number_of_fishermans <= 6:
        price *= 0.9
        if number_of_fishermans % 2 == 0:
            price *= 0.95
    elif 7 < number_of_fishermans <= 11:
        price *= 0.85
        if number_of_fishermans % 2 == 0:
            price *= 0.95
    elif number_of_fishermans >= 12:
        price *= 0.75
        if number_of_fishermans % 2 == 0:
            price *= 0.95
elif season == "Autumn":
    price = 4200
    if number_of_fishermans <= 6:
        price *= 0.9
    elif 7 < number_of_fishermans <= 11:
        price *= 0.85
    elif number_of_fishermans >= 12:
        price *= 0.75
elif season == "Winter":
    price = 2600
    if number_of_fishermans <= 6:
        price *= 0.9
        if number_of_fishermans % 2 == 0:
            price *= 0.95
    elif 7 < number_of_fishermans <= 11:
        price *= 0.85
        if number_of_fishermans % 2 == 0:
            price *= 0.95
    elif number_of_fishermans >= 12:
        price *= 0.75
        if number_of_fishermans % 2 == 0:
            price *= 0.95
difference = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")