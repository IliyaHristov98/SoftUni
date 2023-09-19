males_count = int(input())
females_count = int(input())
tables_max = int(input())
tables_count = 0
tables_full = False
for man in range(1, males_count + 1):
    for woman in range(1, females_count + 1):
        print(f'({man} <-> {woman})', end=" ")
        tables_count += 1
        if tables_count == tables_max:
            tables_full = True
            break
    if tables_full:
        break
