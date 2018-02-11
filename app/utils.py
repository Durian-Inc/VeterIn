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

def get_veteran(uname):
    
    vet = None
    command = "SELECT * FROM veterans WHERE username = '%s' " %uname
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(command)
        vet = cur.fetchone()
        cur.close()
    return vet

def get_organization(orgid):
    organization = None
    command = "SELECT * FROM organization WHERE id = %d " % orgid
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(command)
        organization = cur.fetchone()
        cur.close()
    return organization
    