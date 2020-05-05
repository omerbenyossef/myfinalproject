from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired
from wtforms.validators import InputRequired

class ExpandForm(FlaskForm):
	submit1 = SubmitField('Expand')
	name="Expand"
	value="Expand"
 
class CollapseForm(FlaskForm):
	submit2 = SubmitField('Collapse')
	name="Collapse"
	value="Collapse"

class NBA(FlaskForm):
	teama = SelectField('Select a team:' , validators = [DataRequired] )
	teamb = SelectField('Select a team:' , validators = [DataRequired] )
	season = SelectField('Select season:' , validators = [DataRequired] )
	subnmit = SubmitField('submit')






class LoginFormStructure(FlaskForm):
	username   = StringField('Username:  ' , validators = [DataRequired()])
	password   = PasswordField('Password:  ' , validators = [DataRequired()])
	submit = SubmitField('Submit')



	