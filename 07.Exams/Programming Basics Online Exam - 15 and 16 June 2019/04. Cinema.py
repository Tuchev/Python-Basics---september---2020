capacity = int(input())
command = input()
ticket_price = 5

people_count = 0
rest_place = 0
group_sum = 0
total_sum = 0

is_full = False

while command != "Movie time!":
    people_count += int(command)
    rest_place = capacity - people_count
    group_sum = int(command) * ticket_price
    if int(command) % 3 == 0:
        group_sum -= 5
    total_sum += group_sum

    if people_count > capacity:
        total_sum -= group_sum
        is_full = True
        break
    command = input()
if is_full:
    print("The cinema is full.")
elif command == "Movie time!":
    print(f"There are {rest_place} seats left in the cinema.")
print(f"Cinema income - {total_sum} lv.")