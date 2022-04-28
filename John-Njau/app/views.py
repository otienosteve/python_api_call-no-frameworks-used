from flask import render_template
from app import app
from urllib import request, parse
import json


@app.route('/')
def index():
    title = "Flask -- Working with Apis and json data"

    requestVariables = {
        "api_key": '22f3e85e05becdb7e502c1f391dbd90d',
        'limit': '10'
    }

    encodeVars = parse.urlencode(requestVariables)
    API_BASE_URL = 'https://api.themoviedb.org/3/movie/popular?'
    req_open = request.urlopen(API_BASE_URL + encodeVars)
    req_read = req_open.read()
    req_json = json.loads(req_read)
    movies = req_json['results']

    return render_template('index.html', title=title, movies=movies)
