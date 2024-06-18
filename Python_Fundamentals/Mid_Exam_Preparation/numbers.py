given_list = [int(i) for i in input().split()]
average_value = sum(given_list) / len(given_list)
higher_than_average = []
for i in range(len(given_list)):
    if max(given_list) > average_value:
        higher_than_average.append(max(given_list))
        given_list.remove(max(given_list))

    if len(higher_than_average) == 5:
        break

if len(higher_than_average) == 0:
    print("No")
else:
    higher_than_average.sort(reverse=True)
    print(' '.join(map(str, higher_than_average)))
