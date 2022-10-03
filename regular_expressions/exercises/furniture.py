import re


pattern = r'^>>([a-zA-z]+)<<([\d+]|[\.\d]+)!([\d]+)'
total_money_spend = 0
bought_furniture = []

command = input()
while not command == 'Purchase':

    furniture_name = ''
    price = 0
    quantity = 0
    matches = re.findall(pattern, command)
    for match in matches:
        furniture_name = match[0]
        price = float(match[1])
        quantity = int(match[2])
        bought_furniture.append(furniture_name)

    total = price * quantity

    total_money_spend += total

    command = input()

print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)

print(f'Total money spend: {total_money_spend:.2f}')
