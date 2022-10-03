total_price = 0
prices_without_taxes = 0
taxes = 0
command = input()

while not (command == 'special') and not (command == 'regular'):

    price = float(command)

    if price < 0:
        print('Invalid price!')
        command = input()

    prices_without_taxes += price
    taxes += price * (20 / 100)
    total_price = prices_without_taxes + taxes

    command = input()

if total_price > 0:
    print("Congrtulations you've just bought a new computer!")
    if command == 'special':
        print(f'Price without taxes: {prices_without_taxes:.2f}$')
        print(f'Taxes: {taxes:.2f}$')
        print('-----------')
        total_price -= (total_price * (10 / 100))
        print(f'Total price: {total_price:.2f}$')

    elif command == 'regular':
        print(f'Price without taxes: {prices_without_taxes:.2f}$')
        print(f'Taxes: {taxes:.2f}$')
        print('-----------')
        print(f'Total price: {total_price:.2f}$')

elif total_price == 0:
    print('Invalid order!')
