def computepay():
    try:
        inp = raw_input("Enter hours:")
        h = float(inp)
        inp = raw_input("Enter rate:")
        r = float(inp)
    except:
        print "Error, please enter numeric input"
        quit()

    if h > 40:
        pay = (h - 40)*(r * 1.5) + (40 * r)
    else:
        pay = (h * r)
    return pay

pay = computepay()
print pay