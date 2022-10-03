import re


string = input()
pattern = r'\d+'
while string:

    matches = re.findall(pattern, string)
    if matches:
         print(' '.join(matches), end=' ')
    else:
        break

    string = input()
