import re
text = open('regex_sum_42.txt')
data=text.read()
print sum(map(int,re.findall(r"\b\d+\b",data)))