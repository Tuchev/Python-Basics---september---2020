from math import floor
film_name = input()
num_seasons = int(input())
num_episodes = int(input())
time_of_one_episode = float(input())

time_of_episode_with_ad = time_of_one_episode * 1.2

bonus_time = num_seasons * 10

total_time = time_of_episode_with_ad * num_episodes * num_seasons + bonus_time
print(f"Total time needed to watch the {film_name} series is {floor(total_time)} minutes.")