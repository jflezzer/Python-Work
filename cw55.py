#defines the iteration variable
smallest = None
print 'Before'
#value is an iteration variable that takes on the value of each item 
#in the sequence as it goes through the loop
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print smallest, value
print 'After', smallest