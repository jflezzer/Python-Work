counts = {"chuck" : 1, "fred" : 42, "jan" : 100}
for key in counts:
    print key, counts[key]
    
print list(counts)
print counts.keys()
print counts.values()
print counts.items()

# two iteration variables
# other programming languages don't have this feature
for key, value in counts.items():
    print key, value
    