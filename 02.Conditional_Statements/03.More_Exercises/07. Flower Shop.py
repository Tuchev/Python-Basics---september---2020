from math import floor
from math import ceil
number_of_magnolii = int(input())
number_of_ziumbiuli = int(input())
number_of_roses = int(input())
number_of_cactus = int(input())
price_of_gift = float(input())

total_amount_of_flowers = number_of_magnolii * 3.25 + number_of_ziumbiuli * 4 + number_of_roses * 3.50 + number_of_cactus * 8
residue_after_tax = total_amount_of_flowers * 0.95
residue = abs(residue_after_tax - price_of_gift)

if residue_after_tax >= price_of_gift:
    print(f'She is left with {floor(residue)} leva.')
else:
    print(f'She will have to borrow {ceil(residue)} leva.')