num_of_location = int(input())
total_sum_gold = 0

for location in range(1, num_of_location + 1):
    expected_average_yield = int(input())
    num_of_days = int(input())

    for day in range(1, num_of_days + 1):
        gold_mining = int(input())
        total_sum_gold += gold_mining
        if day == num_of_days:
            if total_sum_gold / num_of_days >= expected_average_yield:
                print(f"Good job! Average gold per day: {total_sum_gold / num_of_days:.2f}.")
            elif total_sum_gold / num_of_days < expected_average_yield:
                print(f"You need {expected_average_yield - (total_sum_gold / num_of_days):.2f} gold.")
            total_sum_gold = 0