import functools

import sqlite3 as sql

from flask import render_template


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
def get_veterans(uname = None):
    """
    @purpose: Runs SQL commands to querey the database for information on veterans. 
    @args: The username of the veteran. None if the username is not provided.
    @returns: A list with one or more veterans.
    """
    vet = None
    if uname:
        command = "SELECT * FROM veterans WHERE username = '%s' " %uname
    else:
        command = "SELECT username, name, years_served, branch, rank FROM veterans"
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(command)
        if uname:
            vet = cur.fetchone()
        else:
            vet = cur.fetchall()
        cur.close()
    return vet[0:10]

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
    
def get_posts(orgid = None):
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

def auth_user(username, hashed_password = None):
    """
    @purpose: Check to see if user has authentication in our database. Whether that be password auth or organization auth.
    @args: The username of the veteran and the hashed_password if needing to check password.
    @returns: A tupe if the user is in the appropriate table. None if they are not in the right table. 
    """
    valid = None
    if hashed_password is None:
        command = "SELECT * FROM partof WHERE username = '%s' AND position = 'owner'" %username
    else:
        command = ("SELECT * FROM passhash WHERE username = '%s' AND hash = '%s'" %username %hashed_password)
    print (command)
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(command)
        valid = cur.fetchone()
        cur.close()
    return valid

