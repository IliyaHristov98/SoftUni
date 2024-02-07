expression = input()

opening_indexes = []

for index in range(len(expression)):
    if expression[index] == "(":
        opening_indexes.append(index)
    elif expression[index] == ")":
        start = opening_indexes.pop()
        end = index + 1
        print(expression[start:end])
