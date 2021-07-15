hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

hour_of_exam_in_minutes = hour_of_exam * 60
hour_of_arrival_in_minutes = hour_of_arrival * 60

total_time_of_exam = hour_of_exam_in_minutes + minute_of_exam
total_time_of_arrival = hour_of_arrival_in_minutes + minute_of_arrival
difference = abs(total_time_of_arrival - total_time_of_exam)

if total_time_of_arrival < total_time_of_exam - 30:
    print("Early")
    if difference // 60 < 1:
        print(f"{difference % 60} minutes before the start")
    elif difference % 60 < 10:
        print(f"{difference // 60}:0{difference % 60} hours before the start")
    else:
        print(f"{difference // 60}:{difference % 60} hours before the start")
elif total_time_of_arrival >= total_time_of_exam - 30 and total_time_of_arrival <= total_time_of_exam:
    if difference == 0:
        print("On time")
    elif difference != 0:
        print("On time")
        print(f"{difference % 60} minutes before the start")
elif total_time_of_arrival > total_time_of_exam:
    print("Late")
    if difference // 60 < 1:
        print(f"{difference % 60} minutes after the start")
    elif difference % 60 < 10:
        print(f"{difference // 60}:0{difference % 60} hours after the start")
    else:
        print(f"{difference // 60}:{difference % 60} hours after the start")