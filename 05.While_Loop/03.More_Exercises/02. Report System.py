required_money = int(input())
product = 0
sum_odd = 0
average_product_odd = 0
sum_even = 0
average_product_even = 0

while True:
    command = input()
    product += 1
    if command == "End":
        break
    if product % 2 == 1:
        if int(command) > 100:
            print("Error in transaction!")
        else:
            sum_even += int(command)
            average_product_even += 1
            print("Product sold!")
    if product % 2 == 0:
        if int(command) <= 10:
            print("Error in transaction!")
        else:
            sum_odd += int(command)
            average_product_odd += 1
            print("Product sold!")
    if (sum_odd + sum_even) >= required_money:
        break

if (sum_odd + sum_even) >= required_money:
    print(f"Average CS: {(sum_even / average_product_even):.2f}")
    print(f"Average CC: {(sum_odd / average_product_odd):.2f}")
else:
    print("Failed to collect required money for charity.")