student = 0
standard = 0
kids = 0
final_ticket_sales = 0
name = input()
while not name == "Finish":
    free_spaces = int(input())
    ticket_type = input()
    total_tickets = 0
    while not ticket_type == 'End':
        total_tickets += 1
        if ticket_type == 'student':
            student += 1
        elif ticket_type == 'standard':
            standard += 1
        else:
            kids += 1

        if total_tickets == free_spaces:
            break

        ticket_type = input()
    final_ticket_sales += total_tickets
    fullness_percentage = total_tickets / free_spaces * 100
    print(f'{name} - {fullness_percentage:.2f}% full.')
    name = input()

print(f'Total tickets: {final_ticket_sales}\n'
      f'{student / final_ticket_sales * 100:.2f}% student tickets.\n'
      f'{standard / final_ticket_sales * 100:.2f}% standard tickets.\n'
      f'{kids / final_ticket_sales * 100:.2f}% kids tickets.')
