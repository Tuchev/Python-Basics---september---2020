import sys
command = input()
sum = 0
total_sum = 0
movie_name = ""
movie_to_watch = ""
movie_size = 0
movie_maxsize = -sys.maxsize
count = 0
is_Count = False

while command != "STOP":
    count += 1
    if count >= 7:
        is_Count = True
        break
    for letter in str(command):
        movie_name = command
        if 65 <= ord(letter) <= 90:
            sum = ord(letter) - len(command)
            total_sum += sum
        elif 97 <= ord(letter) <= 122:
            sum = ord(letter) - len(command) * 2
            total_sum += sum
        else:
            total_sum += ord(letter)
        if total_sum > movie_size:
            movie_size = total_sum
    command = input()
    total_sum = 0
    if movie_size > movie_maxsize:
        movie_maxsize = movie_size
        movie_to_watch = movie_name
if is_Count:
    print("The limit is reached.")
print(f"The best movie for you is {movie_to_watch} with {movie_maxsize} ASCII sum.")