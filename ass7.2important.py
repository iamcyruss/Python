# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox-short.txt'
try:   
    fh = open(fname)
except:
    print 'File cannot be opened.', fname
    exit()

count = 0
grand = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"): continue
    count = count + 1
    zero = line.find('0')
    num = line[zero:zero+6]
    num = float(num)
    grand = grand + num
        
fin = grand / count
print 'Average spam confidence:',fin
