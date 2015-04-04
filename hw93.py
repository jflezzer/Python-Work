try:
    fname = raw_input("Enter file: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    fhandle = open(fname)
except:
    print "File not found:", fname
    exit()
    
counts = dict()
emails = list()
most_emails = 0
person = str()

for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From ') :continue
    words = line.split() #splits the line into words
    user = words[1] #grabs the email address from each line
    emails.append(user) #appends the email address to the list of emails
    counts[user] = counts.get(user, 0) + 1 #adds the email address and count to the dictionary
    
for key, value in counts.items():
    if value > most_emails:
        most_emails = value
        person = key

print person, most_emails
