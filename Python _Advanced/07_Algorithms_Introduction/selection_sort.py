def selection_sort(collection):
    for index in range(len(collection)):
        min_index = index

        for curr_index in range(index + 1, len(collection)):
            if collection[curr_index] < collection[min_index]:
                min_index = curr_index

        collection[index], collection[min_index] = collection[min_index], collection[index]

    return " ".join(map(str, collection))


values = [int(x) for x in input().split()]

print(selection_sort(values))
