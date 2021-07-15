start_number = int(input())
end_number = int(input())
magic_number = int(input())

combination_count = 0
is_Found = False

for num_1 in range(start_number, end_number + 1):
    for num_2 in range(start_number, end_number + 1):
        combination_count += 1
        if (num_1 + num_2) == magic_number:
            is_Found = True
            print(f"Combination N:{combination_count} ({num_1} + {num_2} = {magic_number})")
            exit()
if not is_Found:
    print(f"{combination_count} combinations - neither equals {magic_number}")