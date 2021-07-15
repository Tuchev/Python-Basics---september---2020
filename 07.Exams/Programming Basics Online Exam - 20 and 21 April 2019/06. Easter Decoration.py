num_of_clients = int(input())
num_of_products = 0
price = 0
total_price = 0
total_sum_for_all_client = 0


for client in range(1, num_of_clients + 1):
    total_price = 0
    num_of_products = 0
    command = input()
    while command != "Finish":
        num_of_products += 1
        if command == "basket":
            price = 1.50
            total_price += price
        elif command == "wreath":
            price = 3.80
            total_price += price
        elif command == "chocolate bunny":
            price = 7
            total_price += price
        command = input()
    if num_of_products % 2 == 0:
        total_price *= 0.8
    total_sum_for_all_client += total_price
    print(f"You purchased {num_of_products} items for {total_price:.2f} leva.")
average_sum = total_sum_for_all_client / num_of_clients
print(f"Average bill per client is: {average_sum:.2f} leva.")