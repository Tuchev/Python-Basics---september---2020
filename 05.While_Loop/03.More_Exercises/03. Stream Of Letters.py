command = input()


while True:
    if command == "End":
        break
    if ord(command) <= 96 or ord(command) >= 123:
        None
    if command == "c" or command == "n" or command == "o":
        None

    else:
        print(command)
    command = input()