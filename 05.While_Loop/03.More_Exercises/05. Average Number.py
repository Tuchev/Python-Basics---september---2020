n = int(input())
cycle = 0
sum = 0
for num in range(1, n + 1):
    cycle += 1
    number = int(input())
    sum += number
print(f"{(sum / cycle):.2f}")