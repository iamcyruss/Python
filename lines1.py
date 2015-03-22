fh = open("logexp-2015-02-21.txt", "r")

count = 0
for line in fh:
    print line.strip()
    count = count + 1

print count,"Lines"