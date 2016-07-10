import urllib
from BeautifulSoup import *

url = raw_input('Enter a web address - ')
html = urllib.urlopen('http://'+url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print 'TAG:', tag
    print 'URL:',tag.get('href', None)
    print 'Content:',tag.contents[0]
    print 'Attrs:',tag.attrs
    