# Use words.txt as the file name
try:
	fname = raw_input("Enter file name: ")
	fh = open(fname)
except:
	print "File name not found: ",fname
	exit()

for line in fh:
	line = line.rstrip()
	words = line.upper()
	print words
