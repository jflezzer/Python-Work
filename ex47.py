def getgrade():
    try:
        inp = raw_input("Enter Grade:")
        grade = float(inp)
    except:
        print "Error, please enter numeric input"
        quit()

#check grade value
def errorcheck(grade):
    if grade > 1.0:
        print "Please enter a grade between 0.0 and 1.0"
        quit()
    
#print letter grade
def printgrade(grade):
    if grade >= 0.9:
        print "A"
    elif grade >= 0.8:
        print "B"
    elif grade >= 0.7:
        print "C"
    elif grade >= 0.6:
        print "D"
    else:
        print "F"
        
getgrade(inp)
errorcheck(grade)
printgrade(grade)