season = input()
kilometers_per_month = float(input())

price_for_kilometer = 0

if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_for_kilometer = 0.75
    elif season == "Summer":
        price_for_kilometer = 0.90
    elif season == "Winter":
        price_for_kilometer = 1.05
elif 5000 < kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_for_kilometer = 0.95
    elif season == "Summer":
        price_for_kilometer = 1.10
    elif season == "Winter":
        price_for_kilometer = 1.25
elif 10000 < kilometers_per_month <= 20000:
    if season == "Spring" or season == "Summer" or season == "Autumn" or season == "Winter":
        price_for_kilometer = 1.45
salary = (kilometers_per_month * price_for_kilometer * 4) * 0.9
print(f"{salary:.2f}")