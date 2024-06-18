list_no_vowels = [x for x in input() if x.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(list_no_vowels))
