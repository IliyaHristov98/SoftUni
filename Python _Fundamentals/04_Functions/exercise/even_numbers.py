def even_numbers(numbers):
    return numbers % 2 == 0


list_of_integers = [int(x) for x in input().split()]

even_list = list(filter(even_numbers, list_of_integers))
print(even_list)
