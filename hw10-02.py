try:
    name = raw_input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
except:
    print "File not found:", name
    exit()
    
counts = dict()
time = list()

for line in handle:
    line = line.strip()
    if not line.startswith('From ') :continue
    words = line.split() # splits the line into words
    hms = words[5] # grabs the time from each line
    hour = hms[:2] # extracts the hour from the time
    time.append(hour) # appends the hour to the list of hours
    counts[hour] = counts.get(hour, 0) + 1 # adds the hour and count to the dictionary
    
h = list() # creates an empty list for the hour, count tuples

for k,v in counts.items(): # loops through each tuple
    h.append((k, v)) # appends each key-value pair to the list
h.sort() # sorts the list by key
for k,v in h:
    print k, v 

    