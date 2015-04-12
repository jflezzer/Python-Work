try:
    name = raw_input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
except:
    print "File not found:", name
    exit()
    
counts = dict()
words = list()
letter = list()

for line in handle:
    line = line.strip().lower()
    words = line.split() # splits the line into words
    for word in words:
        words.append(word)
    for char in words:
        print char.lower() # grabs the letter from each line
        #print ltr
        #    hour = hms[:2] # extracts the hour from the letter
#    letter.append(ltr) # appends the hour to the list of hours
#    counts[letter] = counts.get(letter, 0) + 1 # adds the hour and count to the dictionary
    
#h = list() # creates an empty list for the hour, count tuples

#for k,v in counts.items(): # loops through each tuple
#    h.append((k, v)) # appends each key-value pair to the list
#h.sort() # sorts the list by key
#for k,v in h:
#    print k, v 

    