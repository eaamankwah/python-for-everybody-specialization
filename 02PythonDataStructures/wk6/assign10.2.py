fname = raw_input("Enter file name: ") 
fh = open(fname) 
counts = dict()
for line in fh:
    if line.startswith('From '): 
        line = line.split()
        time = line[5]
        time = time.split(':')
        hrs = time[0]
        #for hr in hrs:
        counts[hrs] = counts.get(hrs, 0) + 1
lst = list()
for hrs, count in counts.items():
    #newtup = (val, key)
    lst.append( (hrs, count) )
lst.sort()
for hrs, count in lst:
    print hrs, count
       