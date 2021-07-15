budget = float(input())
type_of_ticket = input() #VIP, Normal
number_of_persons = int(input())

sum_for_transport = 0
price_of_ticket = 0
difference = 0
rest_money = 0

#•	VIP – 499.99 лева.
#•	Normal – 249.99 лева.

# •	От 1 до 4 – 75% от бюджета.
# •	От 5 до 9 – 60% от бюджета.
# •	От 10 до 24 – 50% от бюджета.
# •	От 25 до 49 – 40% от бюджета.
# •	50 или повече – 25% от бюджета.

# Да се отпечата на конзолата един ред:
# •	Ако бюджетът е достатъчен:
# o	"Yes! You have {останалите пари на групата} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# o	"Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.

if 1 <= number_of_persons <=4 and type_of_ticket == "VIP":
    price_of_ticket = 499.99
    sum_for_transport = budget * 0.75
    difference = budget - sum_for_transport
    rest_money = abs(difference - number_of_persons * price_of_ticket)
    if budget >= (sum_for_transport + number_of_persons * price_of_ticket):
        print(f"Yes! You have {rest_money:.2f} leva left.")
    else:
        print(f"Not enough money! You need {rest_money:.2f} leva.")
elif 1 <= number_of_persons <=4 and type_of_ticket == "Normal":
        price_of_ticket = 249.99
        sum_for_transport = budget * 0.75
        difference = budget - sum_for_transport
        rest_money = abs(difference - number_of_persons * price_of_ticket)
        if budget >= (sum_for_transport + number_of_persons * price_of_ticket):
            print(f"Yes! You have {rest_money:.2f} leva left.")
        else:
            print(f"Not enough money! You need {rest_money:.2f} leva.")
elif 5 <= number_of_persons <= 9 and type_of_ticket == "VIP":
    price_of_ticket = 499.99
    sum_for_transport = budget * 0.60
    difference = budget - sum_for_transport
    rest_money = abs(difference - number_of_persons * price_of_ticket)
    if budget >= (sum_for_transport + number_of_persons * price_of_ticket):
        print(f"Yes! You have {rest_money:.2f} leva left.")
    else:
        print(f"Not enough money! You need {rest_money:.2f} leva.")
elif 5 <= number_of_persons <= 9 and type_of_ticket == "Normal":
    price_of_ticket = 249.99
    sum_for_transport = budget * 0.60
    difference = budget - sum_for_transport
    rest_money = abs(difference - number_of_persons * price_of_ticket)
    if budget >= (sum_for_transport + number_of_persons * price_of_ticket):
        print(f"Yes! You have {rest_money:.2f} leva left.")
    else:
        print(f"Not enough money! You need {rest_money:.2f} leva.")
elif 10 <= number_of_persons <= 24 and type_of_ticket == "VIP":
    price_of_ticket = 499.99
    sum_for_transport = budget * 0.50
    difference = budget - sum_for_transport
    rest_money = abs(difference - number_of_persons * price_of_ticket)
    if budget >= (sum_for_transport + number_of_persons * price_of_ticket):
        print(f"Yes! You have {rest_money:.2f} leva left.")
    else:
        print(f"Not enough money! You need {rest_money:.2f} leva.")
elif 10 <= number_of_persons <= 24 and type_of_ticket == "Normal":
    price_of_ticket = 249.99
    sum_for_transport = budget * 0.60
    difference = budget - sum_for_transport
    rest_money = abs(difference - number_of_persons * price_of_ticket)
    if budget >= (sum_for_transport + number_of_persons * price_of_ticket):
        print(f"Yes! You have {rest_money:.2f} leva left.")
    else:
        print(f"Not enough money! You need {rest_money:.2f} leva.")
elif 25 <= number_of_persons <= 49 and type_of_ticket == "VIP":
    price_of_ticket = 499.99
    sum_for_transport = budget * 0.40
    difference = budget - sum_for_transport
    rest_money = abs(difference - number_of_persons * price_of_ticket)
    if budget >= (sum_for_transport + number_of_persons * price_of_ticket):
        print(f"Yes! You have {rest_money:.2f} leva left.")
    else:
        print(f"Not enough money! You need {rest_money:.2f} leva.")
elif 10 <= number_of_persons <= 24 and type_of_ticket == "Normal":
    price_of_ticket = 249.99
    sum_for_transport = budget * 0.40
    difference = budget - sum_for_transport
    rest_money = abs(difference - number_of_persons * price_of_ticket)
    if budget >= (sum_for_transport + number_of_persons * price_of_ticket):
        print(f"Yes! You have {rest_money:.2f} leva left.")
    else:
        print(f"Not enough money! You need {rest_money:.2f} leva.")
elif number_of_persons >= 50 and type_of_ticket == "VIP":
    price_of_ticket = 499.99
    sum_for_transport = budget * 0.25
    difference = budget - sum_for_transport
    rest_money = abs(difference - number_of_persons * price_of_ticket)
    if budget >= (sum_for_transport + number_of_persons * price_of_ticket):
        print(f"Yes! You have {rest_money:.2f} leva left.")
    else:
        print(f"Not enough money! You need {rest_money:.2f} leva.")
elif number_of_persons >= 50 and type_of_ticket == "Normal":
    price_of_ticket = 249.99
    sum_for_transport = budget * 0.25
    difference = budget - sum_for_transport
    rest_money = abs(difference - number_of_persons * price_of_ticket)
    if budget >= (sum_for_transport + number_of_persons * price_of_ticket):
        print(f"Yes! You have {rest_money:.2f} leva left.")
    else:
        print(f"Not enough money! You need {rest_money:.2f} leva.")