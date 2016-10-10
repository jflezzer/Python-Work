import urllib
import xml.etree.ElementTree as ET

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)
    #convert the data to a list for all of the comments
    lst = tree.findall('.//comment')
    print 'Count:', len(lst)
    summary = 0
    for item in lst:
        summary = int(item.find('count').text) + summary
    print 'Sum:',summary
