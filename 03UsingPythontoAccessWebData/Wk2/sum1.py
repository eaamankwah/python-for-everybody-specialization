import re
fname = raw_input("Enter file name: ") 
fh = open(fname) 
data = fh.read()
numlist = list()
for line in data:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    numlist=numlist+stuff
sum=0
for i in numlist:
    sum=sum+int(i)
print sum