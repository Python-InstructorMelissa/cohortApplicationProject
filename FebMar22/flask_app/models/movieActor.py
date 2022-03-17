from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.movie import Movie
# from flask_app.models.actor import Actor

class MovieActor:
    db = 'FebMarMovies'
    def __init__(self, data):
        self.id = data['id']
        self.movie_id = data['movie_id']
        self.actor_id = data['actor_id']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO movie_has_actor (movie_id, actor_id) VALUES (%(movie_id)s, %(actor_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)