# •	Цената на един литър гориво е 2.10 лв.
# •	Цената за екскурзовод е 100лв.
# •	В зависимост от деня има отстъпки от общата цена - за събота 10%, а за неделя 20%

budget = float(input())
fuel = float(input())
day = input()   # "Saturday" и "Sunday"

guide = 100
fuel_price = fuel * 2.1
total_price = guide + fuel_price
if day == "Saturday":
    total_price *= 0.9
elif day == "Sunday":
    total_price *= 0.8

diff = abs(budget - total_price)
if budget >= total_price:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")