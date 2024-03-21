def even_numbers(function):
    def wrapper(*args, **kwargs):
        result = [num for num in args if num % 2 == 0]
        return function(result)

    return wrapper
