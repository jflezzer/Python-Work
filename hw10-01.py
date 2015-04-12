try:
    fname = raw_input("Enter file: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    fhandle = open(fname)
except:
    print "File not found:", fname
    exit()
    
counts = dict()
emails = list()
#most_emails = 0
#person = str()

for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From ') :continue
    words = line.split() #splits the line into words
    user = words[1] #grabs the email address from each line
    emails.append(user) #appends the email address to the list of emails
    counts[user] = counts.get(user, 0) + 1 #adds the email address and count to the dictionary

lst = list()
for key, value in counts.items():
    lst.append((value, key))

lst.sort(reverse=True)

for key, value in lst[:1]:
    print value, key