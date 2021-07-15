eggs_in_shop = int(input())
command = input()
total_eggs_sold = 0

while command != "Close":
    if command == "Buy":
        command = input()
        if int(command) > eggs_in_shop:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_in_shop}.")
            break
        eggs_in_shop -= int(command)
        total_eggs_sold += int(command)
    elif command == "Fill":
        command = input()
        eggs_in_shop += int(command)
    command = input()

if command == "Close":
    print("Store is closed!")
    print(f"{total_eggs_sold} eggs sold.")