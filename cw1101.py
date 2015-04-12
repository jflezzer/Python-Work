hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if line.startswith("From:") >= 0:
        print "Using line.startswith", line
        
        
import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line):
        print "Using Regex:", line