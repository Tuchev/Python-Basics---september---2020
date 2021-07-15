num_of_cats = int(input())

count_of_small_cats = 0
count_of_big_cats = 0
count_of_bigger_cats = 0
total_food = 0

for cat in range(1, num_of_cats + 1):
    food = int(input())
    if 100 <= food < 200:
        count_of_small_cats += 1
        total_food += food
    elif 200 <= food < 300:
        count_of_big_cats += 1
        total_food += food
    elif 300 <= food < 400:
        count_of_bigger_cats += 1
        total_food += food

total_food_kg = total_food / 1000
price_for_food = total_food_kg * 12.45
print(f"Group 1: {count_of_small_cats}")
print(f"Group 2: {count_of_big_cats}")
print(f"Group 3: {count_of_bigger_cats}")
print(f"Price for food per day: {price_for_food:.2f} lv.")