
# import libraries
import re
import urllib
from BeautifulSoup import *

#declare variables
# Note: these are being declared as integers; however the input will be strings
# the program converts them back to integers later on
pos = 0
count = 0

# get the starting URL
url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')

# get the count and position    
count = raw_input('Enter count: ')
pos = raw_input('Enter position: ')    

# there's probably a more elegant way to do this; however, this method works
# x is equal to 2 because the first name is the name in the URL
# the second name is the name at the position-1 since lists enumerate 0,1,2...
x = 2

print re.findall('_([A-Z][a-z]+)\.', url)
print re.findall('_([A-Z][a-z]+)\.', str(tags[int(pos)-1]))

# the while loop opens each URL in the position-1 in the list
# it reads the file and extracts the href info
# it then extracts the name from the href and prints it for the number of count-2
while x <= int(count):
    html = urllib.urlopen(tags[int(pos)-1].get('href', None)).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print re.findall('_([A-Z][a-z]+)\.', str(tags[int(pos)-1]))
    x = x + 1
