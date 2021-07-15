import sys
number = int(input())
sum_of_odd_numbers = 0
max_number_odd = -sys.maxsize
min_number_odd = sys.maxsize
sum_of_even_numbers = 0
max_number_even = -sys.maxsize
min_number_even = sys.maxsize

for number in range(1, number + 1):
    value = float(input())
    if number % 2 == 0:
        sum_of_even_numbers += value
        if value > max_number_even:
            max_number_even = value
        if value < min_number_even:
            min_number_even = value
    else:
        sum_of_odd_numbers += value
        if value > max_number_odd:
            max_number_odd = value
        if value < min_number_odd:
            min_number_odd = value
print(f"OddSum={sum_of_odd_numbers:.2f},")
if min_number_odd == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={min_number_odd:.2f},")
if max_number_odd == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={max_number_odd:.2f},")
print(f"EvenSum={sum_of_even_numbers:.2f},")
if min_number_even == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={min_number_even:.2f},")
if max_number_even == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={max_number_even:.2f}")