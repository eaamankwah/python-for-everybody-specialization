name = raw_input("Enter file name: ") 
fh = open(name)

cou = dict()
for line in fh:                    
 
    if line.startswith('From ') : continue               
    words = line.split()  

maxval = None
maxkee = None
for kee,val in cou.items() :
    if maxval == None or maxval < val :
        maxval = val
        maxkee = kee
print maxkee, maxval
    
    
    