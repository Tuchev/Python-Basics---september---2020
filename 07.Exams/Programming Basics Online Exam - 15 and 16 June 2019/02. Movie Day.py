time_for_photos = int(input())
num_of_scenes = int(input())
time_for_scenes = int(input())

field_preparation = time_for_photos * 0.15
total_time = field_preparation + (num_of_scenes * time_for_scenes)

diff = abs(time_for_photos - total_time)

if time_for_photos >= total_time:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")