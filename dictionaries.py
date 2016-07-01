word = 'mississippi'
dictionary = dict()
for letter in word:
    dictionary[letter] = dictionary.get(letter,0) + 1
        
print dictionary

