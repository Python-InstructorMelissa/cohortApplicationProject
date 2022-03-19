from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.actor import Actor
from flask_app.models.user import User

@app.route('/actors/')
def actors():
    if 'user_id' not in session:
        flash('You need to be logged in to view this page')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('actors.html', actors=Actor.getAll(), user=User.getOne(data))

@app.route('/actors/add/')
def addActor():
    if 'user_id' not in session:
        flash('You need to be logged in to view this page')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('addActor.html', user=User.getOne(data))

@app.route('/actors/create/', methods=['POST'])
def createActor():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
    }
    Actor.save(data)
    flash('New actor created')
    return redirect('/actors/')