#: http://python-data.dr-chuck.net/comments_42.json 
#: http://python-data.dr-chuck.net/comments_271095.json
import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_42.json'
url = raw_input('Enter json URL- ')
uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(data)
counts = []
comments = js["comments"]
for comment in comments:
    counts.append(comment['count'])
print sum(counts)
















