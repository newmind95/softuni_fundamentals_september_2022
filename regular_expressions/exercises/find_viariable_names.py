import re


string = input()
pattern_to_find_var_names = r'\b_([A-Za-z0-9]+)\b'
find_all_patterns = re.findall(pattern_to_find_var_names, string)
print(','.join(find_all_patterns))
