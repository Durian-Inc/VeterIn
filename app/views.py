# views.py

from flask import render_template
from app import app
from app.utils import uses_template


@app.route('/')
def index():
    return render_template("index.html")

# Profile functions : Veterans / Organizations


# function to take veteran credentials and present them on the profile pagei
@app.route('/veteran/<username>', methods=['GET'])
@uses_template('veteran.html')
def vetpro(username):
    vet = {
        'username': "daddyd",
        'name': "Derek Hanger",
        'skills': "code,bees,music stuff,orange chicken",
        'years_served': 2,
        'rank': "man",
        'branch': "lovely boy",
        'bio': "once from fair town, always from fair town",
        'image': "derek.png"
    }

    return {
        'veteran': vet
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
