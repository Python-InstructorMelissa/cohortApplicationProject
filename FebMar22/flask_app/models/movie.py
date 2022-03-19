from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import movieActor
from  flask_app.models import actor

class Movie:
    db = 'FebMarMovies'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.year = data['year']
        self.genre = data['genre']
        self.description = data['description']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
        self.movieActor = None
        self.theActor = None

    
    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM movie;'
        results = connectToMySQL(cls.db).query_db(query)
        movies = []
        for row in results:
            movies.append(cls(row))
        return movies

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM movie WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) <1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO movie (title, year, genre, description, user_id) VALUES (%(title)s, %(year)s, %(genre)s, %(description)s, %(user_id)s);'
        print('save movie model:', data)
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE movie SET title=%(title)s, year=%(year)s, genre=%(genre)s, description=%(description)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM movie WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def movieActors(cls, data):
        query = 'SELECT * FROM movie LEFT JOIN movie_has_actor on movie.id = movie_has_actor.movie_id LEFT JOIN actor on movie_has_actor.actor_id = actor.id WHERE movie.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        # print("results in model: ", results)
        theActors = []
        # movie = cls(results[0])
        for row in results:
            movie = cls(row)
            movieActorData = {
                'id': row['movie_has_actor.id'],
                'movie_id': row['movie_id'],
                'actor_id': row['actor_id']
            }
            # Below line says var = file.Class(Class RowData)
            movieActorRow = movieActor.MovieActor(movieActorData)
            # line 61 (referencing the Class row or "self". self.movieActor from constructor (line 16) = the data)
            movie.movieActor = movieActorRow
            # this is another way to do the above 2 lines
            # movie.movieActor = movieActor.MovieActor(movieActorData)
            actorData = {
                'id': row['actor.id'],
                'firstName': row['firstName'],
                'lastName': row['lastName'],
                'createdAt': row['actor.createdAt'],
                'updatedAt': row['actor.updatedAt'],
            }
            actorRow = actor.Actor(actorData)
            movie.theActor = actorRow
            # Below is appending the Class data that now has movie, movieActor, and theActor as a single object into the list created on line 58 inside this function
            theActors.append(movie)
        return theActors

