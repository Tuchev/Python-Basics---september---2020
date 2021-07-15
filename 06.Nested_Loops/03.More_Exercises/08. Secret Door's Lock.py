num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

for a in range(1, num_1 +1):
    for b in range(1, num_2 + 1):
        for c in range(1, num_3 + 1):
            if a % 2 == 0 and c % 2 == 0:
                if b == 2 or b == 3 or b == 5 or b == 7:
                    print(f"{a} {b} {c}")