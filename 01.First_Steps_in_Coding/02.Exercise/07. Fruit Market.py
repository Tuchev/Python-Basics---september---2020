#•	цената на  малините е на половина по-ниска от тази на ягодите;
#•	цената на портокалите е с 40% по-ниска от цената на малините;
#•	цената на бананите е с 80% по-ниска от цената на малините.

price_of_berries = float(input())
number_of_bananas = float(input())
number_of_portocals = float(input())
number_of_raspberries = float(input())
number_of_berries = float(input())
price_of_raspberries = price_of_berries * 0.5
price_of_portocals = price_of_raspberries - (price_of_raspberries * 0.4)
price_of_bananas = price_of_raspberries - (price_of_raspberries * 0.8)
sum_for_raspberries = price_of_raspberries * number_of_raspberries
sum_for_portocal = price_of_portocals * number_of_portocals
sum_for_bananas = price_of_bananas * number_of_bananas
sum_for_berries = price_of_berries * number_of_berries
total_sum = sum_for_bananas + sum_for_berries + sum_for_portocal + sum_for_raspberries
print(total_sum)