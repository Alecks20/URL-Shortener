
from flask import Flask, request, jsonify, redirect
import pymongo
import os

client = pymongo.MongoClient(os.environ["MONGO_URL"])

app = Flask(__name__)

@app.route("/<url>/")
async def get_url(url):
    d = client.url_shortener.redirects.find_one({"id": url})
    return redirect(d["link"])


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=80)