# •	Козунак  – 3.20 лв.
# •	Яйца –  4.35 лв. за кора с 12 яйца
# •	Курабии – 5.40 лв. за килограм
# •	Боя за яйца - 0.15 лв. за яйце

# •	Брой козунаци - цяло число в интервала [0 … 99]
# •	Брой кори с яйца - цяло число в интервала [0 … 99]
# •	Килограми курабии - цяло число в интервала [0 … 99]

number_easter_bread = int(input())
number_eggshell = int(input())
cookies_kg = int(input())

price_of_easter_bread = number_easter_bread * 3.20
price_of_cookies = cookies_kg * 5.40
total_number_eggs = number_eggshell * 12
total_price_of_eggs = (number_eggshell * 4.35) + (total_number_eggs * 0.15)
total_sum = price_of_easter_bread + price_of_cookies + total_price_of_eggs
print(f'{total_sum:.2f}')