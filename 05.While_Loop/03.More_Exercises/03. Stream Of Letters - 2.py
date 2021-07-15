command = input()
count_of_c = 0
count_of_o = 0
count_of_n = 0

current_word = ""

while command != "End":
    if command == "c":
        count_of_c += 1
        command = input()
        if count_of_c > 1:
            current_word += command

    elif command == "o":
        count_of_o += 1
        command = input()
        if count_of_o > 1:
            current_word += command

    elif command == "n":
        count_of_n += 1
        command = input()
        if count_of_n > 1:
            current_word += command

    if count_of_c == 1 and count_of_n == 1 and count_of_o == 1:
        current_word += " "
        count_of_n = 0
        count_of_o = 0
        count_of_c = 0
    if (ord(command) >= 97 and ord(command) <= 122) or (ord(command) >= 65 and ord(command) <= 90):
        current_word += command

    command = input()
if command == "End":
    print(current_word)