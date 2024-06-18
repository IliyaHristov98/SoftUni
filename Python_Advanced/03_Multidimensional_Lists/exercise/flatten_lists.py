list_of_strings = input().split("|")

sub_list = []

for string in list_of_strings[::-1]:
    sub_list.extend(string.split(" "))

while "" in sub_list:
    sub_list.remove("")

print(*sub_list, sep=" ")
