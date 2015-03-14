# Use words.txt as the file name
#prompt for file name
fname = raw_input("Enter file name: ")
#open file
fh = open(fname)

#read through the file
for word in fh:
    word = word.rstrip()
#print contents of the file in upper case
    print word.upper()
    

