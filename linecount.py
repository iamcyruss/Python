tfile = raw_input("Enter files name: ")
numlines = open(tfile)
count = 0
for line in numlines:
	count = count + 1
	
print 'Line Count:', count
