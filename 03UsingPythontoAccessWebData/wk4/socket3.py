import urllib
import re
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_42.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
sum=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    y=str(tag)
    x= re.findall("[0-9]+",y)
    for i in x:
        i=int(i)
        sum=sum+i
print sum