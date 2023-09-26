n = int(input())
word = input()
full_list = []

for x in range(n):
    string = input()
    full_list.append(string)
print(full_list)

for y in range(len(full_list) - 1, -1, -1):
    element = full_list[y]
    if word not in element:
        full_list.remove(element)
print(full_list)
