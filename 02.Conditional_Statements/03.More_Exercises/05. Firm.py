from math import floor
time_needed = int(input())
number_of_day = int(input())
number_of_employees = int(input())


time_for_job_in_hours = number_of_day * 0.90 * 8
overtime_in_hours = number_of_employees * 2 * number_of_day

total_time = floor(time_for_job_in_hours + overtime_in_hours)
time_left = abs(total_time - time_needed)


if total_time >= time_needed:
    print(f'Yes!{time_left} hours left.')
else:
    print(f'Not enough time!{time_left} hours needed.')