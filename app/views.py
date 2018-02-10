# views.py

import sqlite3 as sql
from flask import render_template, flash, g

from app import app
from app.utils import uses_template


DATABASE = 'app/database/vets.db'

def get_veteran(username):
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("IN")

    
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/veteran/<username>', methods=['GET'])
@uses_template('veteran.html')
def vetpro(username):
    veteran = get_veteran(username)
    vet = {
        'username': "daddyd",
        'name': "Derek Hanger",
        'skills': "code,bees,music stuff,orange chicken",
        'years_served': 2,
        'rank': "man",
        'branch': "emo bitch",
        'bio': "once from fair town, always from fair town",
        'image': "derek.png"
    }

    return {
        'veteran': vet
    }
