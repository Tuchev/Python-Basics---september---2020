junior_cyclist = int(input())
senior_cyclists = int(input())
type_of_route = input() #"trail", "cross-country", "downhill" или "road"

amount_collected = 0

if type_of_route == "trail":
    amount_collected = (junior_cyclist * 5.50 + senior_cyclists * 7) * 0.95
elif type_of_route == "cross-country":
    if (junior_cyclist + senior_cyclists) >= 50:
        amount_collected = (junior_cyclist * 8 * 0.75 + senior_cyclists * 9.50 * 0.75) * 0.95
    else:
        amount_collected = (junior_cyclist * 8 + senior_cyclists * 9.50) * 0.95
elif type_of_route == "downhill":
    amount_collected = (junior_cyclist * 12.25 + senior_cyclists * 13.75) * 0.95
elif type_of_route == "road":
    amount_collected = (junior_cyclist * 20 + senior_cyclists * 21.5) * 0.95
print(f"{amount_collected:.2f}")