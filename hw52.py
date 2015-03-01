# establishes variables largest and smallest
# sets their starting value to None
largest = None
smallest = None

#While Loop used becaused the number of inputs in the sequence are unknown
while True:
    # try/except will take the raw input and convert its type to an integer if it's a number
    try:
        inp = raw_input("Enter a number: ")
        if inp == "done": break
        num = int(inp)
    except:
        print "Invalid input"
        continue
    
    # the Loop first sets the initial values of the variables
    if largest is None and smallest is None:
        largest = num
        smallest = num
    # then compares the variables to the next input
    elif largest < num:
        largest = num
    elif smallest > num:
        smallest = num
    
print "Maximum is", largest
print "Minimum is", smallest