deck_of_cards = input().split()
faro_shuffles_count = int(input())
left_part = []
right_part = []

for shuffle in range(faro_shuffles_count):
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]
    final_disposition = []

    for index in range(len(left_part)):
        final_disposition.append(left_part[index])
        final_disposition.append(right_part[index])
        deck_of_cards = final_disposition
print(final_disposition)
