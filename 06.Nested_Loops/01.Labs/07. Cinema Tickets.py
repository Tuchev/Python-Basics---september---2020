film_name = input()
free_spaces = int(input())
command = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0
sold_tickets = 0

while film_name != "Finish":
    while command != "End":
        if command == "student":
            sold_tickets += 1
            student_tickets += 1
        elif command == "standard":
            sold_tickets += 1
            standard_tickets += 1
        elif command == "kid":
            sold_tickets += 1
            kid_tickets += 1
        command = input()
    print(f"{film_name} - {(sold_tickets / free_spaces) * 100}% full.")
    if film_name == "End":
        film_name = input()
        free_spaces = int(input())
print(f"Total tickets: {sold_tickets}")
print(f"{(sold_tickets - student_tickets) * 100}% student tickets.")
print(f"{(sold_tickets - standard_tickets) * 100}% standard tickets.")
print(f"{(sold_tickets - kid_tickets) * 100}% kids tickets.")
