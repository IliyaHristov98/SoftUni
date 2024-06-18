n, m = input().split()

n_set = set()
m_set = set()

for x in range(int(n) + int(m)):
    number = int(input())
    if x < int(n):
        n_set.add(number)
    else:
        m_set.add(number)

total = m_set & n_set

for item in total:
    print(item)
