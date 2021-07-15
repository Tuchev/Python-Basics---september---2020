term_of_the_contract = input()
type_of_contract = input()
internet = input()
num_of_months = int(input())
price = 0

if term_of_the_contract == "one":
    if type_of_contract == "Small":
        price = 9.98
        if internet == "yes":
            price = 9.98 + 5.50
    elif type_of_contract == "Middle":
        price = 18.99
        if internet == "yes":
            price = 18.99 + 4.35
    elif type_of_contract == "Large":
        price = 25.98
        if internet == "yes":
            price = 25.98 + 4.35
    elif type_of_contract == "ExtraLarge":
        price == 35.99
        if internet == "yes":
            price = 35.99 + 3.85
elif term_of_the_contract == "two":
    if type_of_contract == "Small":
        price = 8.58 * 0.9625
        if internet == "yes":
            price = (8.58 + 5.50) * 0.9625
    elif type_of_contract == "Middle":
        price = 17.09 * 0.9625
        if internet == "yes":
            price = (17.09 + 4.35) * 0.9625
    elif type_of_contract == "Large":
        price = 23.59 * 0.9625
        if internet == "yes":
            price = (23.59 + 4.35) * 0.9625
    elif type_of_contract == "ExtraLarge":
        price = 31.79 * 0.9625
        if internet == "yes":
            price = (31.79 + 3.85) * 0.9625

total_price = num_of_months * price
print(f"{total_price:.2f} lv.")