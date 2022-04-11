from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' not in session:
        flash('You need to be logged in to view this page')
        return render_template('index.html')
    return redirect('/movies/')

@app.route('/register/', methods=['POST'])
def register():
    isValid = User.validate(request.form)
    if not isValid: # if isValid = False this is triggered
        return redirect('/')
    newUser = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(newUser)
    if not id:
        flash("You dun screwed something up")
        return redirect('/')
    session['user_id'] = id
    flash("You have now been logged in")
    return redirect('/movies/')

@app.route('/login/', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data)
    # you can also just do the following vs the above
    # User = user.get_by_email(request.form)
    if not user:
        flash("That email is not being used partner please use the right one")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Wrong password')
        return redirect('/')
    session['user_id'] = user.id
    flash("You got it right and are now logged back in Welcome back!")
    return redirect('/movies/')

@app.route('/logout/')
def logout():
    session.clear()
    flash("You have logged out")
    return redirect('/')

@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        flash('You need to be logged in to view this page')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('dashboard.html', user=User.getOne(data), movies=User.userMovies(data))

@app.route('/imdb/')
def imdb():
    return render_template('imdbAPI.html')