from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.item import Items

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['POST'])
def register():
    isValid = User.validate(request.form)
    if not isValid:
        flash('Something went wrong')
        return redirect('/')
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    if not id:
        flash("Something went wrong!")
        return redirect('/')
    session['user_id'] = id
    flash(f'You are now logged in')
    return redirect('/dashboard/')

@app.route('/login/', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data)
    if not user:
        flash("Invalid Login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Wrong password")
        return redirect('/')
    session['user_id'] = user.id
    flash(f'You are now logged in {user.firstName}')
    return redirect('/dashboard/')


@app.route('/logout/')
def logout():
    session.clear()
    flash("You have been logged out")
    return redirect('/')


@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.getOne(data)
        # Here is where we are calling the join 
        usersItems = User.userItems(data)
        return render_template('dashboard.html', user=user, usersItems=usersItems)