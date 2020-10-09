fname = raw_input("Enter file name: ") 
if len(fname) < 1 : fname = "mbox-short.txt"
fname = "mbox-short.txt"
fh = open(fname) 
text = fh.read()

words = list()                       
for line in fh:                    
    #line = line.rstrip()     
    if not line.startswith("From ") : continue               
    line = line.split()
    words.append(line[1])    
    
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
maxval = None
maxkee = None
for kee,val in counts.items() :
    if maxval is None or maxval < val :
        maxval = val
        maxkee = kee
print maxkee, maxval
