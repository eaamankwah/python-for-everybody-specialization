largest = None
smallest = None
while True:
    inp = raw_input("Enter number: ")
    if inp == "done" : break
    try: 
        num = int(inp)
    except:
        print "Invalid input"
        continue
      
# print maximum and minimum numbers

    if largest == None or largest < num :
        largest = num
 
    if smallest == None or num < smallest :
        smallest = num
    
print "Maximum is", largest
print "Mininum is", smallest