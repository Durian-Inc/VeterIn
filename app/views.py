# views.py

import sqlite3 as sql
from flask import render_template, flash, g

from app import app
from app.utils import uses_template


DATABASE = 'app/database/vets.db'

def get_veteran(uname):
    vet = None
    command = "SELECT * FROM veterans where username = '%s' " %uname
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(command)
        vet = cur.fetchone()
        cur.close()
    return vet
    
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/veteran/<username>', methods=['GET'])
@uses_template('veteran.html')
def vetpro(username):
    vet = get_veteran(username)
    for val in vet:
        print val
    print len(vet)
    veteran = {
        'username': vet[0],
        'name': vet[1],
        'skills': vet[2],
        'years_served': vet[3],
        'rank': vet[4],
        'branch': vet[5],
        'bio': vet[6],
        'contact': vet[8],
        'image': vet[7]
    }

    return {
        'veteran': veteran
    }
