import string

fname = raw_input("Enter the file name:")
try:
    fhandle = open(fname)
except:
    print "File cannot be opened:", fname
    exit()
    
counts = dict()
for line in fhandle:
    line = line.translate(None, string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
for key, value in counts.items():
    print key, value
