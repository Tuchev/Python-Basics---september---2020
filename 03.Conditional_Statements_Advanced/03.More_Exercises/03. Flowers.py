number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
day = input()

total_number_of_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
total_sum = 0

if season == "Spring" and day == "Y":
    total_sum = (number_of_chrysanthemums * 2 + number_of_roses * 4.1 + number_of_tulips * 2.5) * 1.15
    if number_of_tulips > 7 and total_number_of_flowers > 20:
        total_sum = (total_sum * 0.95) * 0.8
    elif number_of_tulips > 7 and total_number_of_flowers <= 20:
        total_sum *= 0.95
    elif number_of_tulips <= 7 and total_number_of_flowers > 20:
        total_sum *= 0.8
elif season == "Spring" and day == "N":
    total_sum = (number_of_chrysanthemums * 2 + number_of_roses * 4.1 + number_of_tulips * 2.5)
    if number_of_tulips > 7 and total_number_of_flowers > 20:
        total_sum = (total_sum * 0.95) * 0.8
    elif number_of_tulips > 7 and total_number_of_flowers <= 20:
        total_sum *= 0.95
    elif number_of_tulips <= 7 and total_number_of_flowers > 20:
        total_sum *= 0.8
elif season == "Summer" and day == "Y":
    total_sum = (number_of_chrysanthemums * 2 + number_of_roses * 4.1 + number_of_tulips * 2.5) * 1.15
    if total_number_of_flowers > 20:
        total_sum *= 0.80
elif season == "Summer" and day == "N":
    total_sum = (number_of_chrysanthemums * 2 + number_of_roses * 4.1 + number_of_tulips * 2.5)
    if total_number_of_flowers > 20:
        total_sum *= 0.80
elif season == "Autumn" and day == "Y":
    total_sum = (number_of_chrysanthemums * 3.75 + number_of_roses * 4.50 + number_of_tulips * 4.15) * 1.15
    if total_number_of_flowers > 20:
        total_sum *= 0.80
elif season == "Autumn" and day == "N":
    total_sum = (number_of_chrysanthemums * 3.75 + number_of_roses * 4.50 + number_of_tulips * 4.15)
    if total_number_of_flowers > 20:
        total_sum *= 0.80
elif season == "Winter" and day == "Y":
    total_sum = (number_of_chrysanthemums * 3.75 + number_of_roses * 4.50 + number_of_tulips * 4.15) * 1.15
    if number_of_roses >= 10 and total_number_of_flowers > 20:
        total_sum = (total_sum * 0.90) * 0.80
    elif number_of_roses >= 10 and total_number_of_flowers <= 20:
        total_sum *= 0.90
    elif number_of_roses < 10 and total_number_of_flowers > 20:
        total_sum *= 0.80
elif season == "Winter" and day == "N":
    total_sum = (number_of_chrysanthemums * 3.75 + number_of_roses * 4.50 + number_of_tulips * 4.15)
    if number_of_roses >= 10 and total_number_of_flowers > 20:
        total_sum = (total_sum * 0.90) * 0.80
    elif number_of_roses >= 10 and total_number_of_flowers <= 20:
        total_sum *= 0.90
    elif number_of_roses < 10 and total_number_of_flowers > 20:
        total_sum *= 0.80

total_sum = total_sum + 2
print(f"{total_sum:.2f}")