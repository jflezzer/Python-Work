name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#declare our variables
emails = list()
senders = dict()
bigSender = None
bigFreq = None

#find the lines that begin with 'From'

for line in handle:
    if not line.startswith('From'):continue
        #split the text of the line into a list
        emails = line.split()
        #extract the 2nd word from the list and add it to the dictionary
        for email in emails:
            senders[email] = emails[2].get

#loop through the dictionary selecting the most frequent sender and the frequency