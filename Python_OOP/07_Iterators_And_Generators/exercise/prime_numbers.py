def get_primes(list_of_integers):
    for integer in list_of_integers:
        if integer <= 1:
            continue

        for divisor in range(2, integer):
            if integer % divisor == 0:
                break
        else:
            yield integer
