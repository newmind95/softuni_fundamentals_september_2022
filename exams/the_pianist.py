number_of_pieces = int(input())
dictionary = {}
for line in range(number_of_pieces):
    tokens = input().split('|')
    piece = tokens[0]
    composer = tokens[1]
    key = tokens[2]
    dictionary[piece] = [composer, key]

command = input()
while not command == 'Stop':

    if 'Add' in command:
        tokens = command.split('|')
        piece = tokens[1]
        composer = tokens[2]
        key = tokens[3]
        if piece in dictionary:
            print(f'{piece} is already in the collection!')
        else:
            dictionary[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')

    elif 'Remove' in command:
        piece = command.split('|')[1]
        if piece in dictionary:
            dictionary.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif 'ChangeKey' in command:
        piece, new_key = command.split('|')[1], command.split('|')[2]
        if piece in dictionary:
            dictionary[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.') 

    command = input()

for piece, composer_key in dictionary.items():
    print(f'{piece} -> Composer: {composer_key[0]}, Key: {composer_key[1]}')
