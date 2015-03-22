try:
    hours = raw_input("Enter Hours ")
    hours = float(hours)
    rate = raw_input("Enter Pay Rate ")
    rate = float(rate)
    regularhours = float(hours*rate)
    fulltime = float(80*rate)
    othours = float(hours-80)
    
except:
    print "Error, that is not a number."
    quit()

if hours <= 80:
    print fulltime
else:
    overtimepay = float(rate/2)
    overtimepay = float((overtimepay+rate)*othours)
    ot = float(fulltime+overtimepay)
    gross = float(ot-(ot*.28))
print('Gross Pay = ' + str(ot))
print('After Everything = ' + str(gross))
