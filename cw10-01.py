fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, value in counts.items():
    lst.append((value, key))

lst.sort(reverse=True)

for key, value in lst[:10]:
    print key, value
    
