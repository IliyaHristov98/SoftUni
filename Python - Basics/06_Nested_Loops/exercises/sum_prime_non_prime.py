number = input()
prime_total = 0
non_prime_total = 0

while not number == 'stop':
    int_number = int(number)
    is_prime = True

    if int_number < 0:
        print(f"Number is negative.")
        number = input()
        continue

    for i in range(2, int_number):
        if int_number % i == 0:
            is_prime = False
            break

    if is_prime and int_number != 1:
        prime_total += int_number
    elif not is_prime and int_number != 1:
        non_prime_total += int_number

    number = input()

print(f'Sum of all prime numbers is: {prime_total}')
print(f'Sum of all non prime numbers is: {non_prime_total}')

