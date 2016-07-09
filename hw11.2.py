import re

file_name = raw_input('Enter file: ')
fhand = open(file_name)

count = 0
val = float

for line in fhand:
    line = line.strip()
    if re.search('^New Revision: [0-9]+', line):
        valstr = re.findall('^New Revision: ([0-9]+)', line)
        val = float(valstr[0])
        count = count + 1

print val / count    
#print file_name, 'had', count, 'lines that matched', regex