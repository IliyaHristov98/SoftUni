clothes_box = [int(x) for x in input().split()]
capacity = int(input())
racks = 1
current_rack = 0

while clothes_box:
    current_piece = clothes_box.pop()
    if current_piece + current_rack <= capacity:
        current_rack += current_piece
    else:
        racks += 1
        current_rack = current_piece

print(racks)
