#!/bin/python3

from re import sub
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    # sr = "/wholesomememes"
    # url = http://meme-api.heroku.com/gimme" + sr
    url = "https://meme-api.heroku.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = repsonse["subreddit"]
    return meme_large, subreddit

@app.route("/")

def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host="0.0.0.0", port=80)