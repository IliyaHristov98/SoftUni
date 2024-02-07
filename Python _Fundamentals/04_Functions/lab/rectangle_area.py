# Using function

def rectangle_area(a, b):
    return a * b


width = int(input())
length = int(input())

print(rectangle_area(width, length))

# Using Lambda function

rectangle_area = lambda a, b: a * b
width = int(input())
length = int(input())
print(rectangle_area(width, length))
