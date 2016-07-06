fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
# by using the raw_input with a prompt to press a key to continue, you effectively put a pause in the program. this is useful for testing code during the development process

print 'Contents of the Dictionary variable: Counts'
print counts
raw_input('Press a key to continue...')
print
        
lst = list()
for key, val in counts.items():
    lst.append((val, key))

print 'Contents of the List variable: lst'
print lst
raw_input('Press a key to continue...')
print

lst.sort(reverse=True)

for val, key in lst[:10]:
    print key, val