import re

pattern = r'((w{3})\.([A-Za-z0-9]+)(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
valid_urls = []
string = input()
while string:

    matches = re.search(pattern, string)
    if matches:
        valid_urls.append(matches[0])

    string = input()

for valid_url in valid_urls:
    print(valid_url)
