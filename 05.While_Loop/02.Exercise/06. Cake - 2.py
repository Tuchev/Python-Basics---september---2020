width = int(input())
lenght = int(input())
total_pieces = width * lenght
eated_pieces = 0
command = input()
while command != "STOP":
    total_pieces -= int(command)
    if total_pieces < 0:
        diff = abs(total_pieces - eated_pieces)
        print(f"No more cake left! You need {diff} pieces more.")
        break
    command = input()
else:
    diff = abs(total_pieces - eated_pieces)
    print(f"{diff} pieces are left.")