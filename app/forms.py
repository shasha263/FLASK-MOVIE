from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,DateField,TimeField
from wtforms import validators
from wtforms.validators import data_required

class datainputform(FlaskForm):
    title=StringField('Movie Name',validators=[data_required()])
    description=StringField('Description')
    release_date= DateField('Year Released',validators=[data_required()])
    runtime=TimeField('Movie Runtime',validators=[data_required()])
    submit=SubmitField()
