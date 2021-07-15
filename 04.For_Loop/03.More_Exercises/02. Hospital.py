period = int(input())
treated_patients = 0
untreated_patients = 0
number_of_doctors = 7

for day in range(1, period + 1):
    number_of_patients = int(input())
    if day % 3 == 0 and untreated_patients > treated_patients:
        number_of_doctors += 1
    if number_of_patients > number_of_doctors:
        treated_patients += number_of_doctors
        untreated_patients += number_of_patients - number_of_doctors
    else:
        treated_patients += number_of_patients
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")