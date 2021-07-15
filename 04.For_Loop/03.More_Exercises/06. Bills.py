number_of_months = int(input())

water = 20
internet = 15
other = 0
average = 0
total_sum_electricity = 0

for month in range(1, number_of_months + 1):
    electricity = float(input())
    total_sum_electricity += electricity
    other += (electricity + 20 + 15) * 1.2

total_sum_wather = number_of_months * 20
total_sum_internet = number_of_months * 15
print(f"Electricity: {total_sum_electricity:.2f} lv")
print(f"Water: {total_sum_wather:.2f} lv")
print(f"Internet: {total_sum_internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {((total_sum_electricity + total_sum_wather + total_sum_internet + other) / number_of_months):.2f} lv")