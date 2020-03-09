"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from myfinalproject import app
from myfinalproject.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

app.config['SECRET_KEY'] = 'All You Need Is Love Ta ta ta ta ta'



from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError




from myfinalproject.Models.QueryFormStructure import UserRegistrationFormStructure 

from myfinalproject.Models.Forms import ExpandForm
from myfinalproject.Models.Forms import CollapseForm

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

###from DemoFormProject.Models.LocalDatabaseRoutines import IsUserExist, IsLoginGood, AddNewUser 

db_Functions = create_LocalDatabaseServiceRoutines() 

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
           img_american_flag = '/static/images/lebrondavis.jpg',
           img_ethereum = '/static/images/pircegarrnet.jpg',
           img_lebron = '/static/images/lebronwade.jpg',
         message='My home page.'


    )

@app.route('/contact')
def contact():

    print("Contact")

    """Renders the contact page."""

    return render_template(
        'contact.html',
        year=datetime.now().year,
        img_tichonet = '/static/images/tichonet.png',
        img_oran = '/static/images/contact.jpg'
    )
@app.route('/about')
def about():

    print("About")

    """Renders the about page."""
    return render_template(
        'about.html',
        year=datetime.now().year,
        img_tichonet = '/static/images/tichonet.png'
    )

@app.route('/data_model')
def data_model():
    """Renders the about page."""
    return render_template(
        'data_model.html',
        year=datetime.now().year,
        img_one = '/static/images/lebronvsjaylen.jpg',
        img_two = '/static/images/lebronandkobe.jpg'

    )

@app.route('/data/nba' , methods = ['GET' , 'POST'])
def nba():

    print("nba")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    # df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\trump.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/nba_team_stats_00_to_18.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'nba.html',
        title='NBA',
        year=datetime.now().year,
        message='NBA Dataset Page.',
        img_one = '/static/images/rayallen.jpg' ,
        img_two = '/static/images/MammbaForever.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/data/nbafinals' , methods = ['GET' , 'POST'])
def nbafinals():

    print("nbafinals")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    # df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\trump.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/championsdata.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'nbafinals.html',
        title='nbafinals',
        year=datetime.now().year,
        message='NBA Dataset Page.',
        img_one = '/static/images/rayallen.jpg' ,
        img_two = '/static/images/MammbaForever.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )


    

@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )







