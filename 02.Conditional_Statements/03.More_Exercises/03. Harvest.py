from math import floor
from math import ceil

x_are_vineyard = int(input())
y_grapes = float(input())
z_required_liters = int(input())
number_workers = int(input())

total_grapes = x_are_vineyard * y_grapes
liters_of_wine = (total_grapes / 2.5) * 0.40

residue = abs(z_required_liters - liters_of_wine)
wine_per_person = abs(residue / number_workers)

if liters_of_wine < z_required_liters:
    print(f'It will be a tough winter! More {floor(residue)} liters wine needed.')

elif liters_of_wine >= z_required_liters:
    print(f'Good harvest this year! Total wine: {floor(liters_of_wine)} liters.')
    print(f'{ceil(residue)} liters left -> {ceil(wine_per_person)} liters per person.')