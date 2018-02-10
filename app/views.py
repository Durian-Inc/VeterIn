# views.py

from flask import render_template

from app import app
from app.utils import uses_template


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/veteran/<username>', methods=['GET'])
@uses_template('veteran.html')
def vetpro(username):
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
