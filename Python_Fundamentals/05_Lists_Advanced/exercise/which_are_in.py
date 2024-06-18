first = input().split(", ")
second = input().split(", ")
list_of_all = [x for x in first for y in second if x in y]
final = []

for i in list_of_all:
    if i not in final:
        final.append(i)

print(final)
