size_of_eggs = input()  #"Large", "Medium" или "Small"
color_of_eggs = input() #"Red", "Green" или "Yellow"
number_batchs = int(input())

# 	                Червено (Red)	Зелено (Green)	Жълто (Yellow)
# Големи (Large)	16 лв.	        12 лв.	        9 лв.
# Средни (Medium)	13 лв.	        9 лв.	        7 лв.
# Малки (Small)	    9 лв.	        8 лв.	        5 лв.

price = 0

if size_of_eggs == "Large":
    if color_of_eggs == "Red":
        price = 16
    elif color_of_eggs == "Green":
        price = 12
    elif color_of_eggs == "Yellow":
        price = 9
elif size_of_eggs == "Medium":
    if color_of_eggs == "Red":
        price = 13
    elif color_of_eggs == "Green":
        price = 9
    elif color_of_eggs == "Yellow":
        price = 7
elif size_of_eggs == "Small":
    if color_of_eggs == "Red":
        price = 9
    elif color_of_eggs == "Green":
        price = 8
    elif color_of_eggs == "Yellow":
        price = 5
income = number_batchs * price
total_sum = income * 0.65
print(f"{total_sum:.2f} leva.")