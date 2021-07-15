num_of_people = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

for person in range(num_of_people):
    activity = input()
    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs += 1
    elif activity == "Protein shake":
        protein_shake += 1
    elif activity == "Protein bar":
        protein_bar += 1

workouters = back + abs + chest + legs
product_buyers = protein_bar + protein_shake

workouters_percentage = workouters / num_of_people * 100
product_buyers_percentage = product_buyers / num_of_people * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{workouters_percentage:.2f}% - work out")
print(f"{product_buyers_percentage:.2f}% - protein")
