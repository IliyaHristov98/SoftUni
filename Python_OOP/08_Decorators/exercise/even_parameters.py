def even_parameters(func):
    def wrapper(*args, **kwargs):
        for num in args:
            if isinstance(num, int):
                if num % 2 == 0:
                    continue
            return "Please use only even numbers!"

        return func(*args, **kwargs)

    return wrapper
