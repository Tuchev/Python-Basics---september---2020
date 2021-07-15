current_hours = int(input())
current_minutes = int(input())
current_time_in_minutes = current_hours * 60 + current_minutes
time_after_fifteen_minutes = current_time_in_minutes + 15
hours_after_fifteen_minutes = time_after_fifteen_minutes // 60
minutes_after_fifteen_minutes = time_after_fifteen_minutes % 60
if hours_after_fifteen_minutes > 23:
    hours_after_fifteen_minutes -= 24
if minutes_after_fifteen_minutes < 10:
    print(f'{hours_after_fifteen_minutes}:0{minutes_after_fifteen_minutes}')
else:
    print(f'{hours_after_fifteen_minutes}:{minutes_after_fifteen_minutes}')