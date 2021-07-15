n = int(input())
m = int(input())
s = int(input())

for adress in range(m, n, - 1):
    if s == adress:
        break
    if adress % 3 == 0 and adress % 2 == 0:
        print(adress, end=" ")