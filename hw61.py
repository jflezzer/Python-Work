text = "X-DSPAM-Confidence:    0.8475";

start = text.find(':')
#end = text.find('5')
print text[start+1:]
number = float(text[start+1:])
print number


    