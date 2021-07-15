inherited_money = float(input())
year = int(input())
year_of_Ivan = 18

for i in range(1800, year +1):
    if i % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + 50 * year_of_Ivan
    year_of_Ivan += 1

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {abs(inherited_money):.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")