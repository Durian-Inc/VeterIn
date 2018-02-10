# views.py

import sqlite3
from flask import render_template, flash, g

from app import app

DATABASE = 'app/database/vets.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def index():
    cur = get_db().cursor()
    return render_template("index.html")
