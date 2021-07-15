import sys
n = int(input())
max = -sys.maxsize
min = sys.maxsize
for number in range(1, n +1):
    value = int(input())
    # дали е максимум
    if value > max:
        max = value
    # дали е минимум
    if value < min:
        min = value
print(f"Max number: {max}")
print(f"Min number: {min}")