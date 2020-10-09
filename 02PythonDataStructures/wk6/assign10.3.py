fname = raw_input("Enter file name: ") 
fh = open(fname) 
counts = dict()
for line in fh:
    if not line.startswith('From '): continue
    line = line.split()
    time = line[5]
    time = time.split(':')
    hrs = time[0]
               
    for hr in hrs:
        counts[hr] = counts.get(hr, 0) + 1
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append( (val, key) )
lst.sort(reverse=True)
for key, val in lst[:] :
    print key, val
       