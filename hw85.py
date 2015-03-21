try:
    fname = raw_input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    fh = open(fname)
except:
    print 'File not found'
    exit()

count = 0
emails = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') :continue
    emails = line.split()
    print emails[1]
    #you need to use a count variable because the length of the list is reset with each line
    count = count + 1

print "There were", count, "lines in the file with From as the first word"