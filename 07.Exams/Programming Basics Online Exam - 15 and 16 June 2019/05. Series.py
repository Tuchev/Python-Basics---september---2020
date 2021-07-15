budget = float(input())
n = int(input())
total_sum = 0

for serial in range(1, n + 1):
    name_of_serial = input()
    price = float(input())
    if name_of_serial == "Thrones":
        price *= 0.5
    elif name_of_serial == "Lucifer":
        price *= 0.6
    elif name_of_serial == "Protector":
        price *= 0.7
    elif name_of_serial == "TotalDrama":
        price *= 0.8
    elif name_of_serial == "Area":
        price *= 0.9
    total_sum += price

diff = abs(budget - total_sum)
if budget >= total_sum:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")