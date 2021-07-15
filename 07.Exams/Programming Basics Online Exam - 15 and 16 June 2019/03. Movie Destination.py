budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

price_for_day = 0

if destination == "Dubai":
    if season == "Winter":
        price_for_day = 45000 * 0.7
    elif season == "Summer":
        price_for_day = 40000 * 0.7
elif destination == "Sofia":
    if season == "Winter":
        price_for_day = 17000 * 1.25
    elif season == "Summer":
        price_for_day = 12500 * 1.25
elif destination == "London":
    if season == "Winter":
        price_for_day = 24000
    elif season == "Summer":
        price_for_day = 20250
total_sum = number_of_days * price_for_day
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")