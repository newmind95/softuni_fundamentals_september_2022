command = input()
counter_coffee = 0
while not command == 'END':

    if command.isupper():
        if command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
            counter_coffee += 2 

    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        counter_coffee += 1 

    command = input()

if counter_coffee > 5:
    print('You need extra sleep')
else:
    print(counter_coffee)
