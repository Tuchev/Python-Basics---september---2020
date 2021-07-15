from math import floor
length = float(input())
width = float(input())

length_in_cm = length * 100
width_in_cm = width * 100

#Едно работно място е с размери 70 на 120 см
#вратата е с размери 160 на нещо си = едно работно място
#катедра е с размери 160 на 120 см = две работни места
#коридора е широк 100 см

number_of_rows = floor(length_in_cm / 120)
number_of_column = floor((width_in_cm - 100) / 70)

total_number_of_desk = number_of_rows * number_of_column - 3
print(total_number_of_desk)