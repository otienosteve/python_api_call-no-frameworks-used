from app import app
from urllib import request, parse
import json

requestVariables={
    "api_key": '22f3e85e05becdb7e502c1f391dbd90d',
    'limit': '10'
    }

encodeVars = parse.urlencode(requestVariables)
print(encodeVars)

API_BASE_URL = 'https://api.themoviedb.org/3/movie/popular?'
print(type(API_BASE_URL))

req_open = request.urlopen(API_BASE_URL + encodeVars)
print(req_open)

req_read = req_open.read()
print(type(req_read))

req_json = json.loads(req_read)
print(type(req_json))
print('=' * 50)

print(req_json["results"][0]['title'])
print(req_json["results"][0]['poster_path'])
print(req_json["results"][0]['release_date'])
print(req_json["results"][0]['vote_count'])
print('=' * 50)

print(req_json["results"][8]['title'])
print(req_json["results"][8]['poster_path'])
print(req_json["results"][8]['release_date'])
print(req_json["results"][8]['vote_count'])

if __name__ == '__main__':
    app.run(port=8080, debug=True)