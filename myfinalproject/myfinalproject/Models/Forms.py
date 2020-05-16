from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired
from wtforms.validators import InputRequired


### these are the action buttons to open and close the data.
class ExpandForm(FlaskForm):

	submit1 = SubmitField('Expand')
	name="Expand"
	value="Expand"
 
class CollapseForm(FlaskForm):
	submit2 = SubmitField('Collapse')
	name="Collapse"
	value="Collapse"


	### this class requests from the user to select two teams and a season to compare between them.
class NBA(FlaskForm):
	teama = SelectField('Select a team:' , validators = [DataRequired] )
	teamb = SelectField('Select a team:' , validators = [DataRequired] )
	season = SelectField('Select season:' , validators = [DataRequired] )
	subnmit = SubmitField('submit')




	### This class requests the user name and password from the user.
	### if the data that entered by the user is correct he will be allowed to continue and be passed to the quarry page where he will be able to investigate the data.
	
class LoginFormStructure(FlaskForm):
	username   = StringField('Username:  ' , validators = [DataRequired()])
	password   = PasswordField('Password:  ' , validators = [DataRequired()])
	submit = SubmitField('Submit')



	