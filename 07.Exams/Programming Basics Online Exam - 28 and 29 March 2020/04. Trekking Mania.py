number_of_groups = int(input())

total_persons = 0
for_musala = 0
for_mont_blanc = 0
for_kilimanjaro = 0
for_k2 = 0
for_everest = 0

for group in range(1, number_of_groups + 1):
    persons = int(input())
    total_persons += persons
    if persons <= 5:
        for_musala += persons
    elif persons <= 12:
        for_mont_blanc += persons
    elif persons <= 25:
        for_kilimanjaro += persons
    elif persons <= 40:
        for_k2 += persons
    else:
        for_everest += persons
print(f"{(for_musala / total_persons * 100):.2f}%")
print(f"{(for_mont_blanc / total_persons * 100):.2f}%")
print(f"{(for_kilimanjaro / total_persons * 100):.2f}%")
print(f"{(for_k2 / total_persons * 100):.2f}%")
print(f"{(for_everest / total_persons * 100):.2f}%")