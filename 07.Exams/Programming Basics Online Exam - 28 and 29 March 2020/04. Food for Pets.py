number_day = int(input())
total_quantity_food = float(input())

total_dog_food = 0
total_cat_food = 0
biscuits = 0

for day in range(1, number_day + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_dog_food += dog_food
    total_cat_food += cat_food
    if day % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.10

total_eaten_food = total_dog_food + total_cat_food
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{(total_eaten_food / total_quantity_food * 100):.2f}% of the food has been eaten.")
print(f"{(total_dog_food / total_eaten_food * 100):.2f}% eaten from the dog.")
print(f"{(total_cat_food / total_eaten_food * 100):.2f}% eaten from the cat.")