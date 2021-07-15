from math import floor
from math import ceil

days = int(input())
food = int(input())
food_for_dog_kg = float(input())
food_for_cat_kg = float(input())
food_for_turtle_grams = float(input())

food_for_turtle_kg = food_for_turtle_grams / 1000

total_necessary_food = food_for_dog_kg * days + food_for_cat_kg * days + food_for_turtle_kg * days
difference_of_food = abs(food - total_necessary_food)

if total_necessary_food <= food:
    print(f'{floor(difference_of_food)} kilos of food left.')
else:
    print(f'{ceil(difference_of_food)} more kilos of food are needed.')