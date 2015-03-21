#averaging using a list

numlist = list()
while True:
    inp = raw_input('Enter a number:')
    if inp == 'done' :break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist)/len(numlist)
print 'Sum:', sum(numlist)
print 'Count:', len(numlist)
print 'Average:', average