number_of_coins_1lv = int(input())
number_of_coins_2lv = int(input())
number_of_coins_5lv = int(input())
sum = int(input())

for num_1 in range(0, number_of_coins_1lv + 1):
    for num_2 in range(0, number_of_coins_2lv + 1):
        for num_3 in range(0, number_of_coins_5lv + 1):
            if (num_1 * 1 + num_2 * 2 + num_3 * 5) == sum:
                print(f"{num_1} * 1 lv. + {num_2} * 2 lv. + {num_3} * 5 lv. = {sum} lv.")