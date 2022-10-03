budget, some_commands = int(input()), input()
is_overdraft = False
while not some_commands == 'End':
    price = int(some_commands)
    budget -= price
    if budget < 0:
        is_overdraft = True
        break
    some_commands = input()

print('You bought everything needed.' 
        if not is_overdraft else 'You went in overdraft!')
