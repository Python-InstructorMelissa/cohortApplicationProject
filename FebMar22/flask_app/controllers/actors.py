from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.actor import Actor

@app.route('/actors/')
def actors():
    # if 'user_id' not in session:
    #     flash('You need to be logged in to view this page')
    #     return redirect('/')
    return render_template('actors.html', actors=Actor.getAll())

@app.route('/actors/add/')
def addActor():
    # if 'user_id' not in session:
    #     flash('You need to be logged in to view this page')
    #     return redirect('/')
    return render_template('addActor.html')

@app.route('/actors/create/', methods=['POST'])
def createActor():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
    }
    Actor.save(data)
    flash('New actor created')
    return redirect('/actors/')