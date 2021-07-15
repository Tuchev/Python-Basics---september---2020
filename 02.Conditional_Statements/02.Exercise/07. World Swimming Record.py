import math

record_in_second = float(input())
distance_in_meter = float(input())
time_to_swim_one_meter = float(input())

necessary_time = distance_in_meter * time_to_swim_one_meter
delay = (math.floor(distance_in_meter / 15) * 12.5)
total_time = necessary_time + delay
if total_time < record_in_second:
    print(f" Yes, he succeeded! The new world record is{total_time: .2f} seconds.")
else:
    time_needed = total_time - record_in_second
    print(f"No, he failed! He was{time_needed: .2f} seconds slower.")
