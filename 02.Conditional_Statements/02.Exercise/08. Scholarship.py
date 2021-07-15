from math import floor

income = float(input())
average_success = float(input())
minimal_salary = float(input())

social_scholarship = floor(minimal_salary * 0.35)
excellent_scholarship = floor(average_success * 25)

excellent = bool(average_success >= 5.50)
very_good = bool(4.50 < average_success < 5.50)
good = bool(average_success <= 4.50)

low_income = bool(income < minimal_salary)
high_income = bool(income > minimal_salary)

high_excellent_scholarship = bool(excellent_scholarship >= social_scholarship)
high_social_scholarship = bool(social_scholarship > excellent_scholarship)


# if average_success >= 5.50:
#     if income < minimal_salary:
#         if excellent_scholarship >= social_scholarship:
#             print(f'You get a scholarship for excellent results {excellent_scholarship} BGN')
#         else:
#             print(f'You get a Social scholarship {social_scholarship} BGN')
#     else:
#         print(f'You get a scholarship for excellent results {excellent_scholarship} BGN')
# elif 4.50 < average_success < 5.50:
#     if income < minimal_salary:
#         print(f'You get a Social scholarship {social_scholarship} BGN')
#     else:
#         print(f'You cannot get a scholarship!')
# else:
#     print(f'You cannot get a scholarship!')

if excellent and low_income and high_excellent_scholarship:
    print(f'You get a scholarship for excellent results {excellent_scholarship} BGN')
elif excellent and low_income and high_social_scholarship:
    print(f'You get a Social scholarship {social_scholarship} BGN')
elif excellent:
    print(f'You get a scholarship for excellent results {excellent_scholarship} BGN')
elif very_good and low_income:
    print(f'You get a Social scholarship {social_scholarship} BGN')
elif very_good and high_income:
    print(f'You cannot get a scholarship!')
else:
    print(f'You cannot get a scholarship!')