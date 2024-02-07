def sequence(number):
    if number <= 0:
        return []
    elif number == 1:
        return [1]
    elif number == 2:
        return [1, 1]
    else:
        tribonacci_sequence = [1, 1, 2]

        for i in range(3, number):
            next_number = tribonacci_sequence[-1] + tribonacci_sequence[-2] + tribonacci_sequence[-3]
            tribonacci_sequence.append(next_number)
        return tribonacci_sequence


number_of_numbers = int(input())
final_list = sequence(number_of_numbers)
for x in final_list:
    print(x, end=" ")
