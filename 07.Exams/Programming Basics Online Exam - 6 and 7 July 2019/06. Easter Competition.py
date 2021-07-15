num_of_easter_bread = int(input())
max_points = 0
best_baker = ""
for easter_bread in range(num_of_easter_bread):
    backer_name = input()
    total_points = 0
    command = input()
    while command != "Stop":
        grade = int(command)
        total_points += grade
        command = input()
    print(f"{backer_name} has {total_points} points.")
    if total_points > max_points:
        max_points = total_points
        best_baker = backer_name
        print(f"{backer_name} is the new number 1!")
print(f"{best_baker} won competition with {max_points} points!")