import re


number_of_messages = int(input())
DECRYPTING_PATTERN = r'[star]|[STAR]'
FINAL_PATTERN = r'.*\@([A-Z][a-z]+)[^\@\:\!\-\>]*:([\d]+)*!([AD])\!->([\d]+).*'
attacked_planets = []
destroyed_planets = []
for message in range(number_of_messages):

    encrypted_message = input()
    count_of_letters = []
    message = ''
    matches = re.findall(DECRYPTING_PATTERN, encrypted_message)

    for match in matches:
        count_of_letters.append(match)
    
    for index in range(len(encrypted_message)):
        message += chr(ord(encrypted_message[index]) - len(count_of_letters))
    
    matches = re.findall(FINAL_PATTERN, message)
    for match in matches:
        attack_type = match[2]
        if attack_type == 'A':
            attacked_planets.append(match[0])
        elif attack_type == 'D':
            destroyed_planets.append(match[0])

print(f'Attacked planets: {len(attacked_planets)}')
if len(attacked_planets) > 0:
    for every_planet in sorted(attacked_planets):
        print(f'-> {every_planet}')

print(f'Destroyed planets: {len(destroyed_planets)}')
if len(destroyed_planets) > 0:
    for every_planet in sorted(destroyed_planets):
        print(f'-> {every_planet}')
