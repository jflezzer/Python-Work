# Use the file name mbox-short.txt as the file name
try:
	fname = raw_input("Enter file name: ")
	fh = open(fname)
except:
	print 'Incorrect file name - please enter mbox-short.txt'
	quit()

#declare variables needed
count = 0
confid = 0

#process the file
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    confid = confid + float(line[line.find('0') :len(line)])

val = confid / count

print 'Average spam confidence: ' + str(val)