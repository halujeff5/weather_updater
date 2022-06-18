import os
from forms import AddForm
from flask import Flask, render_template, url_for, redirect, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
import json
from flask import Response

url = 'http://api.weatherstack.com/current'
response = requests.get(url)
url_params = {'access_key': '576f984270efbce3f34b28b0066c17db', 'query': 'Miami'}        
response = requests.get(url, params=url_params)
weather = response.text
weather_json = json.loads(weather)
weather_json['location']



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
Migrate(app,db)
 

class weather(db.Model):
    __tablename__ = 'weather'
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.Text)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Temperature: {self.name}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/report')
def get_json():
    documents=[]
    for b in weather_json:
        documents.append({b[0]:weather_json['location']})
        documents.append({b[1]:weather_json['current']})
    ans = Response(json.dumps(documents[0:2]), mimetype='application/json')
    return ans

@app.route('/add', methods=['GET', 'POST'])
def add_city():
    url = 'http://api.weatherstack.com/current'
    response = requests.get(url)
    url_params = {'access_key': '576f984270efbce3f34b28b0066c17db', 'query': 'Los Angeles'}        
    response = requests.get(url, params=url_params)
    weather = response.text
    weather_json = json.loads(weather)
    return weather_json

if __name__ == '__main__':
    app.run(debug=True)
