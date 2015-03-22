data = 'From slslslslslslslslslsls@something.gbl.hq Sat Jan 1 00:00:00 1900'
atpos = data.find('@')
print atpos

spacepos = data.find(' ',atpos)
print spacepos

host = data[atpos+1:spacepos] # : sign is for slicing text
print host

#this is parsing text -  find this or find that 23 28