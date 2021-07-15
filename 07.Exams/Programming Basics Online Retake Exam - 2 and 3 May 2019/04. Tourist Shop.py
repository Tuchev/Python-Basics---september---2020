budget = float(input())
command = input()
total_sum = 0
count_of_products = 0
total_count_of_product = 0

while command != "Stop":
    price_of_product = float(input())
    count_of_products += 1
    total_count_of_product += 1
    if count_of_products == 3:
        price_of_product /= 2
        count_of_products = 0
    total_sum += price_of_product
    if total_sum > budget:
        break
    command = input()

diff = abs(budget - total_sum)
if command == "Stop":
    print(f"You bought {total_count_of_product} products for {total_sum:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {diff:.2f} leva!")