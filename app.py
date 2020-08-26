''' Important imports to allow us connect Flask to database'''
import os 
from flask import Flask, render_template

#talk to sqlite databse
from flask_sqlalchemy import SQLAlchemy

# Helps to write data for databse to create 
# the tables in the database
from flask_migrate import Migrate 


app = Flask(__name__)

# Configuring flask with database
basedir = os.path.abspath(os.path.dirname(__file__))

# setting uo databse location on our system
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'ransdb.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

# CREATING OUR DATABASE MODELS WITH PYTHON CLASSES
class CountryReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    total_cases = db.Column(db.Integer)
    recoveries = db.Column(db.Integer)
    activecase = db.Column(db.Integer)
    total_deaths = db.Column(db.Integer)

    def __init__(self,name,total_cases,recoveries,activecase,total_deaths):
        self.name = name
        self.total_cases = total_cases
        self.recoveries = recoveries
        self.activecase = activecase
        self.total_deaths = total_deaths
        
    def __repr__(self):
        return f'{self.name} has {self.total_cases}'








# Configuring our flask route
@app.route('/')
def index():
    allcountryreport = CountryReport.query.all()
    return render_template('index.html',allcountryreport = allcountryreport)



if __name__ == '__main__':
    app.run()

