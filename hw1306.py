import urllib
import json

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    
    print 'Retrieving', address
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    info = json.loads(data)
    
    #declare iteration variables
    total = 0
    i = 0
    user_count = 0
    
    #loop through comments section of dictionary
    for item in info['comments']:
        user_count = user_count + 1
        total = total + int(info['comments'][i]['count'])
        i = i + 1
        
    print 'Count:', user_count
    print 'Sum:', total
    
