smallest = None
print 'Before'
for value in [5, 20, 94, 55, 44, 88, 76, 62]:
	if smallest is None:
		smallest = value
	elif value < smallest:
		smallest= value
	print smallest, value

print 'After', smallest