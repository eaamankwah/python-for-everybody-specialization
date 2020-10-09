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

    if smallest == None or smallest > num :
        smallest = num
 
    if largest == None or num > largest :
        largest = num
    
print "Maximum", largest
print "Mininum", smallest