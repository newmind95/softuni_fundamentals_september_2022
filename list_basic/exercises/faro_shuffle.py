deck_of_cards = input().split()
count_of_shuffle = int(input())
length = len(deck_of_cards) // 2

for shuffle in range(count_of_shuffle):

    final_deck = []
    left_part = deck_of_cards[:length]
    right_part = deck_of_cards[length:]

    for index in range(len(left_part)):
        final_deck.append(left_part[index])
        final_deck.append(right_part[index])

    deck_of_cards = final_deck

print(deck_of_cards)
