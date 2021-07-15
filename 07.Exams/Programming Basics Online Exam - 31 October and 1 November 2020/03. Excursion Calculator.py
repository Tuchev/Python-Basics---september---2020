num_persons = int(input())
season = input()
price = 0

if season == "spring":
    if num_persons <= 5:
        price = 50
    else:
        price = 48
elif season == "summer":
    if num_persons <= 5:
        price = 48.50 * 0.85
    else:
        price = 45.00 * 0.85
elif season == "autumn":
    if num_persons <= 5:
        price = 60
    else:
        price = 49.50
elif season == "winter":
    if num_persons <= 5:
        price = 86.00 * 1.08
    else:
        price = 85.00 * 1.08

total_sum = num_persons * price
print(f"{total_sum:.2f} leva.")