def is_valid_ticket(string:str):
    if len(string) == 20:
        return True

    return False


def founded_symbol(string: str):
    symbol = ''
    if '@' in string:
        symbol = '@'
    elif '#' in string:
        symbol = '#'
    elif '$' in string:
        symbol = '$'
    elif '^' in string:
        symbol = '^'

    return symbol

def left_right_half(string: str):
    return string[:len(string) // 2], string[len(string) // 2:]


def count_winning_symbols(string: str, symbol: str, number_of_occurrence: int):
    return string.count(symbol) >= 6


def count_jackpot_symbols(string: str, symbol: str, number_of_occurrence: int):
    return string.count(symbol) == number_of_occurrence 


def is_winning_ticket(string: str):
    left_half, right_half = left_right_half(string)
    symbol = founded_symbol(string)
    if count_winning_symbols(left_half, symbol, 6) == count_winning_symbols(right_half, symbol, 6):
        return True

    return False


def is_ticket_jackpot(string: str):
    left_half, right_half = left_right_half(string)
    symbol = founded_symbol(string)
    if count_jackpot_symbols(left_half, symbol, 10) == count_jackpot_symbols(right_half, symbol, 10):
        return True

    return False
    

ticket = input().split(', ')
for every_ticket in ticket:
    every_ticket = every_ticket.strip()

    if not is_valid_ticket(every_ticket):
        print('invalid ticket')
    
    elif is_valid_ticket(every_ticket) and not is_winning_ticket(every_ticket):
        print(f'ticket "{every_ticket}" - no match')

    elif (is_valid_ticket(every_ticket) and is_winning_ticket(every_ticket)) \
            and not is_ticket_jackpot(every_ticket):
        print(f'ticket - "{every_ticket}" - 6{founded_symbol(every_ticket)}')
   
    elif is_ticket_jackpot(every_ticket):
       print(f'ticket "{every_ticket}" - 10{founded_symbol(every_ticket)} Jackpot!')
