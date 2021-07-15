first_letter = input()
second_letter = input()
third_letter = input()

combination_count = 0

for letter_1 in range(ord(first_letter), ord(second_letter) + 1):
    for letter_2 in range(ord(first_letter), ord(second_letter) + 1):
        for letter_3 in range(ord(first_letter), ord(second_letter) + 1):
            if chr(letter_1) == third_letter or chr(letter_2) == third_letter or chr(letter_3) == third_letter:
                continue
            combination_count += 1
            print(f"{chr(letter_1)}{chr(letter_2)}{chr(letter_3)}", end=" ")
print(combination_count)