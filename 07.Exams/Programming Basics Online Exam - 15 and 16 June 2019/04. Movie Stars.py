budget = float(input())
command = input()
is_budget_off = False

while command != "ACTION":
    if len(command) <= 15:
        salary_of_actor = float(input())
        if salary_of_actor > budget:
            is_budget_off = True
            diff = abs(budget - salary_of_actor)
            break
        budget -= salary_of_actor
    else:
        budget *= 0.8
    command = input()
if is_budget_off:
    print(f"We need {diff:.2f} leva for our actors.")
elif budget > 0:
    print(f"We are left with {budget:.2f} leva.")