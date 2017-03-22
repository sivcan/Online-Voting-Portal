from flask import Flask, render_template, request, redirect, \
jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Parties
from flask import session as login_session
from functools import wraps 
import httplib2
import json
from flask import make_response


app = Flask(__name__)

APPLICATION_NAME = "Restaurant Menu Application"

#Connect to Database and create database session
engine = create_engine('sqlite:///votingsystem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/', methods=['GET','POST'])
def Aadhar():
    if request.method == 'POST':
        aadharNumber = request.form['aadhar']
        if aadharNumber.isdigit() and len(aadharNumber) == 12 :
            try : 
                user = session.query(User).filter_by(aadhar=aadharNumber).one()
                return render_template('index.html', flash = 'User has already voted!', flashType = 'danger')
            except:
                user = User(aadhar=aadharNumber, voted=True)
                session.add(user)
                session.commit()
                parties = session.query(Parties).all()
                return render_template('vote.html', aadharNumber = aadharNumber, parties = parties)
        else :
            return render_template('index.html', flash = 'Enter the Correct Aadhar Card Number', flashType = 'danger')
        
    else : 
        return render_template('index.html', flash = None)

@app.route('/vote/<int:partyID>', methods=['GET', 'POST'])
def Vote(partyID):
    party = session.query(Parties).filter_by(id=partyID).one()
    party.count = party.count + 1;
    session.add(party)
    session.commit()
    return render_template('index.html', flash = 'You have sucessfully voted.', flashType='success')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    
    
    
    
    
    