import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_42.xml'

while True:
    address = serviceurl
    #raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)

    for item in data:
        count = tree.find('count').text
        print count
        
    #results = tree.findall('.//count').text
    #print results