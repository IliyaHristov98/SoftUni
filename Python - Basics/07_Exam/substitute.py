K = int(input())
L = int(input())
M = int(input())
N = int(input())
count = 0
for k in range(K, 9):
    if k % 2 == 0:

        for l in range(9, L - 1, -1):
            if l % 2 != 0:

                for m in range(M, 9):
                    if m % 2 == 0:

                        for n in range(9, N - 1, -1):
                            if n % 2 != 0:
                                if k == m and l == n:
                                    print(f"Cannot change the same player.")
                                else:
                                    print(f'{k}{l} - {m}{n}')
                                    count += 1

                                if count == 6:
                                    break
                    if count == 6:
                        break
            if count == 6:
                break
    if count == 6:
        break
