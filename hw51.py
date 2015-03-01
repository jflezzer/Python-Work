count = 0
total = 0

#While Loop used because the number of inputs in the sequence are unknown
while True:
    # try/except will take the raw input and convert its type to an integer if it's a number
    try:
        inp = raw_input("Enter a number: ")
        if inp == "done": break
        if len(inp) < 1: break
        
        num = float(inp)
        count = count + 1
        total = total + num
        print num, total, count
    except:
        print "Invalid input"
        continue
        
print "Average", total / count