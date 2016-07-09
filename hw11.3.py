import re

file_name = raw_input('Enter file: ')
if len(file_name) < 1:
    file_name = 'regex_sum_42.txt'
fhand = open(file_name)

total = 0

for line in fhand:
    valstr = re.findall('([0-9]+)', line)
    for val in valstr:
        total = total + int(val)

print total