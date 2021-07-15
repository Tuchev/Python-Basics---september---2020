capacity = float(input())
count = 0
command = input()
while command != "End":
    suitcase_volume = float(command)
    count += 1
    if count % 3 == 0:
        suitcase_volume += suitcase_volume * 0.1
    capacity -= suitcase_volume
    if capacity < 0:
        print("No more space!")
        count -= 1
        break
    command = input()
if command == "End":
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {count} suitcases loaded.")