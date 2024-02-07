given_string = input()

count_of_symbols = {}
set_of_symbols = set()

for symbol in given_string:
    set_of_symbols.add(symbol)
    if symbol not in count_of_symbols:
        count_of_symbols[symbol] = 1
    else:
        count_of_symbols[symbol] += 1

ordered_set = sorted(set_of_symbols)

for element in ordered_set:
    print(f"{element}: {count_of_symbols[element]} time/s")
