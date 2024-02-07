def print_triangle(n):
    for i in range(n):
        for l in range(1, i + 1):
            print(l, end=" ")
        print()

    for m in range(n, 0, -1):
        for n in range(1, m + 1):
            print(n, end=" ")
        print()


size = int(input())
print_triangle(size)
