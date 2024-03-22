def type_check(type_of_data):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_of_data):
                    return "Bad Type"

            return func(*args)

        return wrapper

    return decorator
