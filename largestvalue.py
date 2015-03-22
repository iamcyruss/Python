largest_so_far = -1
print 'Before', largest_so_far
for the_num in [5, 20, 94, 55, 44, 88, 76, 62]:
	if the_num > largest_so_far:
		largest_so_far = the_num
	print largest_so_far,the_num
	
print 'After', largest_so_far