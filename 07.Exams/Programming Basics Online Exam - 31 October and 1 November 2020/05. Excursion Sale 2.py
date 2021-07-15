num_of_excursions_for_sea = int(input())
num_of_excursions_for_mountain = int(input())

count_of_excursions_for_sea = 0
count_of_excursions_for_mountain = 0
total_sum = 0

command = input()
while command != "Stop":
    if command == "sea":
        count_of_excursions_for_sea += 1
        if num_of_excursions_for_sea >= count_of_excursions_for_sea:
            total_sum += 680
    elif command == "mountain":
        count_of_excursions_for_mountain += 1
        if num_of_excursions_for_mountain >= count_of_excursions_for_mountain:
            total_sum += 499
    if count_of_excursions_for_sea >= num_of_excursions_for_sea and count_of_excursions_for_mountain >= num_of_excursions_for_mountain:
        print("Good job! Everything is sold.")
        break
    command = input()
print(f"Profit: {total_sum} leva.")