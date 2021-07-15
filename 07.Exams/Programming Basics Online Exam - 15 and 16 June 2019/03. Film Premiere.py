projection = input()
packet_for_film = input()
number_of_tickets = int(input())

price_of_ticket = 0

if projection == "John Wick":
    if packet_for_film == "Drink":
        price_of_ticket = 12
    elif packet_for_film == "Popcorn":
        price_of_ticket = 15
    elif packet_for_film == "Menu":
        price_of_ticket = 19

if projection == "Star Wars":
    if packet_for_film == "Drink":
        price_of_ticket = 18
    elif packet_for_film == "Popcorn":
        price_of_ticket = 25
    elif packet_for_film == "Menu":
        price_of_ticket = 30
    if number_of_tickets >= 4:
        price_of_ticket *= 0.7

if projection == "Jumanji":
    if packet_for_film == "Drink":
        price_of_ticket = 9
    elif packet_for_film == "Popcorn":
        price_of_ticket = 11
    elif packet_for_film == "Menu":
        price_of_ticket = 14
    if number_of_tickets == 2:
        price_of_ticket *= 0.85

total_sum = number_of_tickets * price_of_ticket
print(f"Your bill is {total_sum:.2f} leva.")