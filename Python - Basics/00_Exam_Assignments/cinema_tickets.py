movie = input()
total_student = 0
total_standard = 0
total_kid = 0
total_tickets = 0

while movie != "Finish":
    free_seats = int(input())
    type_of_ticket = input()
    tickets_per_movie = 0
    while type_of_ticket != 'End':
        if type_of_ticket == 'student':
            total_student += 1
        elif type_of_ticket == 'standard':
            total_standard += 1
        else:
            total_kid += 1
        total_tickets += 1
        tickets_per_movie += 1
        if tickets_per_movie == free_seats:
            break
        type_of_ticket = input()
    print(f'{movie} - {tickets_per_movie / free_seats * 100:.2f}% full.')
    movie = input()

print(f'Total tickets: {total_tickets}\n'
      f'{total_student / total_tickets * 100:.2f}% student tickets.\n'
      f'{total_standard / total_tickets * 100:.2f}% standard tickets.\n'
      f'{total_kid / total_tickets * 100:.2f}% kids tickets.')
