temperature = int(input())
time_of_day = input()

if 10 <= temperature <= 18:
    if time_of_day == "Morning":
        print(f"It's {temperature} degrees, get your Sweatshirt and Sneakers.")
    elif time_of_day == "Afternoon":
        print(f"It's {temperature} degrees, get your Shirt and Moccasins.")
    elif time_of_day == "Evening":
        print(f"It's {temperature} degrees, get your Shirt and Moccasins.")
elif 18 < temperature <= 24:
    if time_of_day == "Morning":
        print(f"It's {temperature} degrees, get your Shirt and Moccasins.")
    elif time_of_day == "Afternoon":
        print(f"It's {temperature} degrees, get your T-Shirt and Sandals.")
    elif time_of_day == "Evening":
        print(f"It's {temperature} degrees, get your Shirt and Moccasins.")
elif temperature >= 25:
    if time_of_day == "Morning":
        print(f"It's {temperature} degrees, get your T-Shirt and Sandals.")
    elif time_of_day == "Afternoon":
        print(f"It's {temperature} degrees, get your Swim Suit and Barefoot.")
    elif time_of_day == "Evening":
        print(f"It's {temperature} degrees, get your Shirt and Moccasins.")