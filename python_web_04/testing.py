import mimetypes
import urllib.parse
from datetime import datetime
import json

route = urllib.parse.urlparse('http://localhost:3000')
# print(route.netloc)

mime_type, *mt = mimetypes.guess_type('filename.mp3')
# print(mt)

# print(datetime.now())


data = b'username=Gerenzeo&message=Lets+play%21'.decode()
data = urllib.parse.unquote_plus(data)

data = {str(datetime.now()): {key: value for key, value in [el.split('=') for el in data.split('&')]}}

# print(data)

with open('storage/data.json', 'rb') as fd:
    data = json.load(fd)

print(data)