counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]

#simplified counting with get()
for name in names:
    counts[name] = counts.get(name, 0) + 1
print counts