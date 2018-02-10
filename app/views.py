# views.py

from flask import render_template
from app import app
from app.utils import uses_template


@app.route('/')
@uses_template('index.html')
def index():
    post = {
        'org_name': "MIL$",
        'org_image': "derek.png",
        'text': "ShamHacks 2018",
        'media': "derek.png",
        'date_time': "February 9th, 2018"
    }

    return {
        'posts': [post]
    }

post = {
    'org_name': "MIL$",
    'org_image': "derek.png",
    'text': "ShamHacks 2018",
    'media': "derek.png",
    'date_time': "February 9th, 2018"
}
# function to take veteran credentials and present them on the profile pagei
@app.route('/veteran/<username>', methods=['GET'])
@uses_template('veteran.html')
def vetpro(username):
    vet = {
        'username': "derekhanger",
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

# TODO
# @app.route('/api/waypoints', methods=['GET'])

# TODO
# @app.route('/add/organization')

# TODO
# @app.route('/add/post/')

# TODO
# @app.route('/login')