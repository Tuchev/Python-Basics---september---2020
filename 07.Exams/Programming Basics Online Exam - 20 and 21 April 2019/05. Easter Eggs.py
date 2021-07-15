number_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

for egg in range(1, number_eggs + 1):
    egg_color = input()
    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    elif egg_color == "green":
        green_eggs += 1

max_eggs_count = red_eggs
max_color = "red"

if orange_eggs > max_eggs_count:
    max_eggs_count = orange_eggs
    max_color = "orange"

if blue_eggs > max_eggs_count:
    max_eggs_count = blue_eggs
    max_color = "blue"

if green_eggs > max_eggs_count:
    max_eggs_count = green_eggs
    max_color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs_count} -> {max_color}")