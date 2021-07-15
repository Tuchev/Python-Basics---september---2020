budget = float(input())
num_of_cards = int(input())
num_of_processors = int(input())
num_of_ram = int(input())

price_of_cards = num_of_cards * 250
price_of_processors = num_of_processors * (0.35 * price_of_cards)
price_of_ram = num_of_ram * (0.10 * price_of_cards)

total = price_of_ram + price_of_cards +price_of_processors

if num_of_cards > num_of_processors:
    total -= total * 0.15
diff = abs(budget - total)
if budget >= total:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")