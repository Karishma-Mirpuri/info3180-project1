from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    age = StringField('Age', validators=[InputRequired()])
    gender = StringField('Gender', validators=[InputRequired()])
    biography = StringField('Biography', validators=[InputRequired()])
    file = StringField('File', validators=[InputRequired()])