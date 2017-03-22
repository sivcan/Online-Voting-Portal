"""
This file is the top level file for the Item Catalog project and
uses the Flask framework.

This project allows users to add items to categories. Users can also
edit and delete their own items.

JSON endpoints are provided for catalog, category, and item.
Authentication is handled by Google's OAuth API and Facebook's OAuth API.

This file contains routes and view functions.
"""

from flask import Flask, render_template, request, redirect, \
jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
#from database_setup import Base, Restaurant, MenuItem, User
from flask import session as login_session
from functools import wraps 
import httplib2
import json
from flask import make_response


app = Flask(__name__)

APPLICATION_NAME = "Restaurant Menu Application"

# Connect to Database and create database session
#engine = create_engine('sqlite:///aadharcard.db')
#Base.metadata.bind = engine
#
#DBSession = sessionmaker(bind=engine)
#session = DBSession()

"""Login check decorator, used to check if the user is logged in or not.
If not logged in, then redirects the user to the login page 
thus preventing unauthorized access to important data."""
def loginCheck(f):
    @wraps(f)
    def userLog(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        else :
            return f(*args, **kwargs)
    return userLog

# Create anti-forgery state token
@app.route('/login')
def showLogin():
    if 'username' in login_session:
        return redirect('/restaurant')
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/aadhar', methods=['POST'])
def checkAadhar():
    return redirect('/vote')

@app.route('/vote')
def vote():
    return render_template('vote.html')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)