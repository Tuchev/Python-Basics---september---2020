# •	цената на килограм захар е с 25% по-ниска от тази на килограм брашно
# •	цената на една кора с яйца е с 10% по-висока от цената на килограм брашно
# •	цената на един пакет мая е с 80% по-ниска от цената на килограм захар

# 1.	Цена на брашното за един килограм – реално число в интервала [0.00 … 10000.00]
# 2.	Килограми на брашното – реално число в интервала [0.00 … 10000.00]
# 3.	Килограми на захарта – реално число в интервала [0.00 … 10000.00]
# 4.	Брой кори с яйца – цяло число в интервала [0 … 10000]
# 5.	Пакети мая  – цяло число в интервала [0 … 10000]

price_of_flour = float(input())
number_of_flour = float(input())
quantity_of_sugar = float(input())
number_eggshels = int(input())
number_of_may_package = int(input())

price_of_sugar_for_kg = price_of_flour * 0.75
total_price_of_sugar = price_of_sugar_for_kg * quantity_of_sugar

total_price_for_all_eggs = number_eggshels * (price_of_flour * 1.10)

price_one_kg_may = price_of_sugar_for_kg * 0.20
total_price_of_may = price_one_kg_may * number_of_may_package

total_price_of_flour = number_of_flour * price_of_flour

necessary_sum = total_price_of_sugar + total_price_for_all_eggs + total_price_of_may + total_price_of_flour
print(f'{necessary_sum:.2f}')