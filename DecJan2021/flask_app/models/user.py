from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = 'dec-jan-Friday'
    def __init__(self, data):
        pass

    @classmethod
    def getAll(cls):
        pass

    @classmethod
    def getOne(cls, data):
        pass

    @classmethod
    def save(cls, data):
        pass

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass