capacity = int(input())
number_of_fans = int(input())

fans_in_sector_A = 0
fans_in_sector_B = 0
fans_in_sector_V = 0
fans_in_sector_G = 0

for fan in range(1, number_of_fans + 1):
    fan = input()
    if fan == "A":
        fans_in_sector_A += 1
    elif fan == "B":
        fans_in_sector_B += 1
    elif fan == "V":
        fans_in_sector_V += 1
    elif fan == "G":
        fans_in_sector_G += 1
print(f"{(fans_in_sector_A / number_of_fans * 100):.2f}%")
print(f"{(fans_in_sector_B / number_of_fans * 100):.2f}%")
print(f"{(fans_in_sector_V / number_of_fans * 100):.2f}%")
print(f"{(fans_in_sector_G / number_of_fans * 100):.2f}%")
print(f"{(number_of_fans / capacity * 100):.2f}%")