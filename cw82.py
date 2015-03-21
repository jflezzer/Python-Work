#range function
print 'The range of 4 is:'
print range(4)

friends = ['Joseph', 'Glenn', 'Sally']
print friends[0]
print friends[1]
print friends[2]
print 'The number of friends is:'
print len(friends)

print 'The range of friends is'
print range(len(friends))

#using loops
for friend in friends:
    print 'Happy New Year:', friend
    
for i in range(len(friends)):
    friend = friends[i]
    print 'Happy New Year:', friend