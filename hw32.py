try:
    inp = raw_input("Enter Hours:")
    hours = float(inp)
    inp = raw_input("Enter Rate:")
    rate = float(inp)
except:
    print "Error, please enter numeric input"
    quit()

#print rate, hours
if hours > 40:
    pay = (40 * rate) + (hours - 40)*(rate * 1.5)
else:
    pay = hours * rate
print pay