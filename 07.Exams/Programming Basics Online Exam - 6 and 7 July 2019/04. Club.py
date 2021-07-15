goal_profit = float(input())

total_profit = 0
command = input()

while command != "Party!":
    cocktail = command
    num_of_coctails = int(input())
    price_of_order = len(cocktail) * num_of_coctails
    if price_of_order % 2 != 0:
        price_of_order -= price_of_order * 0.25
    total_profit += price_of_order
    if total_profit >= goal_profit:
        print("Target acquired.")
        break
    command = input()

if total_profit < goal_profit:
    print(f"We need {goal_profit - total_profit:.2f} leva more.")

print(f"Club income - {total_profit:.2f} leva.")