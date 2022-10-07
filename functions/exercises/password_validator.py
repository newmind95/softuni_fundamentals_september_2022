def check_length(password: str) -> bool:
    has_needed_length = 6 <= len(password) <= 10
    return has_needed_length 


def check_alphanumeric(password: str) -> bool:
    return password.isalnum() 


def check_digits(password: str) -> bool:
    counter = 0
    for every_char in password:
        
        if every_char.isdigit():
            counter += 1
    
    has_needed_digits = counter > 2

    return has_needed_digits


some_password = input()
is_valid_length = check_length(some_password)
is_valid_alnum = check_alphanumeric(some_password)
is_valid_digits = check_digits(some_password)
print(is_valid_length, is_valid_alnum, is_valid_digits)
if is_valid_length and is_valid_alnum and is_valid_digits:
    print('Passwor is valid')
elif not is_valid_length:
    print('Password must be between 6 and 10 characters')
elif not is_valid_alnum:
    print('Password must consist only of letters and digits')
elif not is_valid_digits:
    print('Password must have at least 2 digits')
