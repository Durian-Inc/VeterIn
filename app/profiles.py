# profiles.py
import uuid

from flask import abort, Flask, flash, redirect, request, session, url_for
from datetime import datetime

app = Flask(__name__)

# template dict
veteran = {
    'username': "bill",
    'name': "billyboy",
    'skills': "none",
    'years_served': "6",
    'rank': "the good one",
    'branch': "army"}


# function to take veteran credentials and present them on the profile page?
@app.route('/veteran/<username>', methods=['GET'])
def vetpro(veteran):
    return
