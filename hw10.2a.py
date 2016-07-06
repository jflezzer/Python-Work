fname = raw_input('Enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)

counts = dict()
hours = list()
hrList = list()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        for word in words:
            if word.__contains__(':'):
                hours.append(word[:word.find(':')])

for hour in hours:
    counts[hour] = counts.get(hour,0)+1


for key, val in counts.items():
    hrList.append((key, val))
    
hrList.sort()

for key, val in hrList:
    print key, val
            


