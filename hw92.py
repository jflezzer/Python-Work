import string

fname = "mbox-short.txt"
try:
    fhandle = open(fname)
except:
    print "File cannot be opened:", fname
    exit()
    
counts = dict()
days = list()

for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From ') :continue
    words = line.split()
    day = words[2]
    days.append(day)
    counts[day] = counts.get(day, 0) + 1
    
print counts
