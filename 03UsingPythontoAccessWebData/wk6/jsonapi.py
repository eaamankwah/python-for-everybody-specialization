import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = raw_input('Enter location- ')
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(str(data))
location = js['results'][0]['place_id']
print location