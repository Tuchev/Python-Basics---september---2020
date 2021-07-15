volume_of_pool = int(input())
first_pipe_flow = int(input())
second_pipe_flow = int(input())
hours_of_absent = float(input())

total_debit_first_pipe = first_pipe_flow * hours_of_absent
total_debit_second_pipe = second_pipe_flow * hours_of_absent

total_water_in_pool = total_debit_first_pipe + total_debit_second_pipe
percentage_of_water_in_pool = total_water_in_pool / volume_of_pool * 100
percentage_of_first_pipe = total_debit_first_pipe / total_water_in_pool * 100
percentage_of_second_pipe = total_debit_second_pipe / total_water_in_pool * 100
water_outside_pool = total_water_in_pool - volume_of_pool

if total_water_in_pool <= volume_of_pool:
    print(f'The pool is {percentage_of_water_in_pool:.2f}% full. Pipe 1: {percentage_of_first_pipe:.2f}%. Pipe 2: {percentage_of_second_pipe:.2f}%.')
else:
    print(f'For {hours_of_absent:.2f} hours the pool overflows with {water_outside_pool} liters.')