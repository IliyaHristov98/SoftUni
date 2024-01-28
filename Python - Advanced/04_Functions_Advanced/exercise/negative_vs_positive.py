def func(nums):
    negative = sum(num for num in nums if num < 0)
    positive = sum(num for num in nums if num > 0)

    print(negative)
    print(positive)
    if abs(negative) > positive:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
func(numbers)
