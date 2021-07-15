name_of_actor = input()
point_of_academy = float(input())
n = int(input())

point_after_evaluat = 0
total_points = 0
is_nominee = False

for evaluating in range(1, n + 1):
    evaluat = input()
    point_of_evaluat = float(input())
    if evaluating <= 1:
        point_for_actor = (len(evaluat) * point_of_evaluat) / 2
        point_after_evaluat = point_of_academy + point_for_actor
        total_points += point_after_evaluat
    else:
        point_for_actor = (len(evaluat) * point_of_evaluat) / 2
        total_points += point_for_actor
    if total_points >= 1250.5:
        is_nominee = True
        break
if is_nominee:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {(1250.5 - total_points):.1f} more!")