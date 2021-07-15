import sys
from math import ceil
number_easter_bread = int(input())

quantity_sugar = 0
quantity_flour = 0

sugar_pack = 950
flour_pack = 750
max_quantity_sugar = -sys.maxsize
max_quantity_flour = -sys.maxsize

for easter_bread in range(1, number_easter_bread + 1):
    sugar_for_one_easter_bread = int(input())
    flour_for_one_easter_bread = int(input())
    quantity_sugar += sugar_for_one_easter_bread
    quantity_flour += flour_for_one_easter_bread
    if sugar_for_one_easter_bread > max_quantity_sugar:
        max_quantity_sugar = sugar_for_one_easter_bread
    if flour_for_one_easter_bread > max_quantity_flour:
        max_quantity_flour = flour_for_one_easter_bread

print(f"Sugar: {ceil(quantity_sugar / sugar_pack)}")
print(f"Flour: {ceil(quantity_flour / flour_pack)}")
print(f"Max used flour is {max_quantity_flour} grams, max used sugar is {max_quantity_sugar} grams.")