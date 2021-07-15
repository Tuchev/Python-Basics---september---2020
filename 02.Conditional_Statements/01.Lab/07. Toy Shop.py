puzzle = 2.60
talking_doll = 3
bear = 4.10
minion = 8.20
truck = 2
price_of_vacation = float(input())
number_of_puzzle = int(input())
number_of_talking_doll = int(input())
number_of_bear = int(input())
number_of_minion = int(input())
number_of_truck = int(input())
profit = puzzle * number_of_puzzle + talking_doll * number_of_talking_doll + bear * number_of_bear + minion * number_of_minion + truck * number_of_truck
all_toy = number_of_puzzle + number_of_talking_doll + number_of_bear + number_of_minion + number_of_truck
if all_toy >= 50:
    profit = profit - (profit * 0.25)
profit = profit - (profit * 0.10)
if profit >= price_of_vacation:
    money_lef = profit - price_of_vacation
    print(f'Yes!{money_lef: .2f} lv left.')
elif profit < price_of_vacation:
    money_need = price_of_vacation - profit
    print(f'Not enough money!{money_need: .2f} lv needed.')


