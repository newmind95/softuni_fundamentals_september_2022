import unittest


def has_20_chars(string):
    if len(string) == 20:
        return True
    
    return False


def is_valid_ticket(string):
    if '@' in string:
        return True

    elif '#' in string:
        return True

    elif '$' in string:
        return True

    elif '^' in string:
        return True
    
    else:
        return False


def check_symbols_in_both_sides(string:str , symbol: str):
    half = len(string) // 2
    left_half = string[:half]
    right_half = string[half:]
    if left_half.count(symbol) == 6 and right_half.count(symbol) == 6:
        return True

    return False


def check_jackpot_winning(string: str, symbol: str):
    half = len(string) // 2
    left_half = string[:half]
    right_half = string[half:]
    if left_half.count(symbol) == 10 and right_half.count(symbol) == 10:
        return True

    return False
    


class TestExercises(unittest.TestCase):
    
    def test_20_equal_chars(self):
        string = 'Cash$$$$$$Ca$$$$$$sh'
        expected = True
        result = has_20_chars(string)
        self.assertEquals(result, expected, 
                'The string has 20 characters')
    

    def test_20_above_chars(self):
        string = 'Cash$$$$$$Ca$$$$$$s'
        expected = False 
        result = has_20_chars(string)
        self.assertEquals(result, expected,
                'The string has less than 20 characters')

    
    def test_monkey_symbol(self):
        string = '@@sg@@'
        result = is_valid_ticket(string)
        expected = True
        self.assertEquals(result, expected,
                'The string contain @')        
    

    def test_hashtag_symbol_in_string(self):
        string = 'Cas#####sh#######'
        expected = True
        result = is_valid_ticket(string)
        self.assertEquals(result, expected, 
                'The string contain #')
    
    def test_different_symbol(self):
        string = 'Ca(((sh)))'
        result = is_valid_ticket(string)
        expected = False
        self.assertEquals(result, expected,
                'The string contains different symbol.')


    def test_string_contain_6_symbols(self):
        string = 'Cash$$$$$$Ca$$$$$$sh'
        symbol = '$'
        expected = True
        result = check_symbols_in_both_sides(string, symbol)
        self.assertEquals(result, expected, 
                'The string contains 6 symbols')


    def test_string_contains_5_symbols(self):
        string = 'Cash$$$$$Ca$$$$$sh'
        symbol = '$'
        expected = False
        result = check_symbols_in_both_sides(string, symbol)
        self.assertEquals(result, expected,
                'The string contains 5 symbols')

    
    def test_jackpot_winning(self):
        string = '$$$$$$$$$$$$$$$$$$$$'
        symbol = '$'
        expected = True
        result = check_jackpot_winning(string, symbol)
        self.assertEquals(result, expected,
                'The string is jackpot')


    def test_not_winning_jackpot(self):
        string = '$$$$$$$$$$$$$$$$$$$'
        symbol = '$'
        expected = False
        result = check_jackpot_winning(string, symbol)
        self.assertEquals(result, expected,
                'The string is not winning jackpot')


unittest.main()
        
