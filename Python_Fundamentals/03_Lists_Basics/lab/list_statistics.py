number_of_integers = int(input())
negative_list = []
positive_list = []

for n in range(number_of_integers):
    integer = int(input())
    if integer < 0:
        negative_list.append(integer)
    else:
        positive_list.append(integer)

print(f'{positive_list} \n'
      f'{negative_list} \n'
      f'Count of positives: {len(positive_list)} \n'
      f'Sum of negatives: {sum(negative_list)}')
