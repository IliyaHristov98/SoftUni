def print_top_part(size):
    for i in range(1, size + 1):
        print((size - i) * " ", "* " * i)


def print_bottom_part(size):
    for i in range(size - 1, 0, -1):
        print((size - i) * " ", "* " * i)


n = int(input())
print_top_part(n)
print_bottom_part(n)
