# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
count=0
value = 0
total=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    num = float(line[pos+1:])
    total=total+num
    count = count+1    
print "Average spam confidence:", total/count