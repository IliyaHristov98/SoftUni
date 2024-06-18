def even_odd(*args):
    command = args[-1]
    if command == "even":
        return [int(arg) for arg in args[:-1] if int(arg) % 2 == 0]
    elif command == "odd":
        return [int(arg) for arg in args[:-1] if int(arg) % 2 != 0]
