from flask import render_template, session, redirect, url_for, current_app, request
from .. import db
from ..models import Actor
from . import main
from .forms import NameForm, RadForm
from datetime import datetime

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    rad_form = RadForm()
    
    if rad_form.validate_on_submit():
        print(rad_form.example.data)
        
    select = request.form.get('col_select')
    column_choices = [{'name':'first_name'}, {'name':'last_name'}, {'name':'last_update'}]
    
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Name has been changed')
        
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))

  
    if request.method == "POST":
        print(select)
        df = return_df(select)
        df = df.style.render()
        return render_template('index.html',
                           current_time=datetime.utcnow(),
                           form=form,
                           name=session.get('name'),
                           column_choices=column_choices,
                           df=df,
                           rad_form=rad_form)
        
    return render_template('index.html',
                           current_time=datetime.utcnow(),
                           form=form,
                           name=session.get('name'),
                           column_choices=column_choices,
                           rad_form=rad_form)

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())



