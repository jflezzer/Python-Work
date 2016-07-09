import re

file_name = raw_input('Enter a file to search: ')
fhand = open(file_name)
regex = raw_input('Enter a regular expression: ')

count = 0

for line in fhand:
    line = line.strip()
    if re.search(regex, line):
        count = count + 1

print file_name, 'had', count, 'lines that matched', regex