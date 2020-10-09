import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
cnt = raw_input('Enter Count - ')
cnt=int(cnt)
pst = raw_input('Enter Position - ')
pst=int(pst)

for i in range (7): # repeat 7 times and position is 18
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
    tags=soup.findAll('a')
    for tag in tags:
        url = tag.get('href', None)
        tags=soup.findAll('a')
        url = tags[pst-1].get('href', None)
print url
        