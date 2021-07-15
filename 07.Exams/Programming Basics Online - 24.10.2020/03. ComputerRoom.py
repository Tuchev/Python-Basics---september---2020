month = input()
num_of_hours = int(input())
num_of_people = int(input())
time_of_day = input()

price = 0

if month == "march" or month == "april" or month == "may":
    if time_of_day == "day":
        price = 10.50
    elif time_of_day == "night":
        price = 8.40
elif month == "june" or month == "july" or month == "august":
    if time_of_day == "day":
        price = 12.60
    elif time_of_day == "night":
        price = 10.20
if num_of_people >= 4:
    price *= 0.9
if num_of_hours >= 5:
    price *= 0.5

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {num_of_people * num_of_hours * price:.2f}")