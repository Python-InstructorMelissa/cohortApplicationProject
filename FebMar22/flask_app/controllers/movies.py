from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.movie import Movie
from flask_app.models.actor import Actor
from flask_app.models.movieActor import MovieActor
from flask_app.models.user import User


@app.route('/movies/')
def movies():
    if 'user_id' not in session:
        flash('You need to be logged in to view this page')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('movies.html', movies=Movie.getAll(), actors=Actor.getAll(), user=User.getOne(data))

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
    if 'user_id' not in session:
        flash('You need to be logged in to view this page')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('addMovie.html', user=User.getOne(data))

@app.route('/movies/create/', methods=['post'])
def createMovie():
    data = {
        'title': request.form['title'],
        'year': request.form['year'],
        'genre': request.form['genre'],
        'description': request.form['description'],
        'user_id': request.form['user_id']
    }
    Movie.save(data)
    print('create movie, controller: ', data)
    return redirect('/movies/')

@app.route('/movies/<int:movie_id>/view/')
def viewMovie(movie_id):
    if 'user_id' not in session:
        flash('You need to be logged in to view this page')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    movieData = {
        'id': movie_id
    }
    actors = Movie.movieActors(movieData)
    return render_template('viewMovie.html', movie=Movie.getOne(movieData), user=User.getOne(data), users=User.getAll(), actors = Movie.movieActors(movieData))

@app.route('/movies/<int:movie_id>/edit/')
def editMovie(movie_id):
    if 'user_id' not in session:
        flash('You need to be logged in to view this page')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    movieData = {
        'id': movie_id
    }
    return render_template('editMovie.html', movie=Movie.getOne(movieData), user=User.getOne(data))

@app.route('/movies/<int:movie_id>/update/', methods=['POST'])
def updateMovie(movie_id):
    data = {
        'id': movie_id,
        'title': request.form['title'],
        'year': request.form['year'],
        'genre': request.form['genre'],
        'description': request.form['description'],
    }
    Movie.update(data)
    flash("You have updated the movie")
    return redirect('/movies/')

@app.route('/movies/<int:movie_id>/delete/')
def deleteMovie(movie_id):
    movieData = {
        'id': movie_id
    }
    Movie.delete(movieData)
    flash("The movie was deleted")
    return redirect('/movies/')