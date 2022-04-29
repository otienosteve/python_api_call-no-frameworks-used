import json
from urllib import request, parse

params = {
    "api_key": "rJM3VmADEJHGZR2wo6gnANb9TzYVhX5c",
    "limit": "5",
    "q": "willsimith"
}
qrstring = parse.urlencode(params)
print(qrstring)
base_url = 'https://api.giphy.com/v1/gifs/trending?'
req = request.urlopen(base_url + qrstring)
details = parse.urlparse(base_url)
print(details)
print(type(req))

resp = req.read()
print(type(resp))

apires = json.loads(resp)
print(type(apires))

jsondata = json.dumps(apires)
print(type(jsondata))

print(apires["data"][0]["images"]["downsized"]["url"])
