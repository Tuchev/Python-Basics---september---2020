type_of_project = input()
rows = int(input())
columns = int(input())
price = 0

if type_of_project == 'Premiere':
    price = 12
elif type_of_project == 'Normal':
    price = 7.50
elif type_of_project == 'Discount':
    price = 5

total_sum = price * rows * columns
print(f"{total_sum:.2f} leva")