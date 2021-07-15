command = input()
total_sum = 0
while command != "NoMoreMoney":
    if int(float(command)) < 0:
        print(f"Invalid operation!")
        break
    total_sum += float(command)
    print(f"Increase: {float(command):.2f}")
    command = input()
print(f"Total: {total_sum:.2f}")