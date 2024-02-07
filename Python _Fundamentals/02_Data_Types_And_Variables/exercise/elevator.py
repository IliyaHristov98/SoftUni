people = int(input())
capacity = int(input())

full_courses = people // capacity
people_left = people % capacity
if people_left > capacity:
    full_courses += 2
elif people_left <= capacity and people_left != 0:
    full_courses += 1
print(full_courses)
