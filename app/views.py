# views.py

from flask import render_template, abort
from app import app
from app.utils import uses_template, get_veteran, get_organization


@app.route('/')
def index():
    return render_template("index.html")

# Profile functions : Veterans / Organizations


# function to take veteran credentials and present them on the profile page
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
    org = get_organization(int(id))
    for val in org:
        print (val)
    print (len(org))
    organization = {
        'id': org[0],
        'name': org[1],
        'location': org[2],
        'image': org[3],
        'bio': org[7],
        'url': org[4],
        'contact': org[8],
        'type': org[5]
    }

    return {
        'organization': organization
    }


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

# End of Profile functions
