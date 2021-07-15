needed_money = float(input())
money_in_hand = float(input())
consecutive_days = 0
past_days = 0
while True:
    command = input()
    sum = float(input())
    past_days += 1
    if command == "spend":
        money_in_hand -= sum
        if money_in_hand < 0:
            money_in_hand = 0
        consecutive_days += 1
        if consecutive_days == 5:
            break
    elif command == "save":
        money_in_hand += sum
        if money_in_hand >= needed_money:
            break
        consecutive_days = 0
if money_in_hand >= needed_money:
    print(f"You saved the money for {past_days} days.")
else:
    print("You can't save the money.")
    print(past_days)