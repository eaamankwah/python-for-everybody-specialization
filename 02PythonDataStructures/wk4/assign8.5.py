fname = raw_input("Enter file name: ") 
count = 0
fh = open(fname) 
lst = list()                       
for line in fh:                    
    line = line.rstrip()     
    if not line.startswith('From ') : continue               
    words = line.split()  
    count =  count + 1
    print words[1]
print "There were", count, "lines in the file with From as"   
 