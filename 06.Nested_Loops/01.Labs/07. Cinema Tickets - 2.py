name_of_film = input()
free_spaces = int(input())
type_ticket = input()
total_tickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0

while type_ticket != 'Finish':
    busy_seats = 0
    while type_ticket != 'End' and busy_seats < free_spaces:
        busy_seats += 1
        if type_ticket == 'standard':
            standard_tickets += 1
        elif type_ticket == 'student':
            student_tickets += 1
        elif type_ticket == 'kid':
            kid_tickets += 1
        type_ticket = input()
    total_tickets = standard_tickets + student_tickets + kid_tickets
    print(f'{name_of_film} - {(busy_seats / free_spaces) * 100:.2f}% full.')
    if type_ticket != 'Finish':
        name_of_film = input()
        free_spaces = int(input())
        type_ticket = input()
print(f'Total tickets: {total_tickets}')
print(f'{(student_tickets / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.')
