import re
text = open('regex_sum_42.txt')
data = text.read()
numlist = list()
for line in data:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    if len(stuff) !=1 : continue
    num = int(stuff[0])
    numlist.append(num)
print sum(num)
