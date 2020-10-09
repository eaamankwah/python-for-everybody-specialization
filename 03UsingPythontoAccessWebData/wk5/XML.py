#: http://python-data.dr-chuck.net/comments_42.xml
#: http://python-data.dr-chuck.net/comments_271091.xml
import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter - ')
html = urllib.urlopen(url).read() # read the content of the url as string
sum=0
# change string content into xml tree
tree = ET.fromstring(html)
counts = tree.findall('comments/comment/count') # find all count elements
# extract the value of each count element and sum them.
for count in counts:
    sum = sum + int(count.text)
print 'Sum: ', sum 
   