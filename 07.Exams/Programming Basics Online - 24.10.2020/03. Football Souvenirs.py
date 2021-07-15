import sys
team = input() #"Argentina", "Brazil", "Croatia", "Denmark"
souvenir = input() #"flags", "caps", "posters", "stickers"
num_of_souvenirs = int(input())

if team == "Argentina":
    if souvenir == "flags":
        price = 3.25
    elif souvenir == "caps":
        price = 7.20
    elif souvenir == "posters":
        price = 5.10
    elif souvenir == "stickers":
        price = 1.25
elif team == "Brazil":
    if souvenir == "flags":
        price = 4.20
    elif souvenir == "caps":
        price = 8.50
    elif souvenir == "posters":
        price = 5.35
    elif souvenir == "stickers":
        price = 1.20
elif team == "Croatia":
    if souvenir == "flags":
        price = 2.75
    elif souvenir == "caps":
        price = 6.90
    elif souvenir == "posters":
        price = 4.95
    elif souvenir == "stickers":
        price = 1.10
elif team == "Denmark":
    if souvenir == "flags":
        price = 3.10
    elif souvenir == "caps":
        price = 6.50
    elif souvenir == "posters":
        price = 4.80
    elif souvenir == "stickers":
        price = 0.90
if team != "Argentina" and team != "Brazil" and team != "Croatia" and team != "Denmark":
    print("Invalid country!")
    sys.exit(0)
if souvenir != "flags" and souvenir != "caps" and souvenir != "posters" and souvenir != "stickers":
    print("Invalid stock!")
    sys.exit(0)
print(f"Pepi bought {num_of_souvenirs} {souvenir} of {team} for {num_of_souvenirs * price:.2f} lv.")