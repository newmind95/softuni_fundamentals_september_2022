import re


sofia_phone_number = input()
regex = r'(\+359 [\d]{1} [\d]{3} [\d]{4}|\+359-[\d]{1}-[\d]{3}-[\d]{4})\b'
matches = re.findall(regex, sofia_phone_number)
print(', '.join(matches))
