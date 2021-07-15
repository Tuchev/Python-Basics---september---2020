from math import floor

income_lv = float(input())
averagegrade = float(input())
minsalary = float(input())
social_scholarship = floor(minsalary * 0.35)
excelent_scholarship = floor(averagegrade * 25)
if averagegrade >= 5.50 and income_lv < minsalary and excelent_scholarship >= social_scholarship:
    print(f'You get a scholarship for excellent results {excelent_scholarship} BGN')
elif averagegrade >= 5.50 and income_lv <minsalary and excelent_scholarship < social_scholarship:
    print(f'You get a Social scholarship {social_scholarship} BGN')
elif averagegrade >= 5.50:
    print(f'You get a scholarship for excellent results {excelent_scholarship} BGN')
elif 4.50 < averagegrade < 5.50 and income_lv < minsalary:
    print(f'You get a Social scholarship {social_scholarship} BGN')
elif 4.50 < averagegrade < 5.50 and income_lv > minsalary:
    print(f'You cannot get a scholarship!')
else:
    print(f'You cannot get a scholarship!')