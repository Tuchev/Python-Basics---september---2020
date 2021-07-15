destination = input()   #"France", "Italy" или "Germany"
dates = input()         #"21-23", "24-27" или "28-31"

number_of_overnight = int(input())

# Дестинация	21-23 март	    24-27 март	    28-31 март
# Франция	    30 лв.	        35 лв.	        40 лв.
# Италия	    28 лв.	        32 лв.	        39 лв.
# Германия	    32 лв.	        37 лв.	        43 лв.

price = 0

if destination == "France":
    if dates == "21-23":
        price = 30
    elif dates == "24-27":
        price = 35
    elif dates == "28-31":
        price = 40
elif destination == "Italy":
    if dates == "21-23":
        price = 28
    elif dates == "24-27":
        price = 32
    elif dates == "28-31":
        price = 39
elif destination == "Germany":
    if dates == "21-23":
        price = 32
    elif dates == "24-27":
        price = 37
    elif dates == "28-31":
        price = 43

total_sum = number_of_overnight * price
print(f"Easter trip to {destination} : {total_sum:.2f} leva.")