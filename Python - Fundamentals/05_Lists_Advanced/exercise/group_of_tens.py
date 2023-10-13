input_integers = list(int(i) for i in input().split(", "))
starting = 10

while max(input_integers) > starting - 10:
    filtering = lambda x: starting - 10 < x <= starting
    current_tens = list(filter(filtering, input_integers))
    print(f"Group of {starting}'s: {current_tens}")
    starting += 10
