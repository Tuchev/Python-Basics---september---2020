number_of_mans = int(input())
number_of_womans = int(input())
number_of_tables = int(input())

count = 0

for man in range(1, number_of_mans + 1):
    for woman in range(1, number_of_womans + 1):
        count += 1
        if count <= number_of_tables:
            print(f"({man} <-> {woman})", end=" ")