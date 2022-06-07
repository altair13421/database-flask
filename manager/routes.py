from manager import app, db
from flask import Flask, flash, redirect, render_template, url_for
from .forms import DataForm
from .models import Data

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = "HOME")


@app.route('/form', methods = ['GET', 'POST'])
def form():
    form = DataForm()
    if form.validate_on_submit():
        flash(f'Successfully Added Data For {form.name.data}')
        formdata = Data(name = f'{form.name.data}', age = form.age.data, description = f'{form.description.data}')
        db.session.add(formdata)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', title = 'Form', form=form)

@app.route('/history', methods=['POST', 'GET'])
def historytable():
    dbdata = Data.query.all()
    return render_template('consultation-history.html', title='HISTORY', dataset = dbdata)

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    deldata = Data.query.get(id)
    db.session.delete(deldata)
    db.session.commit()
    return redirect(url_for('historytable'))
