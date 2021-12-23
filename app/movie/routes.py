from flask import Blueprint
from flask.templating import render_template
from app.forms import datainputform

auth=Blueprint('movie',__name__, template_folder='movie.templates')

@auth.route('/datainput')
def datainput():
    form=datainputform()
    return render_template('datainput.html', form = form)

