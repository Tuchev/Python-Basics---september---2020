# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.

number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetable_menu = int(input())

price_for_all_menu = number_chicken_menu * 10.35 + number_fish_menu * 12.40 + number_vegetable_menu * 8.15
desert = price_for_all_menu * 0.2
total_price = price_for_all_menu + desert + 2.50
print(f"Total: {total_price:.2f}")