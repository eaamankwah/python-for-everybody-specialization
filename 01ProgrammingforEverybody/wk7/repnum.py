 
while True:
    inp = raw_input("Enter number: ")
    if inp == "done" : break
    try: 
        num = int(inp)
    except:
        print "Invalid input"
        continue
      
# print maximum and minimum numbers

numbers = list(num)
largest = None
smallest = None
for num in numbers :
    if largest == None or largest < num :
        largest = num
for num in numbers : 
    if smallest == None or num < smallest :
        smallest = num
    
print "maximum", largest
print "mininum", smallest