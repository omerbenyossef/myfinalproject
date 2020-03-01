"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from myfinalproject import app
from flask import request

import pandas as pd

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from myfinalproject.Models.Forms import ExpandForm
from myfinalproject.Models.Forms import CollapseForm



from os import path
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
           img_american_flag = '/static/images/nbalogo2.png',
        year=datetime.now().year,
         message='My home page.'


    )

@app.route('/contact')
def contact():

    print("Contact")

    """Renders the contact page."""

    return render_template(
        'contact.html',
        year=datetime.now().year,
        img_tichonet = '/static/imgs/tichonet.png',
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='על הפרויקט',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/data_model')
def data_model():
    """Renders the about page."""
    return render_template(
        'data_model.html',
        title='data model',
        year=datetime.now().year,
        message='my data page.'
    )

@app.route('/register')
def register():
    """Renders the about page."""
    return render_template(
        'register.html',
        title='register',
        year=datetime.now().year,
        message='my data page.'
    )



@app.route('/data/trump' , methods = ['GET' , 'POST'])
def trump():

    print("Trump")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    # df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\trump.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/trump.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'trump.html',
        title='Trump',
        year=datetime.now().year,
        message='Trump dataset page.',
        img_trump = '/static/imgs/trump.jpg',
        img_obama = '/static/imgs/trump.jpg',
        img_bush = '/static/imgs/trump.jpg',
        img_clinton = '/static/imgs/trump.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )



