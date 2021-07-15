a = int(input())
b = int(input())
max_number_of_password = int(input())

count_password = 0
start_number_a = 35
start_number_b = 64

while start_number_a <= 55:
    while start_number_b <= 96:
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                A = chr(start_number_a)
                B = chr(start_number_b)
                print(f"{A}{B}{x}{y}{B}{A}", end="|")
                count_password += 1
                start_number_a += 1
                start_number_b += 1
                if count_password >= max_number_of_password or (x == a and y == b):
                    exit(0)
                if start_number_a > 55:
                    start_number_a = 35
                if start_number_b > 96:
                    start_number_b = 64