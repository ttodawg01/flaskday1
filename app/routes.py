from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html', user= 'tony', email='tonydawg@gmail.com')


@app.route('/favorites')
def home():
    return render_template('favorites.html')