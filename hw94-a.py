name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#declare our variables
emails = list()
senders = dict()

#find the lines that begin with 'From'

for line in handle:
    line = line.rstrip()
    if not line.startswith('From:'):continue
    emails = line.split()
    senders[emails[1]] = senders.get(emails[1],0) + 1

# this is the idiom for searching a key, value set for the highest value
# these variables aren't needed until this loop is ready to run
bigSender = None
bigFreq = 0

for key, value in senders.items():
    if value > bigFreq:
        bigSender = key
        bigFreq = value
        
print bigSender, bigFreq