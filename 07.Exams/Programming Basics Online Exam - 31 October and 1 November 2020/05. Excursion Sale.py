num_of_days = int(input())

dayly_limit = 60
cost = 0
rest_money = 0

for day in range(1, num_of_days + 1):
    count_of_products = 0
    command = input()
    while command != "Day over":
        cost += int(command)
        count_of_products += 1
        if int(command) >= dayly_limit:
            cost -= int(command)
            count_of_products -= 1
            command = input()
            continue
        if cost >= dayly_limit:
            print(f"Daily limit exceeded! You've bought {count_of_products} products.")
            count_of_products = 0
            cost = 0
            break
        command = input()
    if command == "Day over":
        rest_money = dayly_limit - cost
        dayly_limit += rest_money
        cost = 0
        print(f"Money left from today: {rest_money:.2f}. You've bought {count_of_products} products.")