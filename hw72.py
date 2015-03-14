# Use the file name mbox-short.txt as the file name
#prompt for file name
try:
    fname = raw_input("Enter file name: ")
    #open the file
    fh = open(fname)
except:
    print 'File',fname + ' cannot be found. Please try again.'
    exit()
    
#initialize variables for summing the spamminess of an email and to count the number of emails that are spammy
spamminess = 0
count = 0

#read through the file looking for lines that start with 'X-DSPAM-Confidence'
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    start = line.find(':')
    end =line.find('\n')
    value = line[start+1: end]
 #   print start+1, end-1, value -- this was my check to show the location of the numeric values
    
    #extract the floating point values from each line    
    spamminess = spamminess + float(value)
    count = count + 1

#compute the average of those values using label "Average spam confidence: nnn"
print 'Average spam confidence:',spamminess/count



