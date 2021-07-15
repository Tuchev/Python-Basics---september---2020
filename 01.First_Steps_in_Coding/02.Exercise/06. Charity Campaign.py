price_of_cake = 45
price_of_waffles = 5.80
price_of_pancake = 3.20
number_of_day = int(input())
number_of_confectioner = int(input())
number_of_cake = int(input())
number_of_waffles = int(input())
number_of_panacake = int(input())
total_sum_of_cake = number_of_cake * price_of_cake
total_sum_of_waffles = number_of_waffles * price_of_waffles
total_sum_of_panacake = number_of_panacake * price_of_pancake
sum_for_one_day = total_sum_of_cake + total_sum_of_waffles + total_sum_of_panacake
total_revenue = (sum_for_one_day * number_of_day) * number_of_confectioner
total_sum = total_revenue - (total_revenue * 1 / 8)
print(total_sum)