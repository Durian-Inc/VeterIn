# views.py

import sqlite3 as sql
from flask import render_template, abort
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

# Profile functions : Veterans / Organizations


# function to take veteran credentials and present them on the profile pagei
@app.route('/veteran/<username>', methods=['GET'])
@uses_template('veteran.html')
def vetpro(username):
    vet = get_veteran(username)
    if vet is None:
        abort(404)
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


@app.route('/organization/<id>', methods=['GET'])
@uses_template('organization.html')
def orgpro(id):
    org = {
        'id': 0,
        'name': "MIL$",
        'location': "here",
        'image': "derek.png",
        'bio': "is an up and coming crypto currency or something I think",
        'url': "vetstoreusa.com",
        'contact': "1-800-PLZ-DONT"
    }

    return {
        'organization': org
    }


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

# End of Profile functions
