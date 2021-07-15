import sys
town = input()
package = input()
vip_discount = input()
days = int(input())

price_per_day = 0
discount = 0

if town == "Bansko" or town == "Borovets":
    if package == "noEquipment":
        price_per_day = 80
        discount = 0.05
    elif package == "withEquipment":
        price_per_day = 100
        discount = 0.10
    else:
        print("Invalid input!")
        sys.exit(0)
elif town == "Varna" or town == "Burgas":
    if package == "noBreakfast":
        price_per_day = 100
        discount = 0.07
    elif package == "withBreakfast":
        price_per_day = 130
        discount = 0.12
    else:
        print("Invalid input!")
        sys.exit(0)
else:
    print("Invalid input!")
    sys.exit(0)

if vip_discount == "yes":
    price_per_day -= price_per_day * discount

if days > 7:
    days -= 1

total = price_per_day * days
if days > 0:
    print(f"The price is {total:.2f}lv! Have a nice time!")
else:
    print("Days must be positive number!")