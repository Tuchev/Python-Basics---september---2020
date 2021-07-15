#бензин = 2.22 лева за литър
#дизел = 2.33 лева за литър
#газ = 0.93 лева за литър

#карта за отстъпка - бензин - 18ст., дизел - 12ст. газ - 8ст.

#ако зареденото количество е между 20 и 25 литра, включително - 8% отстъпка от крайната цена;
#ако зареденото количество е повече от 25 литра - 10% отстъпка от крайната цена;

type_fuel = input()
quantity_fuel = float(input())
discount_card = input()

price_of_gasoline = quantity_fuel * 2.22
price_of_diesel = quantity_fuel * 2.33
price_of_gas = quantity_fuel * 0.93

price_of_gasoline_with_card = price_of_gasoline - 0.18 * quantity_fuel
price_of_diesel_with_card = price_of_diesel - 0.12 * quantity_fuel
price_of_gas_with_card = price_of_gas - 0.08 * quantity_fuel

if quantity_fuel < 20 and discount_card == "No" and type_fuel == "Gasoline":
    print(f'{price_of_gasoline:.2f} lv.')
elif quantity_fuel < 20 and discount_card == "No" and type_fuel == "Diesel":
    print(f'{price_of_diesel:.2f} lv.')
elif quantity_fuel < 20 and discount_card == "No" and type_fuel == "Gas":
    print(f'{price_of_gas:.2f} lv.')

if quantity_fuel < 20 and discount_card == "Yes" and type_fuel == "Gasoline":
    print(f'{price_of_gasoline_with_card:.2f} lv.')
elif quantity_fuel < 20 and discount_card == "Yes" and type_fuel == "Diesel":
    print(f'{price_of_diesel_with_card:.2f} lv.')
elif quantity_fuel < 20 and discount_card == "Yes" and type_fuel == "Gas":
    print(f'{price_of_gas_with_card:.2f} lv.')

if 20 <= quantity_fuel <= 25 and discount_card == "No" and type_fuel == "Gasoline":
    print(f'{(price_of_gasoline * 0.92):.2f} lv.')
elif 20 <= quantity_fuel <= 25 and discount_card == "No" and type_fuel == "Diesel":
    print(f'{(price_of_diesel * 0.92):.2f} lv.')
elif 20 <= quantity_fuel <= 25 and discount_card == "No" and type_fuel == "Gas":
    print(f'{(price_of_gas * 0.92):.2f} lv.')

if 20 <= quantity_fuel <= 25 and discount_card == "Yes" and type_fuel == "Gasoline":
    print(f'{(price_of_gasoline_with_card * 0.92):.2f} lv.')
elif 20 <= quantity_fuel <= 25 and discount_card == "Yes" and type_fuel == "Diesel":
    print(f'{(price_of_diesel_with_card * 0.92):.2f} lv.')
elif 20 <= quantity_fuel <= 25 and discount_card == "Yes" and type_fuel == "Gas":
    print(f'{(price_of_gas_with_card * 0.92):.2f} lv.')

if quantity_fuel > 25 and discount_card == "No" and type_fuel == "Gasoline":
    print(f'{(price_of_gasoline * 0.90):.2f} lv.')
elif quantity_fuel > 25 and discount_card == "No" and type_fuel == "Diesel":
    print(f'{(price_of_diesel * 0.90):.2f} lv.')
elif quantity_fuel > 25 and discount_card == "No" and type_fuel == "Gas":
    print(f'{(price_of_gas * 0.90):.2f} lv.')

if quantity_fuel > 25 and discount_card == "Yes" and type_fuel == "Gasoline":
    print(f'{(price_of_gasoline_with_card * 0.90):.2f} lv.')
elif quantity_fuel > 25 and discount_card == "Yes" and type_fuel == "Diesel":
    print(f'{(price_of_diesel_with_card * 0.90):.2f} lv.')
elif quantity_fuel > 25 and discount_card == "Yes" and type_fuel == "Gas":
    print(f'{(price_of_gas_with_card * 0.90):.2f} lv.')