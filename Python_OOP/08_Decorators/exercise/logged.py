def logged(ref_func):
    def wrapper(*args):
        result = ref_func(*args)
        return f"you called {ref_func.__name__}({', '.join(map(str, args))})\n" \
               f"it returned {result}"

    return wrapper
