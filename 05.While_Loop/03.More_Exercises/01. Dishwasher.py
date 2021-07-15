quantity_detergent = int(input())

total_detergent = quantity_detergent * 750
total_dishes = 0
total_pots = 0
cycle = 0
detergent_for_dishes = 0
detergent_for_pots = 0

while True:
    command = input()
    cycle += 1
    if command == "End":
        break
    else:
        if cycle % 3 == 0:
            total_pots += int(command)
            detergent_for_pots = total_pots * 15
        else:
            total_dishes += int(command)
            detergent_for_dishes = total_dishes * 5
    if total_detergent < (detergent_for_dishes + detergent_for_pots):
        break

if total_detergent >= (detergent_for_dishes + detergent_for_pots):
    print("Detergent was enough!")
    print(f"{total_dishes} dishes and {total_pots} pots were washed.")
    print(f"Leftover detergent {total_detergent - detergent_for_dishes - detergent_for_pots} ml.")
else:
    print(f"Not enough detergent, {abs(total_detergent - detergent_for_dishes - detergent_for_pots)} ml. more necessary!")