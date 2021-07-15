total_food_kg = int(input())
total_food_grams = total_food_kg * 1000
sum_of_eated_food = 0
command = input()

while command != "Adopted":
    sum_of_eated_food += int(command)
    command = input()

diff = abs(total_food_grams - sum_of_eated_food)
if total_food_grams >= sum_of_eated_food:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")