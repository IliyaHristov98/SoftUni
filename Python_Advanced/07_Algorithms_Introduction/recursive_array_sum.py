def sum_nums(numbers, index=0):
    if index == len(numbers) - 1:
        return numbers[index]

    return numbers[index] + sum_nums(nums, index + 1)


nums = [int(x) for x in input().split()]
print(sum_nums(nums))
