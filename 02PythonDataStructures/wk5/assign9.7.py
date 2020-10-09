fname = raw_input("Enter file name: ") 
fh = open(fname) 
emails = dict()
for line in fh:
    if line.startswith('From '):
        line = line.split()
        email = line[1]
        emails[email] = emails.get(email,0) + 1
largest = None
for kee in emails:
    if largest is None or emails[kee] > largest:
        largest = emails[kee]
        maxkee = kee  
print maxkee, largest
