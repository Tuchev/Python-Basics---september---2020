number = float(input())
input_unit = input()
output_unit = input()
result = 0
if input_unit == 'mm':
    if output_unit == "m":
        result = number / 1000
    elif output_unit == 'cm':
        result = number / 10
elif input_unit == 'cm':
    if output_unit == 'mm':
        result = number * 10
    elif output_unit == 'm':
        result = number / 100
elif input_unit == 'm':
    if output_unit == 'mm':
        result = number * 1000
    elif output_unit == 'cm':
        result = number * 100
print(f'{result: .3f}')