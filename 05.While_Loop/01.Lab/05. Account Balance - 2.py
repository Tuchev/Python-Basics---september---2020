money = input()
total_sum = 0
while money != "NoMoreMoney":
    if int(float(money)) < 0:
        print("Invalid operation!")
        break
    total_sum += float(money)
    print(f"Increase: {money}")
    money = input()
print(f"Total: {total_sum:.2f}")