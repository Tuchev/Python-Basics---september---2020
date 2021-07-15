film_name = input()
num_of_days = int(input())
num_of_tickets = int(input())
price_for_ticket = float(input())
percent_for_cinema = int(input())

sum_of_all = num_of_days * num_of_tickets * price_for_ticket
profit = sum_of_all - (sum_of_all * percent_for_cinema / 100)
print(f"The profit from the movie {film_name} is {profit:.2f} lv.")