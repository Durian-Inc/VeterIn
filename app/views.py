# views.py

from flask import render_template, abort, session, request, jsonify
from json import dumps

from app import app
from app.utils import uses_template, get_veterans, get_organization, get_posts, auth_user, get_free_veterans, create_user, find_hash, get_row_count, create_organization


@app.route('/')
@uses_template('index.html')
def index():
    sqlposts = get_posts()
    posts = []
    print (get_row_count("veterans"))
    for val in sqlposts:
        post = {
            'org_name': val[3],
            'org_image': val[4],
            'text': val[2],
            'media': val[1],
            'date_time': val[0]
        }
        posts.append(post)

    return {
        'posts': posts
    }


# function to take veteran credentials and present them on the profile page
@app.route('/veteran/<username>', methods=['GET'])
@uses_template('veteran.html')
def vetpro(username):
    vet = get_veterans(username)
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
    # org_posts = get_posts(int(id))
    # TODO
    # Import posts into the organization's page
    if org is None:
        abort(404)

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


@app.route('/api/waypoints', methods=['GET'])
def api_waypoints():
    # lat long name link-to-profile
    orgs = get_organization()
    orgs_list = []
    for org in orgs:
        orgs_list.append({
            'id': org[0],
            'name': org[1],
            'location': org[2]
        })
    return dumps(orgs_list)


@app.route('/api/hires', methods=['GET'])
def api_hires():
    if 'username' in session and auth_user(session['username']):
        vets = get_veterans()
        vets_list = []
        for vet in vets:
            vets_list.append({
                'username': vet[0],
                'name': vet[1],
                'skills': vet[2],
                'years_served': vet[3],
                'rank': vet[4],
                'branch': vet[5],
                'bio': vet[6],
                'contact': vet[8],
                'image': vet[7]
            })
        return dumps(vets_list)
    else:
        organizations = get_organization()
        orgs_list = []
        for org in organizations:
            orgs_list.append({
                'id': org[0],
                'name': org[1],
                'image': org[3],
                'profit': org[6]
            })
        return dumps(orgs_list)


@app.route('/hiring')
def hiring():
    return render_template('hiring.html')


# TODO
@app.route('/add/organization')
def register_org():
    # UPLOAD_FOLDER = '/path/to/the/uploads'
    # ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        organization = {
            'id': get_row_count("organization")+1,
            'name': request.form['name'],
            'location': request.form['location'],
            'url': request.form['url'],
            'industry': request.form['industry'],
            'profit': request.form['profit'],
            'bio': request.form['bio'],
            'contact': request.form['contact'],
            'image': "orgdefault.png"
        }
        create_organization(organization)
        abort(404)

# TODO
# @app.route('/add/post/')


# TODO
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        if auth_user(request.form['username'],
                     find_hash(request.form['password'])) is not None:
            session['username'] = request.form['username']
            abort(404)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # UPLOAD_FOLDER = '/path/to/the/uploads'
    # ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        veteran = {
            'username': request.form['username'],
            'name': request.form['name'],
            'skills': request.form['skills'],
            'years_served': request.form['years_served'],
            'rank': request.form['rank'],
            'branch': request.form['branch'],
            'bio': request.form['bio'],
            'contact': request.form['contact'],
            'image': "default.png"
        }
        pass_hash = find_hash(request.form['password'])

        create_user(veteran, pass_hash)
        abort(404)
