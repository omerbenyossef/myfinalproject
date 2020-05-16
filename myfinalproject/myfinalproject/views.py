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
from myfinalproject.Models.QueryFormStructure import LoginFormStructure

from myfinalproject.Models.Forms import ExpandForm
from myfinalproject.Models.Forms import CollapseForm
from myfinalproject.Models.Forms import NBA

import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure



from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)


###from DemoFormProject.Models.LocalDatabaseRoutines import IsUserExist, IsLoginGood, AddNewUser 
### this is the home page.

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
### contact page
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

### about page
@app.route('/about')
def about():

    print("About")

    """Renders the about page."""
    return render_template(
        'about.html',
        year=datetime.now().year,
        img_tichonet = '/static/images/tichonet.png'
    )
### data model page
@app.route('/data_model')
def data_model():
    """Renders the about page."""
    return render_template(
        'data_model.html',
        year=datetime.now().year,
        img_one = '/static/images/lebronvsjaylen.jpg',
        img_two = '/static/images/lebronandkobe.jpg'

    )
### nba data page - in this page there are explanations about the data.
@app.route('/data/nba' , methods = ['GET' , 'POST'])
def nba():

    print("nba")

    """Renders the about page."""
    
    form1 = ExpandForm()
    #  the button expand is to open that data set on the site.
    form2 = CollapseForm()
    #  the button collapse os to close the data set on the site.

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


    
### the register page on the site - where you can register a new user.
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

### the query page - this page allowing to investigate the database.
@app.route('/query' , methods = ['GET' , 'POST'])
def query():

    

    form1 = NBA()
    chart = 'static/images/chasestats.jpg'

   
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/nba_team_stats_00_to_18.csv'))
    l = list(set(df['TEAM'].tolist()))  
    m = list(zip(l,l))
    form1.teama.choices = m 
    form1.teamb.choices = m 
    l = list(set(df['SEASON'].tolist()))  
    m = list(zip(l,l))
    form1.season.choices = m




    if request.method == 'POST':
        teama = form1.teama.data
        teamb = form1.teamb.data
        season = form1.season.data
        df = df[['SEASON','TEAM','WIN%','FG%','3P%','FT%']]
        df = df.loc[df['SEASON']== season]
        df = df.loc[(df['TEAM']== teama)|(df['TEAM']==teamb)]
        df['WIN%'] = df['WIN%'].apply(lambda x:100*x)
        df = df.drop('SEASON',1)
        print (df)
        df = df.set_index("TEAM")
        df = df.transpose()
        print (df)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        df.plot(ax = ax , kind = 'bar', figsize = (24, 8) , fontsize = 22 , grid = True)
        chart = plot_to_img(fig)

    
    return render_template(
        'query.html',
        form1 = form1,
        chart = chart
    )

def plot_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String


### login page - You can connect with your user and then investigate the database.
@app.route('/Login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)
    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('You Successfully Login To The Website!')
            return redirect('query')
        else:
            flash('Error In - Username and/or Password!!!')
   
    return render_template(
        'Login.html', 
        form=form, 
        title='In This Page You Can Login To The Website:',
        year=datetime.now().year,
    )








