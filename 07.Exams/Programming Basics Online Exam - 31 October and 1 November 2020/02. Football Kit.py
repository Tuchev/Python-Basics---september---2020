price_of_t_shirt = float(input())
sum_for_ball = float(input())

price_of_shorts = price_of_t_shirt * 0.75
price_of_socks = price_of_shorts * 0.2
price_of_buttons = (price_of_t_shirt + price_of_shorts) * 2

total_sum = price_of_t_shirt + price_of_shorts + price_of_socks + price_of_buttons
total_sum_after_discount = total_sum * 0.85

if total_sum_after_discount >= sum_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum_after_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {sum_for_ball - total_sum_after_discount:.2f} lv. more.")