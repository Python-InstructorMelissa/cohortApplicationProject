from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.movie import Movie
from flask_app.models.actor import Actor
from flask_app.models.movieActor import MovieActor


@app.route('/movies/')
def movies():
    # if 'user_id' not in session:
    #     flash('You need to be logged in to view this page')
    #     return redirect('/')
    return render_template('movies.html', movies=Movie.getAll(), actors=Actor.getAll())

@app.route('/movies/<int:movie_id>/connectActor/', methods=['post'])
def connectActor(movie_id):
    data = {
        'movie_id': movie_id,
        'actor_id': request.form['actor_id'],
    }
    MovieActor.save(data)
    return redirect('/movies')

@app.route('/movies/add/')
def addMovie():
    # if 'user_id' not in session:
    #     flash('You need to be logged in to view this page')
    #     return redirect('/')
    return render_template('addMovie.html')

@app.route('/movies/create/', methods=['post'])
def createMovie():
    data = {
        'title': request.form['title'],
        'year': request.form['year'],
        'genre': request.form['genre'],
        'description': request.form['description'],
    }
    Movie.save(data)
    print('create movie, controller: ', data)
    return redirect('/movies/')