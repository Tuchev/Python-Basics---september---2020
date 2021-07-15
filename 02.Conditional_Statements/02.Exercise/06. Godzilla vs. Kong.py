budget = float(input())
number_of_actors = float(input())
price_of_clothes = float(input())

price_for_decor = budget * 0.10
price_for_all_clothes = number_of_actors * price_of_clothes
total_price_for_film = price_for_decor + price_for_all_clothes

if number_of_actors > 150:
    total_price_for_clothes = price_for_all_clothes - (price_for_all_clothes * 0.10)
    total_price_for_film = price_for_decor + total_price_for_clothes

if total_price_for_film > budget:
    money_needed = total_price_for_film - budget
    print("Not enough money!")
    print(f"Wingard needs{money_needed: .2f} leva more.")
elif total_price_for_film <= budget:
    money_left = budget - total_price_for_film
    print("Action!")
    print(f"Wingard starts filming with{money_left: .2f} leva left.")
