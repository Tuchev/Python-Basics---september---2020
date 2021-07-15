season = input() # "Winter", "Spring", "Summer"
type_of_group = input() # "boys", "girls", "mixed"
number_of_scholar = int(input())
number_of_overnight = int(input())

price_per_scholar = 0
type_of_sport = ""

if type_of_group == "boys":
    if season == "Winter":
        type_of_sport = "Judo"
        price_per_scholar = 9.60
    elif season == "Spring":
        type_of_sport = "Tennis"
        price_per_scholar = 7.20
    elif season == "Summer":
        type_of_sport = "Football"
        price_per_scholar = 15
elif type_of_group == "girls":
    if season == "Winter":
        type_of_sport = "Gymnastics"
        price_per_scholar = 9.60
    elif season == "Spring":
        type_of_sport = "Athletics"
        price_per_scholar = 7.20
    elif season == "Summer":
        type_of_sport = "Volleyball"
        price_per_scholar = 15
elif type_of_group == "mixed":
    if season == "Winter":
        type_of_sport = "Ski"
        price_per_scholar = 10
    elif season == "Spring":
        type_of_sport = "Cycling"
        price_per_scholar = 9.50
    elif season == "Summer":
        type_of_sport = "Swimming"
        price_per_scholar = 20
if number_of_scholar >= 50:
    price_per_scholar *= 0.5
elif 20 <= number_of_scholar < 50:
    price_per_scholar *= 0.85
elif 10 <= number_of_scholar < 20:
    price_per_scholar *= 0.95
else:
    price_per_scholar *= 1

total_sum = number_of_scholar * number_of_overnight * price_per_scholar
print(f"{type_of_sport} {total_sum:.2f} lv.")