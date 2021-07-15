budget = float(input())
season = input()

price = 0
type_class = ""
type_of_car = ""

if budget <= 100:
    type_class = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        budget *= 0.35
    elif season == "Winter":
        type_of_car = "Jeep"
        budget *=0.65
elif 100 < budget <= 500:
    type_class = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        budget *= 0.45
    elif season == "Winter":
        type_of_car = "Jeep"
        budget *=0.80
elif budget > 500:
    type_class = "Luxury class"
    if season == "Summer" or season == "Winter":
        type_of_car = "Jeep"
        budget *= 0.90
price_of_car = budget
print(type_class)
print(f"{type_of_car} - {price_of_car:.2f}")