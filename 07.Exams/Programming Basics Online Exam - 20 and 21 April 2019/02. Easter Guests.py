from math import ceil
number_of_guests = int(input())
budget = int(input())

number_of_easter_breads = ceil(number_of_guests / 3)
number_of_eggs = number_of_guests * 2

price_of_easter_bread = 4
price_of_egg = 0.45

total_sum_for_easter_breads = number_of_easter_breads * price_of_easter_bread
total_sum_for_eggs = number_of_eggs * price_of_egg
total_sum = total_sum_for_easter_breads + total_sum_for_eggs
difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Lyubo bought {number_of_easter_breads} Easter bread and {number_of_eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")