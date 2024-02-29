
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class MyForm(FlaskForm):
 
 name = StringField('Name',validators=[InputRequired()])
 email = StringField('Name',validators=[InputRequired()])
 subject = StringField('Name',validators=[InputRequired()])
 message = StringField('Name',validators=[InputRequired()])
