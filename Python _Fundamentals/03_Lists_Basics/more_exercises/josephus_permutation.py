people_list = input().split()
k = int(input())
circle_list = []
killed_list = []
count = 0
index = 0
for i in range(len(people_list)):
    circle_list.append(int(people_list[i]))

while len(circle_list) > 0:
    count += 1
    if count % k == 0:
        killed_list.append((circle_list.pop(index)))
    else:
        index += 1

    if index >= len(circle_list):
        index = 0

print(str(killed_list).replace(' ', ''))
