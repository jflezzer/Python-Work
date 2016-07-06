fname = raw_input('Enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)

counts = dict()
emails = list()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        #emails = words[1]
        for word in words:
            counts[word] = counts.get(word,0)+1

for key, val in counts.items():
    if key.__contains__('@'):
        emails.append((val, key))

emails.sort(reverse=True)

for key, val in emails[:1]:
    print val, key
            


