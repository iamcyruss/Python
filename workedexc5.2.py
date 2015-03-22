count = 0
total = 0
while True:
    inp = raw_input('Enter a number: ')
    
    # handle the edge cases
    if inp == 'done' : break
    if len(inp) < 1 : break   # check for empty line
    
    # do the work
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue #will not run the next 3 lines so all that is outputted is invalid input without the numbers
    count = count + 1
    total = total + num
    print num, total, count

print 'Average:', total / count