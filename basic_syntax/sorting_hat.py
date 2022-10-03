command = input()
sorted_students = True
while not command == 'Welcome!':

    if command == 'Voldemort':
        print('You must not speak of that name!')
        sorted_students = False
        break

    if len(command) < 5:
        print(f'{command} goes to Gryffindor.')

    if len(command) == 5:
        print(f'{command} goes to Slytherin.')

    if len(command) == 6:
        print(f'{command} goes to Ravenclaw.')

    if len(command) > 6:
        print(f'{command} goes to Hufflepuff.')

    command = input()

if sorted_students is True:
    print('Welcome to Hogwarts.')
