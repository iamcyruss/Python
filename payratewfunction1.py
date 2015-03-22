def computepay(h,r):
    if h > 80:
        gross = ((h-80)*((r/2)+r))+(80*r)
        total = gross-(gross*.275)
        print gross
        return total
    else:
        gross = (r*h)
        total = gross-(gross*.275)
        print gross
        return total

try:
    hrs = raw_input("Enter Hours: ")
    hrs = float(hrs)
    rte = raw_input("Enter Rate: ")
    rte = float(rte)
    p = computepay(hrs,rte)
    print p

except:
    print "Error, that is not a number."
    quit()