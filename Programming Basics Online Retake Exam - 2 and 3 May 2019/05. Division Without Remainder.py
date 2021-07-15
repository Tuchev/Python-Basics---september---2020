numbers = int(input())
count = 0
p1 = 0
p2 = 0
p3 = 0

while count != numbers:
    num = int(input())
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1
    count += 1

print(f"{(p1 / numbers * 100):.2f}%")
print(f"{(p2 / numbers * 100):.2f}%")
print(f"{(p3 / numbers * 100):.2f}%")