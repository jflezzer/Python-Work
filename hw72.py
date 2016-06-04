# Use the file name mbox-short.txt as the file name
try:
	fname = raw_input("Enter file name: ")
	fh = open(fname)
except:
	print 'File not found:',fname
	exit()
val = ""

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
    	for letter in line:
    		if not letter.isdigit(): continue
    		else:
    			val = val.join()
    	print val
print "Done"