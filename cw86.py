#extracting the day of the week from a list

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') :continue
    words = line.split()
    print words[2]
    email = words[1]
    pieces = email.split('@')
    print pieces[0], pieces[1]
