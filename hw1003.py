file = open("mbox-short.txt")

words = list()
counts = dict()
chars = list()

for line in file: # loops through each line of the file
    lower = line.lower() # converts the line to lowercase
    words = lower.split() # splits each word out of the line
    for word in words: # loops through each word in the words list
        for char in word: # loops through each character in each word
            if char.isalpha(): # evaluates whether the character is alphabetical
                counts[char] = counts.get(char, 0) + 1 # adds the alphabetical characters to the counts dictionary

lst = list() 

for k, v in counts.items():
    lst.append((v, k))
    
lst.sort(reverse=True)

for k,v in lst:
    print k, v
    