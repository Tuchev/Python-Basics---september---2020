month = input() #May, June, July, August, September или October
overnight = int(input())

price_of_studio = 0
price_of_apartment = 0

if overnight <= 7:
    if month == "May" or month == "October":
        price_of_studio = 50
        price_of_apartment = 65
    elif month == "June" or month == "September":
        price_of_studio = 75.20
        price_of_apartment = 68.70
    elif month == "July" or month == "August":
        price_of_studio = 76
        price_of_apartment = 77
elif 7 < overnight <= 14:
    if month == "May" or month == "October":
        price_of_studio = 50 * 0.95
        price_of_apartment = 65
    elif month == "June" or month == "September":
        price_of_studio = 75.20
        price_of_apartment = 68.70
    elif month == "July" or month == "August":
        price_of_studio = 76
        price_of_apartment = 77
elif overnight > 14:
    if month == "May" or month == "October":
        price_of_studio = 50 * 0.70
        price_of_apartment = 65 * 0.90
    elif month == "June" or month == "September":
        price_of_studio = 75.20 * 0.80
        price_of_apartment = 68.70 * 0.90
    elif month == "July" or month == "August":
        price_of_studio = 76
        price_of_apartment = 77 * 0.90
total_price_of_studio = overnight * price_of_studio
total_price_of_apartment = overnight * price_of_apartment
print(f"Apartment: {total_price_of_apartment:.2f} lv.")
print(f"Studio: {total_price_of_studio:.2f} lv.")