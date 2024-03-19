def solution():
    def integers():
        n = 0
        while True:
            n += 1
            yield n

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return (take, halves, integers)
