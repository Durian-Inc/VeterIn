import functools

import sqlite3 as sql

from flask import render_template

from hashlib import sha256

DATABASE = 'app/database/vets.db'


def uses_template(template):
    """Wrap a function to add HTML template rendering functionality."""
    def wrapper(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            template_path = template
            ctx = func(*args, **kwargs)
            if type(ctx) is dict:
                try:
                    return render_template(template_path,
                                           veteran=ctx['veteran'])
                except KeyError:
                    try:
                        return render_template(template_path,
                                               organization=ctx['organization']
                                               )
                    except KeyError:
                        return render_template(template_path,
                                               posts=ctx['posts'])
            else:
                return ctx
        return wrapped
    return wrapper


# Database functions:
def get_veterans(uname=None):
    """
    @purpose: Runs SQL commands to querey the database for information on veterans. 
    @args: The username of the veteran. None if the username is not provided.
    @returns: A list with one or more veterans.
    """
    vet = None
    if uname:
        command = "SELECT * FROM veterans WHERE username = '%s' " %uname
    else:
        command = "SELECT * FROM veterans"
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(command)
        if uname:
            vet = cur.fetchone()
        else:
            vet = cur.fetchall()
        cur.close()
    if vet is not None and len(vet) > 10:
        return vet[0:10]
    else: 
        return vet

def get_free_veterans():
    """
    @purpose: Get all of the free veterans in the database.
    @args:
    @returns: A list of tuple elements of all the free veterans. 
    """
    all_vets = None
    free_vets = []
    taken_vets = None
    taken_vets_command = "SELECT username FROM partof"
    all_vets_command = "SELECT * FROM veterans"
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(all_vets_command)
        all_vets = cur.fetchall()
        cur.execute(taken_vets_command)
        taken_vets = cur.fetchall()
        cur.close()
    for vet in all_vets:
        found_match = False
        for veter in taken_vets:
            if vet[0] == veter[0]:
                found_match = True
                break
        if found_match == False:
            free_vets.append(vet)
    return free_vets
    
def get_organization(orgid = None):
    """
    @purpose: Runs SQL commands to querey the database for information on organizations. 
    @args: The id of the organization. None if one is not provided and all organizations are needed.
    @returns: A list with one or more organizations.
    """
    organization = None
    if orgid is None:
        command = "SELECT * FROM organization"
    else:
        command = "SELECT * FROM organization WHERE id = %d " % orgid
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(command)
        if orgid:
            organization = cur.fetchone()
        else:
            organization = cur.fetchall()
        cur.close()
    return organization[0:10]


def get_posts(orgid=None):
    """
    @purpose: Runs SQL commands to querey the database for all the posts
    @args: The id of the organization. None if one is not provided and all posts are needed.
    @returns: A list with up to 10 posts.
    """
    posts = None
    if orgid is None:
        command = "SELECT P.postdate, P.image, P.posttext, O.name, O.image FROM post as P, organization as O WHERE P.posterid = O.id"
    else:
        command = "SELECT P.postdate, P.image, P.posttext, O.name, O.image FROM post AS P, organization AS O WHERE P.posterid = O.id AND O.id = %d " % orgid
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(command)
        posts = cur.fetchall()
        cur.close()
    return posts[0:10]


# password handling and hashing

def find_hash(password):
    return sha256(password.encode('utf-8')).hexdigest()


def auth_user(username, hashed_password=None):
    """
    @purpose: Check to see if user has authentication in our database. Whether
    that be password auth or organization auth.
    @args: The username of the veteran and the hashed_password if needing to
    check password.
    @returns: A tupe if the user is in the appropriate table. None if they are
    not in the right table.
    """
    valid = None
    if hashed_password is None:
        command = "SELECT * FROM partof WHERE username = '%s' AND position = 'owner'" %username
    else:
        command = ("SELECT * FROM passhash WHERE username = '%s' AND hash = '%s'" %username %hashed_password)
    print(command)
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(command)
        valid = cur.fetchone()
        cur.close()
    return valid

def create_user(new_user, hashed_password):
    """
    @purpose: Adds a new user to the database and hashes their password
    @args: List of all the elements that will be added to the database
    @returns: 
    """
    columns = ', '.join(new_user.keys())
    placeholders = ', '.join('?' * len(new_user))
    insert_command = "INSERT INTO veterans ({}) VALUES ({})".format(columns, placeholders)
    conn = sql.connect(DATABASE)
    cur = conn.cursor()
    cur.execute(insert_command, new_user.values())
    conn.commit()
    hash_command = "INSERT INTO passhash (username, hash) VALUES ('%s', '%s')".format(new_user["username"],hashed_password)
    cur.execute(hash_command)
    conn.close()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
