from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.movieActor import MovieActor
from flask_app.models import movie

class Actor:
    db =  'FebMarMovies'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.movie = None
        self.actorMovie = None
        self.movies = []

    
    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM actor;'
        results = connectToMySQL(cls.db).query_db(query)
        actors = []
        for row in results:
            actors.append(cls(row))
        return actors

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM actor WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) <1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO actor (firstName, lastName) VALUES (%(firstName)s, %(lastName)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE actor SET firstName=%(firstName)s, lastName=%(lastName)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM actor WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def actorMovies(cls, data):
        query = 'SELECT * FROM actor LEFT JOIN movie_has_actor on actor.id = movie_has_actor.actor_id LEFT JOIN movie on movie_has_actor.movie_id = movie.id WHERE actor.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        actor = cls(results[0])
        for row in results:
            actorMovieData = {
                'id': row['movie_has_actor.id'],
                'movie_id': row['movie_id'],
                'actor_id': row['actor_id']
            }
            oneActorMovie = MovieActor(actorMovieData)
            actor.actorMovie = oneActorMovie
            movieData = {
                'id': row['movie.id'],
                'title': row['title'],
                'year': row['year'],
                'genre': row['genre'],
                'description': row['description'],
                'createdAt': row['actor.createdAt'],
                'updatedAt': row['actor.updatedAt'],
            }
            oneMovie = movie.Movie(movieData)
            actor.movie = oneMovie
            actor.movies.append(actor)
        return actor.movies

    # instance method to call just the full name vs each piece
    def actorName(self):
        return f'{self.firstName} {self.lastName}'