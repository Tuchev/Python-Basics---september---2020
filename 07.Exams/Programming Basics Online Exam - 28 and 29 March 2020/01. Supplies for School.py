# •	Пакет химикали - 5.80 лв
# •	Пакет маркери - 7.20 лв
# •	Препарат - 1.20 лв (за литър)

number_pens = int(input())
number_markers = int(input())
detergent = float(input())
discount_rate = int(input())

total_sum = number_pens * 5.80 + number_markers * 7.20 + detergent * 1.20 - ((number_pens * 5.80 + number_markers * 7.20 + detergent * 1.200) * discount_rate / 100)
print(f'{total_sum:.3f}')