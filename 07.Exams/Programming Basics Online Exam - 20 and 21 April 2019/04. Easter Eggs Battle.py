eggs_player_one = int(input())
eggs_player_two = int(input())

command = input()
while command != "End of battle":
    if command == "one":
        eggs_player_two -= 1
        if eggs_player_two == 0:
            break
    elif command == "two":
        eggs_player_one -= 1
        if eggs_player_one == 0:
            break
    command = input()
if eggs_player_one == 0:
    print(f"Player one is out of eggs. Player two has {eggs_player_two} eggs left.")
if eggs_player_two == 0:
    print(f"Player two is out of eggs. Player one has {eggs_player_one} eggs left.")
if command == "End of battle":
    print(f"Player one has {eggs_player_one} eggs left.")
    print(f"Player two has {eggs_player_two} eggs left.")