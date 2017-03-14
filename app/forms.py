from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    age = StringField('age', validators=[InputRequired()])
    gender = StringField('gender', validators=[InputRequired()])
    biography = StringField('biography', validators=[InputRequired()])
    pic = FileField('pic', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'images only')])