name = input()
adult_tickets_count = int(input())
children_tickets_count = int(input())
adult_ticket_price = float(input())
tax = float(input())

children_ticket_price  = adult_ticket_price * 0.30
total_income = adult_tickets_count * adult_ticket_price + children_tickets_count * children_ticket_price +\
    tax * (children_tickets_count + adult_tickets_count)

total_profit = total_income * 0.2

print(f'The profit of your agency from {name} tickets is {total_profit:.2f} lv.')