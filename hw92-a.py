name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


emails = list()
senders = dict()

for line in handle:
    if not line.startswith('From'):continue
        