num_of_days = int(input())
command = input()
money = 0
total_money = 0
num_of_win_games = 0
num_of_lose_games = 0
total_win_games = 0
total_lose_games = 0

for day in range(1, num_of_days + 1):
        command = input()
        while command != "Finish":
            if command == "win":
                num_of_win_games += 1
                money += 20
            elif command == "lose":
                num_of_lose_games += 1
            command = input()
        if num_of_win_games > num_of_lose_games:
            money *= 1.10
            total_money += money
            money = 0
            total_win_games += num_of_win_games
            num_of_win_games = 0
            total_lose_games += num_of_lose_games
            num_of_lose_games = 0
        else:
            total_money += money
            money = 0
            total_win_games += num_of_win_games
            num_of_win_games = 0
            total_lose_games += num_of_lose_games
            num_of_lose_games = 0

if total_win_games > total_lose_games:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")