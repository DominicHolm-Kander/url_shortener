from app import app, URL, db
from flask import render_template, redirect, request
from .shortener import shortener

@app.route('/')
def index():
    return render_template('index.html', input_url = "you haven't provided a url", shortened_url = "no url to shorten")

@app.route('/shortened_url/')
def shortened_url():
    url = request.args.get('url')
    shortened_url = shortener()
    newURL = URL(regular_url=url, shortened_url=shortened_url)
    db.session.add(newURL)
    db.session.commit()
    return render_template('index.html', input_url = url, shortened_url = "localhost:5000/shortened/" + shortened_url)

@app.route("/shortened/<string:shortened_url>")
def redirect_to_page(shortened_url):
    full_url = URL.query.filter_by(shortened_url = shortened_url).first()
    only_url = full_url.regular_url
    return redirect('https://' + only_url)