import re
from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.movie import Movie
from flask_app.models.actor import Actor
from flask_app.models.movieActor import MovieActor

@app.route('/')
def index():
    return redirect('/movies/')

@app.route('/movies/')
def movies():
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
    return render_template('addMovie.html')