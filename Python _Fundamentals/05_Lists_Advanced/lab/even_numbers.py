list_of_numbers = [int(x) for x in input().split(", ")]
list_of_indexes = map(lambda x: x if list_of_numbers[x] % 2 == 0 else "no", range(len(list_of_numbers)))
even_indexes = list(filter(lambda y: y != "no", list_of_indexes))
print(even_indexes)
