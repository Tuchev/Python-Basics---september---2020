number_of_rows = int(input())
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0
total_result = 0

for row in range(1, number_of_rows + 1):
    row = int(input())
    if 0 <= row <= 9:
        from_0_to_9 += 1
        total_result += row * 0.2
    if 10 <= row <= 19:
        from_10_to_19 += 1
        total_result += row * 0.3
    if 20 <= row <= 29:
        from_20_to_29 += 1
        total_result += row * 0.4
    if 30 <= row <= 39:
        from_30_to_39 += 1
        total_result += 50
    if 40 <= row <= 50:
        from_40_to_50 += 1
        total_result += 100
    if row < 0 or row > 50:
        invalid_numbers += 1
        total_result /= 2

print(f"{total_result:.2f}")
print(f"From 0 to 9: {(from_0_to_9 / number_of_rows * 100):.2f}%")
print(f"From 10 to 19: {(from_10_to_19 / number_of_rows * 100):.2f}%")
print(f"From 20 to 29: {(from_20_to_29 / number_of_rows * 100):.2f}%")
print(f"From 30 to 39: {(from_30_to_39 / number_of_rows * 100):.2f}%")
print(f"From 40 to 50: {(from_40_to_50 / number_of_rows * 100):.2f}%")
print(f"Invalid numbers: {(invalid_numbers / number_of_rows * 100):.2f}%")
