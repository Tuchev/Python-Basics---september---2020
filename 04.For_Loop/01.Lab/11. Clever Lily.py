ages = int(input())
laundry = float(input())
price_per_toy = int(input())
number_of_toy = 0
amount_collect = 0
total_amount = 0


for age in range(1, ages + 1):
    if age % 2 == 1:
        number_of_toy += 1
    elif age % 2 == 0:
        amount_collect += 10
        total_amount += amount_collect - 1

total_sum_from_toys = number_of_toy * price_per_toy
total_sum_collect = total_amount + total_sum_from_toys
difference = abs(laundry - total_sum_collect)
if total_sum_collect >= laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")