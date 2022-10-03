import re


command = input()
total_amount = 0
pattern = '%(?P<costumer>([A-Z][a-z]+))%<(?P<product>[A-Za-z]+)>\|(?P<count>[\d]+)\|(?P<price>[\d.]+)\$'
while not command == 'end of shift':

    total_price = 0

    matches = re.match(pattern, command)
    if matches:
        name_of_costumer = matches.group('costumer') 
        name_of_product = matches.group('product')
        quantity = int(matches.group('count'))
        price_of_product = float(matches.group('price'))

        total_price = quantity * price_of_product
        total_amount += total_price

        print(f'{name_of_costumer}: {name_of_product} - {total_price:.2f}')

    command = input()

print(f'Total income: {total_amount:.2f}')
