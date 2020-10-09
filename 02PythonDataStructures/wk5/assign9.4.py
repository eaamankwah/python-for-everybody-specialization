fname = raw_input("Enter file name: ") 
#count = 0
fh = open(fname) 
lst = list()                       
for line in fh:                    
    line = line.rstrip()     
    if not line.startswith('From ') : continue               
    words = line.split()
    words.append(line[1])    
    
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
maxval = None
maxkee = None
for kee,val in counts.items() :
    if maxval == None or maxval < val :
        maxval = val
        maxkee = kee
print maxkee, maxval

