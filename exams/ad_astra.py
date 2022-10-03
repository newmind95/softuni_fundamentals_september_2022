import re


text_string = input()
pattern = r'(#|\|)([A-Za-z\s]+)\1([\d]{2}/[\d]{2}/[\d]{2})\1(\d{1,5})\1'
total_calories = 0
result = []
matches = re.findall(pattern, text_string)
for match in matches:
    total_calories += int(match[3])

total_calories //= 2000
print(f'You have food to last you for: {total_calories} days!')
for match in matches:
    print(f'Item: {match[1]}', end=', ')
    print(f'Best before: {match[2]}', end=', ')
    print(f'Nutrition: {match[3]}')
