encrypted_message = input()
command = input()
while not command == 'Decode':
    if 'Move' in command:
        number_of_letters = int(command.split('|')[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    if 'ChangeAll' in command:
        substring = command.split('|')[1]
        replacement = command.split('|')[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    if 'Insert' in command:
        index = command.split('|')[1]
        value = command.split('|')[2]
        encrypted_message = encrypted_message[:int(index)] + value + encrypted_message[int(index):]
    command = input()

print(f'The decrypted message is: {encrypted_message}')
