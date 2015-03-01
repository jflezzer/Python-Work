#defines the iteration variable
smallest_so_far = -1

print 'Before',smallest_so_far

#the_num is an iteration variable that takes on the value of each item in the sequence as it goes through the loop
for the_num in [9,41,12,3,74,15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print smallest_so_far, the_num

print 'After', smallest_so_far

#running this code fails to produce any results, because smallest_so_far is set at -1