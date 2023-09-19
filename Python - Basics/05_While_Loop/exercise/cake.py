width = int(input())
length = int(input())
eaten_pieces = 0
total_pieces = width * length
eaten = True

while total_pieces > eaten_pieces:
    pieces_taken = input()
    if pieces_taken == 'STOP':
        if eaten_pieces < total_pieces:
            eaten = False
            break
    else:
        eaten_pieces += int(pieces_taken)

if not eaten:
    print(f'{total_pieces - eaten_pieces} pieces are left.')
elif eaten:
    print(f'No more cake left! You need {eaten_pieces - total_pieces} pieces more.')
