number_of_cargo = int(input())
average_price = 0
total_size_of_cargo = 0
size_of_cargo_with_bus = 0
size_of_cargo_with_truck = 0
size_of_cargo_with_train = 0

for cargo in range(1, number_of_cargo + 1):
    size_of_cargo = int(input())
    total_size_of_cargo += size_of_cargo
    if size_of_cargo <= 3:
        size_of_cargo_with_bus += size_of_cargo
    if 4 <= size_of_cargo <= 11:
        size_of_cargo_with_truck += size_of_cargo
    if size_of_cargo >= 12:
        size_of_cargo_with_train += size_of_cargo
print(f"{((size_of_cargo_with_bus * 200 + size_of_cargo_with_truck * 175 + size_of_cargo_with_train * 120) / total_size_of_cargo):.2f}")
print(f"{((size_of_cargo_with_bus / total_size_of_cargo) * 100):.2f}%")
print(f"{((size_of_cargo_with_truck / total_size_of_cargo) * 100):.2f}%")
print(f"{((size_of_cargo_with_train / total_size_of_cargo) * 100):.2f}%")