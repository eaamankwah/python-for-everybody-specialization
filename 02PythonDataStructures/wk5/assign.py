fname = raw_input("Enter file name: ") 
count = 0
fh = open(fname) 
lst = list()                       
for line in fh:                    
    line = line.rstrip()     
    if not line.startswith('From ') : continue               
    words = line.split()  
    counts = dict()
    for word in words:
        counts[word] = counts.get(word,0) + 1
    bigcount = None
    bigword = None
    for word, count in counts.items() :
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
    print bigword, bigcount

