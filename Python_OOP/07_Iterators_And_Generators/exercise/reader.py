def read_next(*args):
    for item in args:
        # Option 1
        # for i in item:
        #     yield i
        # Option 2
        yield from item
