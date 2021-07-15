from math import floor
world_record = float(input())
distance = float(input())
time_for_one_meter = float(input())

time_for_distance = distance * time_for_one_meter
number_for_delay = floor(distance / 50)
delay = number_for_delay * 30
total_time = time_for_distance + delay

if total_time < world_record:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {abs(world_record - total_time):.2f} seconds slower.')