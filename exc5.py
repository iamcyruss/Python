largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    
    if num == "done" : break
 
    try:
        num = int(num)
        for the_num in [num]:
            if largest is None:
                largest = the_num
            elif the_num > largest:
                largest = the_num
            if smallest is None:
                smallest = the_num
            elif the_num < smallest:
                smallest = the_num

    except:
        print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest