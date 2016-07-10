# Import required libraries
import re
import urllib
from BeautifulSoup import *

# Request url, connect and read the page
url = raw_input('Enter a web address - ')
html = urllib.urlopen('http://'+url).read()
soup = BeautifulSoup(html)

# Retrieve all of the span tags
tags = soup('span')

# Print the number of items in the list
print 'Count:',len(tags)

# Print the sum of the numeric values in the list
print 'Sum:',sum([int(i) for i in re.findall('>([0-9]+)<', str(tags))])

    