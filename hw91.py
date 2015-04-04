# opens the words.txt file
file_handle = open("words.txt")

dictionary = dict()
for line in file_handle:
    words = line.split()
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

print "Printing the dictionary contents"
print dictionary

print "Printing the dictionary as tuples"
print dictionary, dictionary[word]