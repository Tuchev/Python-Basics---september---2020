from math import floor
width = float(input())
length = float(input())
height = float(input())
average_height_of_astronauts = float(input())

total_volume_of_rocket = width * length * height

volume_for_one_room = 2 * 2 * (average_height_of_astronauts + 0.40)

total_peoples = floor(total_volume_of_rocket / volume_for_one_room)

if 3 <= total_peoples <= 10:
    print(f"The spacecraft holds {total_peoples} astronauts.")
elif total_peoples < 3:
    print("The spacecraft is too small.")
elif total_peoples > 10:
    print("The spacecraft is too big.")