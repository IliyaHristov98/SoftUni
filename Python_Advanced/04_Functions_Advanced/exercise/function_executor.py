# 1
def func_executor(*funcs):
    results = []
    for item in funcs:
        func, values = item[0], item[1]
        results.append(f"{func.__name__} - {func(*values)}")
    return "\n".join(results)

# 2
# def func_executor(*funcs):
#     return '\n'.join(f"{func.__name__} - {func(*values)}" for func, values in funcs)
