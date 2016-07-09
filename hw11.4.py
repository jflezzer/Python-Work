import re
print sum( [ int(i) for i in re.findall('[0-9]+', open(raw_input('Enter file:')).read()) ] )

# open(raw_input('Enter file:)).read()
#   this line prompts for the name of the file and reads it entirely into memory

# re.findall('[0-9]+', open...)
#   this regex expression looks for any numbers in the text

# print sum( [int(i) for i in re.findall...])
#   since the regex re.findall() is going to return a list, we can traverse the list
#   converting the data into integers