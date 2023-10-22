rating_list = [int(i) for i in input().split(", ")]
entry_point = int(input())
price_range = input()
right_list = [rating_list[x] for x in range(entry_point + 1, len(rating_list))]
left_list = [rating_list[y] for y in range(0, entry_point)]

right_damage = 0
left_damage = 0

if price_range == "cheap":
    for right in right_list:
        if right < rating_list[entry_point]:
            right_damage += right

    for left in left_list:
        if left < rating_list[entry_point]:
            left_damage += left

else:
    for right in right_list:
        if right >= rating_list[entry_point]:
            right_damage += right

    for left in left_list:
        if left >= rating_list[entry_point]:
            left_damage += left

if left_damage >= right_damage:
    print(f"Left - {left_damage}")
else:
    print(f"Right - {right_damage}")
