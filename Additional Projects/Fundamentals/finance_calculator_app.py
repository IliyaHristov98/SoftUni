def simple_interest(principal, interest_rate, months):
    return ((principal * (interest_rate / 100)) / 12) * months


def compound_interest(principal, interest_rate, months):
    total = principal
    for i in range(months):
        total += ((total * (interest_rate / 100)) / 12)
    return total - principal


def loan_payment(principal, interest_rate, months):
    monthly_interest = (principal * (interest_rate / 100)) / 12
    to_be_paid = principal + monthly_interest * months
    return to_be_paid / months


while True:
    print(f"Menu:\n"
          f"{2 * ' '}1. Calculate Simple Interest\n"
          f"{2 * ' '}2. Calculate Compound Interest\n"
          f"{2 * ' '}3. Calculate Monthly Loan Payment\n"
          f"{2 * ' '}4. Quit\n")

    choice = int(input("Enter your choice (1/2/3/4): "))
    input_principal = int(input("Enter principal amount: "))
    input_interest_rate = int(input("Enter yearly interest rate percentage: "))
    input_months = int(input("Enter time (in months): "))
    if choice == 1:
        print(f"Total simple interest: {simple_interest(input_principal, input_interest_rate, input_months):.2f}")
    elif choice == 2:
        print(f"Total compound interest: {simple_interest(input_principal, input_interest_rate, input_months):.2f}")
    elif choice == 3:
        print(f"Monthly payment: {simple_interest(input_principal, input_interest_rate, input_months):.2f}")
    elif choice == 4:
        print("Goodbye!")
        break

    more_calculation = input(f"Do you want to perform another calculation? (yes/no): ")
    if more_calculation == "yes":
        continue
    else:
        print("Goodbye!")
        break

# To adjust outcomes when the input in "Enter your choice (1/2/3/4): "
# and "Do you want to perform another calculation? (yes/no): " is not either