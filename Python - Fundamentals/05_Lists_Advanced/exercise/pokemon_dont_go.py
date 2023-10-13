initial_integers = [int(i) for i in input().split()]
removed_elements = []

while initial_integers:
    given_index = int(input())

    if given_index < 0:
        popped_index = initial_integers.pop(0)
        removed_elements.append(popped_index)
        initial_integers.insert(0, initial_integers[-1])

    elif 0 <= given_index <= len(initial_integers) - 1:
        popped_index = initial_integers.pop(given_index)
        removed_elements.append(popped_index)

    else:
        popped_index = initial_integers.pop(-1)
        removed_elements.append(popped_index)
        initial_integers.insert(len(initial_integers), initial_integers[0])

    for x in range(len(initial_integers)):
        if initial_integers[x] <= popped_index:
            initial_integers[x] += popped_index
        elif initial_integers[x] > popped_index:
            initial_integers[x] -= popped_index

print(sum(removed_elements))
